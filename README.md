![CI](https://github.com/mariano-tp/mlflow-mini-experiments/actions/workflows/ci.yml/badge.svg?branch=main&style=flat-square)
![Last commit](https://img.shields.io/github/last-commit/mariano-tp/mlflow-mini-experiments?style=flat-square)
![Release](https://img.shields.io/github/v/release/mariano-tp/mlflow-mini-experiments?style=flat-square)
![License](https://img.shields.io/github/license/mariano-tp/mlflow-mini-experiments?style=flat-square)
![Stars](https://img.shields.io/github/stars/mariano-tp/mlflow-mini-experiments?style=flat-square)


# MLflow Mini Experiments

Demostración mínima de MLOps con MLflow: entrenamiento reproducible, logging de parámetros/métricas/artefactos y UI local vía Docker Compose. Pensado para complementar un pipeline simple sin requerir cloud.

## Qué incluye
- MLflow Tracking Server (local) con backend en SQLite y artifacts en filesystem.
- Script `train.py` (scikit-learn) que loguea params, métricas y el modelo.
- Tests básicos que validan que el run registró métricas esperadas.
- GitHub Actions que ejecuta entrenamiento y tests en cada PR/commit a `main`.

## Uso local (opcional)
1) `docker compose up -d`
2) `export MLFLOW_TRACKING_URI=http://127.0.0.1:5000`
3) `python -m pip install -r requirements.txt`
4) `python -m src.train`
5) UI: http://127.0.0.1:5000

## CI
El workflow ejecuta:
- Instalación de dependencias
- Entrenamiento (con MLflow apuntando a un file backend temporal)
- Tests (validan logging de métricas y artefactos)

## Relación con otros repos
- Complementa un pipeline “mini” (artefactos y métricas en archivos) al mostrar tracking de experimentos y UI.
