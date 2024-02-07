import joblib
import pandas as pd
import numpy as np
from scipy.sparse import hstack

# These variables are assumed to be global and will be used in the prediction function
tfi = None
random_forest = None

"""
Important:
Importance of 'http' feature: 0.012458165219633695
Importance of 'https' feature: 0.0007734964148284983
Importance mean: 0.00019735366767310755
Importance median: 4.026161872931552e-05
Importance max: 0.022190096184069263
"""


def detect_http(text):
    if pd.isna(text):
        return 0  # If the value is NaN, return 0
    return 1 if 'http://' in text else 0


def detect_https(text):
    if pd.isna(text):
        return 0  # If the value is NaN, return 0
    return 1 if 'https://' in text else 0


def load_models():
    # Make the variables global to modify them
    global tfi
    global random_forest

    # Load the models from the files
    tfi = joblib.load("tfidf_vectorizer.joblib")
    random_forest = joblib.load("random_forest_model.joblib")


def predict(email):
    # Check if the models are loaded
    if tfi is None or random_forest is None:
        load_models()
    http_feature = detect_http(email)
    https_feature = detect_https(email)
    # Transform the email using TfidfVectorizer
    vector_text = tfi.transform([email])  # Make sure to pass the email as a list
    # Combine the TF-IDF vector with the new http and https features
    vector_combined = hstack([vector_text, np.array([[http_feature, https_feature]])])

    # Make the prediction with the RandomForest model
    prediction = random_forest.predict(vector_combined)
    print(prediction)
    return prediction
