import pandas as pd
from pathlib import Path
from datetime import datetime

def save_email(email_subject, body, email_from, prediction):
    """
    Saves an email to a CSV file.

    Parameters:
    email_subject (str): The subject of the email.
    body (str): The body of the email.
    email_from (str): The sender of the email.
    prediction (list or numpy.ndarray): The prediction result to be saved.
    """
    csv_file_path = Path('emails.csv')
    try:
        # Convert the prediction to a list if it's a numpy ndarray.
        if not isinstance(prediction, list):
            prediction = prediction.tolist()

        new_email = {
            'from': email_from,
            'subject': email_subject,
            'body': body,
            'prediction': prediction,
            'date': datetime.now().isoformat()
        }

        # Append the new row to the CSV file without loading the entire DataFrame.
        if csv_file_path.is_file():
            pd.DataFrame([new_email]).to_csv(csv_file_path, mode='a', header=False, index=False, encoding='utf-8')
        else:
            pd.DataFrame([new_email]).to_csv(csv_file_path, index=False, encoding='utf-8')
    except Exception as e:
        print(f"Error saving email: {e}")
