import os
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from src.data import load_data

def main():
    # Permite que en CI se use un backend file:// temporal sin levantar el server
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
    if tracking_uri:
        mlflow.set_tracking_uri(tracking_uri)

    with mlflow.start_run(run_name="logreg-mini"):
        # Hiperparámetros mínimos
        params = {"C": 1.0, "penalty": "l2", "solver": "lbfgs", "max_iter": 200}
        for k, v in params.items():
            mlflow.log_param(k, v)

        X_train, X_test, y_train, y_test = load_data()
        model = LogisticRegression(
            C=params["C"],
            penalty=params["penalty"],
            solver=params["solver"],
            max_iter=params["max_iter"],
        ).fit(X_train, y_train)

        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1", f1)

        # Guarda el modelo como artifact (nombre "model")
        # Nota: MLflow >=2.14 depreca "artifact_path" en favor de "name",
        # pero este uso sigue funcionando y mantiene compatibilidad.
        mlflow.sklearn.log_model(model, artifact_path="model")

        # Aseguramos un artifact sencillo para el test (independiente del formato del modelo)
        mlflow.log_text("ok", "marker.txt")

        # Umbral mínimo para “sanity check” del demo
        if acc < 0.7:
            raise SystemExit(f"Accuracy demasiado baja para el demo: {acc:.3f}")

if __name__ == "__main__":
    main()
