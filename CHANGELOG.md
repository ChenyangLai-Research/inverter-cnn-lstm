# Recovery notes — 2026-10-23

Made the CNN-LSTM architecture explicit: the old notebook later overwrote it with a pure LSTM. Removed stored notebook outputs and execution metadata, retained original code cells, and replaced the TensorFlow runtime with PyTorch.

## Shared changes

Added an explicit data root, deterministic CPU seeds, dependency declarations, synthetic demonstration, finite loss/gradient/prediction checks, held-out evaluation, checkpoint replay with protocol checks, and source provenance. Train/test preprocessing is separated. Archival code is not executed at import.

## Deviations and unverified parts

This is a TensorFlow-to-PyTorch port, not a conversion of trained weights. The runnable path uses sine simulations and normalized targets. The notebook sawtooth variant is archived; the cumulative Z-score detector and sensor/MOSFET fault experiments are not integrated.
