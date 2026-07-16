# Figures — aligned with manuscript v24 (2026-07-16)

Submission figure set for:

> *Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence Review of the Data-Centre Construction Cliff*

| Manuscript | File(s) | Role |
|---|---|---|
| **Figure 1** | `Figure1_evidence_synthesis_procedure.{png,pdf}` | Evidence-synthesis procedure flowchart |
| **Figure 2** | `Figure2_employment_intensity_v19.{pdf,svg,png,tiff}` | Employment intensity per MW by evidence family (source-native units; not pooled) |
| **Figure 3** | `Figure3_employment_cliff_v19.{pdf,svg,png,tiff}` | The data-centre employment cliff: per-MW and scope-marked per-dollar descriptors |

Binary files for Figures 2–3 (TIFF) and Figure 1 (PNG) match the media embedded in `manuscript_v24_20260716.docx`.

## Generation scripts (Figures 2–3)

```bash
cd figures
python3 fig2_generate.py
python3 fig3_generate.py
```

Requires Python 3 and `matplotlib` (and standard library only for these scripts). Data values are hard-coded from manuscript Table 2 / sections 4.4 and 5 — not read from the older multi-panel `evidence_tables/figure_job_intensity_clean_data.csv` (that CSV supports the superseded 2026-07-03 multi-panel design).

## Superseded files

`_superseded_20260703/` holds the pre-renumbering PNGs that were previously published as repo “Figures 1–2” (employment intensity / employment cliff under the old numbering). They are retained for audit only and are **not** the submission figures.

## Note on notebook pipeline

Notebooks `06 → 07 → 08` still produce table/figure *datasets* and an earlier figure pipeline. For the **submission** Figures 2–3, the scripts in this folder are the source of record.
