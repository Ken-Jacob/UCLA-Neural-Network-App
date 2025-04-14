import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from logger import get_logger

logger = get_logger(__name__)

def load_and_preprocess_data(filepath):
    try:
        df = pd.read_csv(filepath)

        # Drop unnecessary column
        df.drop(columns=['Serial_No'], inplace=True)

        # Separate features and target
        X = df.drop(columns=['Admit_Chance'])
        y = df['Admit_Chance']

        # Scale the features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42
        )

        logger.info("Data loaded and preprocessed successfully.")
        return X_train, X_test, y_train, y_test, scaler

    except Exception as e:
        logger.error("Error in preprocessing data", exc_info=True)
        raise e
