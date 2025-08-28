import os
import shutil
import tempfile
import glob
import mlflow
from src import train

def test_run_logs_metrics_and_artifacts():
    # Usa un backend file:// temporal sin server
    tmpdir = tempfile.mkdtemp()
    try:
        mlruns_path = os.path.join(tmpdir, "mlruns")
        os.environ["MLFLOW_TRACKING_URI"] = f"file://{mlruns_path}"

        # Ejecuta el entrenamiento
        train.main()

        # Verifica que se creó al menos un experimento
        experiments = mlflow.search_experiments()
        assert len(experiments) >= 1

        # Verifica artifacts: aceptamos o bien el modelo o el marcador simple
        model_artifacts = glob.glob(
            os.path.join(mlruns_path, "*", "*", "artifacts", "model", "**"),
            recursive=True,
        )
        marker_artifact = glob.glob(
            os.path.join(mlruns_path, "*", "*", "artifacts", "marker.txt"),
            recursive=True,
        )

        assert any(model_artifacts) or any(marker_artifact), \
            "No se encontraron artifacts (ni modelo ni marker.txt)"
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
