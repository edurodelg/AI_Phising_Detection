import yagmail
import os

# Use environment variables for credentials
username = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
yag = yagmail.SMTP(username, password)


def send_email(email_subject, email_from, prediction):
    try:
        # Make sure the prediction is in text format
        prediction_text = ', '.join(prediction) if isinstance(prediction, list) else str(prediction)
        response = f'Your email has been categorized as: {prediction_text}'

        # Path to the attachment
        attachment = 'Data Use and Privacy Information.txt'  # Data Use and Privacy Information

        # Send the response with an attachment
        yag.send(to=email_from, subject="Re: " + email_subject, contents=[response, attachment])
        print("Response with attachment sent to:", email_from)
        return True
    except Exception as e:
        # Here you could add logging to a log file instead of just printing the error
        print(f"Error sending email to {email_from} with attachment: {e}")
        # Consider some additional logic in case of failure (retries, notifications, etc.)
        return False
