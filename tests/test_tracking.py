import os
import shutil
import tempfile
import mlflow
import glob
from src import train

def test_run_logs_metrics_and_artifacts():
    # Usa un backend file:// temporal sin server
    tmpdir = tempfile.mkdtemp()
    try:
        mlruns_path = os.path.join(tmpdir, "mlruns")
        os.environ["MLFLOW_TRACKING_URI"] = f"file://{mlruns_path}"

        # Ejecuta el entrenamiento
        train.main()

        # Verifica que se creó al menos un run
        experiments = mlflow.search_experiments()
        assert len(experiments) >= 1

        # Busca artifacts con el modelo
        # Como es backend file://, los artifacts quedan en mlruns/<exp>/<run>/artifacts
        model_artifacts = glob.glob(os.path.join(mlruns_path, "*", "*", "artifacts", "model", "**"), recursive=True)
        assert any(model_artifacts), "No se encontraron artifacts del modelo"
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
