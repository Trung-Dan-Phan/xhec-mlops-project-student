from prefect import flow, task
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

@task(name="Preprocess data")
def preprocess_data(df):
    """
    Preprocess the data by encoding categorical features and splitting the dataset.

    Args:
        df (pd.DataFrame): The input DataFrame containing the dataset.

    Returns:
        tuple: A tuple containing the training and testing data (X_train, X_test, y_train, y_test).
    """
    # Encode binary feature
    label_encoder = LabelEncoder()
    df['Sex_encoded'] = label_encoder.fit_transform(df['Sex'])

    # Independent variables (X) and target variable (y)
    X = df.drop(['Rings', 'Sex'], axis=1)
    y = df['Rings']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, label_encoder
