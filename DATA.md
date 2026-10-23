# Local data contract

No research data are bundled. Obtain access from the dataset owner; a publication DOI does not grant redistribution rights. `--data-root` is the root of the corresponding original project, not this repository.

`all_materials/master_thesis_Aruna/master_thesis_Aruna/model_comparison_torino/data/sin.mat`: arrays `VAs`, `thetaMs`, `DTheta_ms`, `IAs`, observed shape (20001,30). Columns are independent simulations. Features are VA, -0.95765*sin(4*thetaM), and DTheta; target is IA.

## Preprocessing and split

The first two thirds of simulations are training data and the remainder are held out. Drop the first time row, fit training-only input and target scalers, and sample length-30 windows within each simulation. No window crosses simulation boundaries.

Missing files produce an actionable error. Dataset schemas were inspected locally; the synthetic demo only checks the code path and is not a substitute for research data.
