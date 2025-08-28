import os
import shutil
import tempfile
from mlflow.tracking import MlflowClient
from src import train

def test_run_logs_metrics_and_artifacts():
    tmpdir = tempfile.mkdtemp()
    try:
        os.environ["MLFLOW_TRACKING_URI"] = f"file://{tmpdir}/mlruns"

        # Ejecuta el entrenamiento (crea experimento/run y artifacts bajo tmpdir/mlruns)
        train.main()

        client = MlflowClient()

        # Obtenemos el run más reciente de cualquier experimento
        experiments = client.search_experiments()
        assert experiments, "No se encontraron experimentos"
        exp_ids = [e.experiment_id for e in experiments]

        runs = client.search_runs(exp_ids, order_by=["attributes.start_time DESC"], max_results=1)
        assert runs, "No se encontraron runs"
        run_id = runs[0].info.run_id

        # Métricas mínimas
        assert client.get_metric_history(run_id, "accuracy"), "No se registró 'accuracy'"

        # Artifacts en la raíz del run
        root = {a.path for a in client.list_artifacts(run_id)}
        # Aceptamos modelo o marcador simple
        assert ("model" in root) or ("marker.txt" in root), "No se encontraron artifacts en la raíz"

        # Si existe la carpeta model, verificamos que tenga contenido
        if "model" in root:
            assert client.list_artifacts(run_id, path="model"), "La carpeta 'model' está vacía"
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
