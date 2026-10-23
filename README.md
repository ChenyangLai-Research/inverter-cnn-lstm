# CNN-LSTM for anomaly detection in actuator power inverters

Private working repository for Chenyang Lai's research code. [Associated publication](https://doi.org/10.1109/ICSRS68021.2025.11422055)

This is a **runnable, curated recovery** of selected legacy code. The default experiment is deliberately small and checks data loading, training, held-out prediction and checkpoint saving. It does **not** reproduce the paper's numerical results.

## Method

A PyTorch port of the notebook CNN-LSTM: causal convolutions (64×5, 32×3), stride-one max pooling, 128-unit LSTM, flattening, and dense layers 64→16→1. It reconstructs phase current from voltage and motion-derived inputs.

## Install and run

Tested with Python 3.12 on macOS, CPU. From the repository directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-tested.txt
python run.py --demo --epochs 3 --max-samples 32 --output outputs/demo
```

The synthetic demonstration requires no research dataset. For authorized local research data, point to the original project root described in [DATA.md](DATA.md):

```sh
python run.py --data-root "/absolute/path/to/original/project" --epochs 3 --max-samples 32 --output outputs/real
```

`--epochs`, `--batch-size`, `--lr`, `--seed`, `--max-samples` and `--output` are configurable. Some models have additional fixed caps documented below. Longer training alone does not restore the full published protocol.

The output folder contains metrics/history, predictions and a checkpoint (`model.pt`); preprocessing information is saved separately or inside the joblib bundle. Outputs and all data files are git-ignored. Regression MSE is in normalized coordinates unless the task says otherwise.

To replay held-out inference from a checkpoint (not resume training):

```sh
python run.py --demo --seed 22 --max-samples 32 --checkpoint outputs/demo/model.pt --output outputs/replay
```

Replay requires the sibling `protocol.json`, identical data, data root/mode, seed and sample cap. The pipeline rebuilds its deterministic preprocessing and data split; this is not an arbitrary new-data prediction API. Only load trusted checkpoints.

## Data and execution protocol

The first two thirds of simulations are training data and the remainder are held out. Drop the first time row, fit training-only input and target scalers, and sample length-30 windows within each simulation. No window crosses simulation boundaries.

## Validation

```sh
python -m unittest discover -s tests -v
```

The regression test trains on synthetic data, reloads the checkpoint and checks identical predictions. It also checks that mismatched replay settings and missing local data fail clearly. [VALIDATION.md](VALIDATION.md) records local-data checks without including the underlying data.

## Scope and limitations

This is a TensorFlow-to-PyTorch port, not a conversion of trained weights. The runnable path uses sine simulations and normalized targets. The notebook sawtooth variant is archived; the cumulative Z-score detector and sensor/MOSFET fault experiments are not integrated.

## Repository layout and provenance

- `run.py`: command-line entry point.
- `experiment.py`: data selection, training objective and evaluation protocol.
- `model.py`: extracted model definitions or explicitly documented port.
- `runtime.py`: shared CPU experiment utilities.
- `legacy/`: selected archival source for traceability; notebooks have outputs and execution metadata removed. These old scripts are reference material and may retain machine-specific paths and obsolete dependencies; run `run.py` instead.
- `project.json`: original relative source paths and original SHA-256 hashes. Notebook hashes refer to the original unsanitized source.
- `CHANGELOG.md`: changes and deviations from the archive.

Original folders were left unchanged. No raw data, manuscript, trained research weights or partner documents are distributed. No open-source license has been assigned; see [RIGHTS.md](RIGHTS.md). Keep this repository private until its scope and rights are reviewed.
