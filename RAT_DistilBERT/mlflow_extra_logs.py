import mlflow

run_id = "0194922c05b64dcf9e196aa7d9844224"
with mlflow.start_run(run_id=run_id) as run:
    mlflow.log_param("archi", "RAT")
    mlflow.log_param("emb", "distil")
    mlflow.log_param("lr", 7.4e-06)
    mlflow.log_param("bs", 2)
    # # mlflow.set_tag("GPU", "P4")
    
    mlflow.log_metric("test_accuracy", 0.3191489361702128)