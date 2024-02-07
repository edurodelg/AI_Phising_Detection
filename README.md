Application Overview:
The application is an AI-powered tool that employs a Random Forest algorithm to detect potential phishing emails. It scrutinizes incoming emails and evaluates their content to assess the likelihood of being a phishing attempt. It is recommended to read all the code comments for a comprehensive understanding of the application's functionalities and operations.

Necessary Libraries:
The tool utilizes the following Python libraries:
imaplib and email: For fetching and parsing emails from the IMAP server.
time and threading: For managing asynchronous operations and processing multiple emails simultaneously.
math and os: For various utility and system operations.
yagmail: For sending email responses.
joblib: For loading the machine learning models.
pandas and numpy: For data manipulation and handling.
scipy: For operations on sparse matrices.


Components and Modules:
main.py: The main script that connects to the email server using IMAP, identifies unread emails, and processes them using multithreading.
Predict.py: This module loads the pre-trained machine learning model and predicts whether an email might be phishing. It contains specialized functions to detect URLs in the email body.
Send.py: It sends an automated response to the email sender with the prediction result, using the yagmail library.
Save.py: It records the emails and their corresponding predictions into a CSV file for future reference and analysis.

Workflow:
The main.py script establishes a connection to the email server and checks for unread emails.
Each new email is processed in a separate thread to ensure efficiency and speed.
Within each thread, the following actions occur:
The Predict.py module assesses the email and provides a phishing prediction.
The Save.py module logs the email and its prediction status.
The Send.py module informs the sender about the AI’s prediction.
In case of a lost connection, the script will attempt to reconnect with increasing timeout intervals.

Initial Setup Instructions:
Install Python and the required libraries.
Place the .py files in a single directory.
Load necessary model files such as tfidf_vectorizer.joblib and random_forest_model.joblib.
Configure the email server credentials in the main.py and Send.py scripts.

Execution:
Run the main.py file to start the email monitoring and processing.

Security Notes:
Passwords and sensitive credentials should not be hardcoded. Use environment variables or secure configuration managers.
Keep the machine learning models and TF-IDF vectors in a secure location, not publicly accessible.

Maintenance and Logging:
Regularly check the emails.csv for insights into the emails processed and the AI’s performance.
Monitor system logs for any errors or performance issues.

Disclaimer:
The application's predictions are based on its training and the data provided. The creator of this application is not responsible for any inaccuracies in the AI’s predictions. Users should use the application's results as one of several tools in determining the legitimacy of an email.

Errors:
Several errors have been identified in the application when the size of the email is small. These errors can affect the accuracy of the predictions and the tool's ability to correctly identify phishing attempts.
