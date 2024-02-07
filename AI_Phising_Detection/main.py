import imaplib
import email
import time
from threading import Thread
import math
import os


import Predict
import Save
import Send


# Set up your credentials and server

username = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
imap_url = 'imap.gmail.com'



def process_email(email_subject, body, email_from):
    try:
        # Here other functions would be called to process the email
        prediction = Predict.predict(body)
        if prediction is not None:
            Save.save_email(email_subject, body, email_from, prediction)
            if Send.send_email(email_subject, email_from, prediction):
                print("Email sent")
        # Make sure to release resources or handle files here.
    except Exception as e:
        print(f"An error occurred while processing the email: {e}")
    finally:
        print("Thread terminated")


def connect_to_server():
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)
    return mail


def get_unread_emails(mail):
    try:
        mail.select("inbox")

        # Search for unread emails
        status, response = mail.search(None, '(UNSEEN)')
        unread_msg_nums = response[0].split()

        # List to keep track of email IDs that are already being processed
        processed_emails = []

        for e_id in unread_msg_nums:
            if e_id in processed_emails:
                continue
            status, data = mail.fetch(e_id, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    message = email.message_from_bytes(response_part[1])
                    email_subject = email.header.decode_header(message['subject'])[0][0]
                    if isinstance(email_subject, bytes):
                        email_subject = email_subject.decode()
                    if message.is_multipart():
                        for part in message.walk():
                            if part.get_content_type() == "text/plain" and part.get("Content-Disposition") is None:
                                email_body = part.get_payload(decode=True).decode('utf-8')
                                email_from = email.utils.parseaddr(message['From'])[1]
                                thread = Thread(target=process_email, args=(email_subject, email_body, email_from))
                                thread.start()
                                processed_emails.append(e_id)
                                break
    except imaplib.IMAP4.error as e:
        print(f"IMAP4 Error: {e}")
        return False
    except Exception as e:
        print(f"General Error: {e}")
        return False
    return True


# Try to reconnect in case of connection loss
def check_emails():
    mail = connect_to_server()
    attempt_count = 0  # Counter for the number of reconnection attempts

    while True:
        if not get_unread_emails(mail):
            attempt_count += 1  # Increment the attempt counter
            # Calculate the logarithmic wait time and limit to a maximum value
            wait_time = min(math.log2(attempt_count + 1), 300)
            print(f"Attempting to reconnect... Waiting {wait_time} seconds.")
            time.sleep(wait_time)
            mail = connect_to_server()
        else:
            attempt_count = 0  # Reset the counter if the connection was successful
        time.sleep(5)



# Start the process
if __name__ == "__main__":
    check_emails()
