> Available languages / Idiomas disponibles: [*English*](README.md) / [*Español*](README.ES.md)

Volver al repositorio: [Home](https://github.com/metorresponce/metorresponce/blob/main/README.ES.md)  

[![ci](https://img.shields.io/github/actions/workflow/status/metorresponce/mlflow-mini-experiments/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/metorresponce/mlflow-mini-experiments/actions/workflows/ci.yml)
[![last commit](https://img.shields.io/github/last-commit/metorresponce/mlflow-mini-experiments?style=flat-square)](https://github.com/metorresponce/mlflow-mini-experiments/commits/main)
[![release](https://img.shields.io/github/v/release/metorresponce/mlflow-mini-experiments?display_name=tag&style=flat-square)](https://github.com/metorresponce/mlflow-mini-experiments/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/metorresponce/mlflow-mini-experiments?style=flat-square)](https://github.com/metorresponce/mlflow-mini-experiments/stargazers)

# MLflow Mini Experiments

Demo mínima de MLOps usando MLflow para tracking de experimentos: entrenamiento reproducible, registro de parámetros/métricas/artefactos y una UI local opcional con Docker Compose.

Está pensada para complementar una pipeline simple, sin necesidad de usar servicios cloud.

## Qué hace
- Ejecuta un script de entrenamiento con scikit-learn y registra experimentos en MLflow
- Guarda parámetros, métricas y artefactos del modelo para tener trazabilidad
- Ofrece una UI local de MLflow Tracking (opcional) usando Docker Compose
- Valida el run en CI mediante GitHub Actions

## Qué incluye
- MLflow Tracking Server (local) con backend SQLite y artefactos en filesystem
- src/train.py (scikit-learn) que registra parámetros, métricas y el modelo
- Tests básicos que validan que el run registró las métricas esperadas
- Workflow en GitHub Actions que ejecuta entrenamiento y tests en cada push/PR a main

## Validación 100% online (GitHub Actions)
No hace falta ejecutar nada en local para evaluar este repo.

1. Subí este repo a GitHub
2. Entrá a Actions -> tests (ci.yml) -> Run workflow
3. El workflow debería quedar en verde

Evidencia: logs del workflow en Actions.

## Uso local (opcional)
La ejecución local es opcional y sirve principalmente para desarrollo y troubleshooting.

1. docker compose up -d
2. export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
3. python -m pip install -r requirements.txt
4. python -m src.train
5. Abrí la UI: http://127.0.0.1:5000

## CI (GitHub Actions)
El workflow ejecuta:
- Instalación de dependencias
- Entrenamiento (con MLflow apuntando a un backend local temporal)
- Tests (validan el registro de métricas y artefactos)

## Relación con otros repos
Este repo complementa la ML mini pipeline (artefactos y métricas guardados como archivos) sumando tracking de experimentos y una UI.

## Créditos
Repositorio de portfolio por @metorresponce.

Ver también: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
