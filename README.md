> Available languages / Idiomas disponibles: [*English*](README.md) / [*Español*](README.ES.md)

Back to repository: [Home](https://github.com/mariano-tp/mariano-tp/blob/main/README.md)

[![ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/mlflow-mini-experiments/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/actions/workflows/ci.yml)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/mlflow-mini-experiments?style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/commits/main)
[![release](https://img.shields.io/github/v/release/mariano-tp/mlflow-mini-experiments?display_name=tag&style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/mariano-tp/mlflow-mini-experiments?style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/stargazers)

# MLflow Mini Experiments

Minimal MLOps demo using MLflow for experiment tracking: reproducible training, logging of parameters/metrics/artifacts, and an optional local UI via Docker Compose.

Designed to complement a simple pipeline without requiring any cloud services.

## What it does
- Runs a scikit-learn training script and logs experiments to MLflow
- Records parameters, metrics, and model artifacts for traceability
- Provides a local MLflow Tracking UI (optional) using Docker Compose
- Validates the run in CI via GitHub Actions

## What’s included
- MLflow Tracking Server (local) with SQLite backend and filesystem artifacts
- src/train.py training script (scikit-learn) that logs params, metrics, and the model
- Basic tests validating that the run recorded the expected metrics
- GitHub Actions workflow that runs training and tests on each push/PR to main

## Validate 100% online (GitHub Actions)
No local setup is required to evaluate this repo.

1. Push this repo to GitHub
2. Go to Actions -> tests (ci.yml) -> Run workflow
3. The workflow should turn green

Evidence: workflow logs in Actions.

## Local usage (optional)
Local execution is optional and mainly useful for development and troubleshooting.

1. docker compose up -d
2. export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
3. python -m pip install -r requirements.txt
4. python -m src.train
5. Open the UI: http://127.0.0.1:5000

## CI (GitHub Actions)
The workflow runs:
- Dependency installation
- Training (with MLflow pointing to a temporary local backend)
- Tests (validate logging of metrics and artifacts)

## Relation to other repos
This repo complements the ML mini pipeline (artifacts and metrics stored as files) by adding experiment tracking and a UI.

## Credits
Portfolio repository by @mariano-tp.

See also: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
