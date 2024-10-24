import os
import pandas as pd
from config import DATA_DIRPATH, MODELS_DIRPATH
from prefect import serve
from workflows import batch_predict_workflow, train_model_workflow

df_path = "https://raw.githubusercontent.com/Trung-Dan-Phan/xhec-mlops-project-student/refs/heads/3/use_prefect/data/abalone.csv"


if __name__ == "__main__":
    # Load the training data
    #training_data = pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).head(3000)
    # training_data = pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).head(3000)
    training_data = pd.read_csv(df_path).head(3000)

    # Define the model training deployment
    train_model_deployment = train_model_workflow.to_deployment(
        name="Model training Deployment",
        version="0.1.0",
        tags=["training", "model"],
        cron="0 0 * * 0",  # Run every Sunday at midnight
        parameters={
            #"df": pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).head(3000).to_json(),
            'df_path': df_path,
            "artifacts_filepath": MODELS_DIRPATH,
        },
    )

    # Load the batch prediction data
    # batch_prediction_data = pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).tail(1000)
    batch_prediction_data = pd.read_csv(df_path).tail(1000)

    # Define the batch prediction deployment
    batch_predict_deployment = batch_predict_workflow.to_deployment(
        name="Batch predict Deployment",
        version="0.1.0",
        tags=["inference"],
        interval=600,  # Run every 10 minutes
        parameters={
            #"df": pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).tail(1000).to_json(),
            "batch_df_path": df_path,
            "artifacts_filepath": MODELS_DIRPATH,
        },
    )

    # Serve both deployments
    serve(train_model_deployment, batch_predict_deployment)
