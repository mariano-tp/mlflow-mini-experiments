[![ci](https://img.shields.io/github/actions/workflow/status/mariano-tp/mlflow-mini-experiments/ci.yml?branch=main&label=tests&style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/actions/workflows/ci.yml)
[![last commit](https://img.shields.io/github/last-commit/mariano-tp/mlflow-mini-experiments?style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/commits/main)
[![release](https://img.shields.io/github/v/release/mariano-tp/mlflow-mini-experiments?display_name=tag&style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/releases)
[![license: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![stars](https://img.shields.io/github/stars/mariano-tp/mlflow-mini-experiments?style=flat-square)](https://github.com/mariano-tp/mlflow-mini-experiments/stargazers)


# MLflow Mini Experiments

Minimal MLOps demo with MLflow: reproducible training, logging of parameters/metrics/artifacts, and local UI via Docker Compose. Designed to complement a simple pipeline without requiring cloud.

## What’s included
- MLflow Tracking Server (local) with SQLite backend and filesystem artifacts.
- `train.py` script (scikit-learn) that logs params, metrics, and the model.
- Basic tests validating that the run recorded expected metrics.
- GitHub Actions workflow that runs training and tests on each PR/commit to `main`.

## Local usage (optional)
1) `docker compose up -d`
2) `export MLFLOW_TRACKING_URI=http://127.0.0.1:5000`
3) `python -m pip install -r requirements.txt`
4) `python -m src.train`
5) UI: http://127.0.0.1:5000

## CI
The workflow runs:
- Dependency installation
- Training (with MLflow pointing to a temporary file backend)
- Tests (validate logging of metrics and artifacts)

## Relation to other repos
- Complements the “mini” pipeline (artifacts and metrics stored as files) by adding experiment tracking and a UI.

## Credits

Portfolio repository by **@mariano-tp**.

See also: [Code of Conduct](./CODE_OF_CONDUCT.md) · [Contributing](./CONTRIBUTING.md) · [Security](./SECURITY.md)
