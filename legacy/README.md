# Archival source files

These files document the original research implementation. They are not installed or executed by `run.py`.
They may execute training or filesystem writes on import. Do not import them as a library.

The curated Python entry point is `../run.py`; its dependencies are specified at the repository root.
The archive was syntax-checked, but its original experiments were not executed in this audit.

The notebooks depend on the original TensorFlow/Colab environment and external MAT files. Outputs and execution metadata have been removed. Notebook cells were checked for syntax, not executed.

Original source hashes and relative locations are recorded in `../project.json`. Original hashes remain provenance records. `archived_sha256` records each reviewed copy; `audit_edits` identifies safety changes. Original research folders were not changed.
