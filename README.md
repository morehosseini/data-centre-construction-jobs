# Data-centre construction jobs — supplementary data

Supplementary data and figures for:

> **Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence Review of the Data-Centre Construction Cliff**

**Licence:** all rights reserved. See `LICENSE`.

This repository holds the **corrected evidence register**, quarantine log, supporting tables, figure files, and bibliographic metadata referenced in the manuscript. It does **not** include proprietary search-agent code, prompts, notebooks, or internal discovery run logs.

---

## Contents

```
data-centre-construction-jobs/
├── evidence_tables/     Tables S1–S2 and supporting datasets
├── figures/             Manuscript Figures 1–3 (+ regeneration scripts for Figs 2–3)
├── references/          Verified source metadata (.bib / .ris / .csv)
├── ra_tasks/spotcheck/  Human source spot-check queue and pass/fail log
├── LICENSE
└── CITATION.cff
```

### Supplementary tables (`evidence_tables/`)

| File | Description |
|------|-------------|
| `Table_S1_corrected_evidence_44rows.csv` | **Table S1** — corrected evidence base (44 rows, 20 sources) |
| `Table_S2_quarantine_log.csv` | **Table S2** — quarantine log (10 rows) |
| `corrections_log.csv` | Deduplication / quarantine / reclassification actions |
| `comparative_evidence_primary_table.csv` | Primary comparative evidence table |
| `comparative_evidence_tables.xlsx` | Combined workbook of comparative tables |
| `figure_job_intensity_clean_data.csv` | Figure-oriented intensity dataset |
| `scale_context_table.csv` | Market / capacity scale-context rows |
| `dc_jobs_per_dollar_inputs_and_derivation.csv` | Inputs for jobs-per-dollar descriptors |
| `dc_jobs_per_dollar_summary.json` | Summary of jobs-per-dollar derivation |

Tables S1–S2 are hosted **only** in this repository (not appended to the manuscript PDF).

### Figures (`figures/`)

| Manuscript | Files |
|------------|--------|
| **Figure 1** | `Figure1_evidence_synthesis_procedure.{png,pdf}` |
| **Figure 2** | `Figure2_employment_intensity_v19.*` · `fig2_generate.py` |
| **Figure 3** | `Figure3_employment_cliff_v19.*` · `fig3_generate.py` |

See `figures/README.md` to regenerate Figures 2–3.

### References (`references/`)

Bibliographic metadata for data-centre and comparator sources (`.csv`, `.bib`, `.ris`). Third-party full texts are **not** redistributed.

### Spot-check (`ra_tasks/spotcheck/`)

Human source-level spot-check queue and pass/fail log for the corrected register.

---

## Note on excluded materials

Search-agent implementation details, prompts, orchestration notebooks, and raw discovery-run artefacts are **not published** here. The manuscript describes the high-level evidence-synthesis procedure; the files above support the analysed evidence base and figures only.

This repository does not redistribute copyrighted third-party PDFs. Retrieve sources via the DOIs/URLs in `references/` and the source fields in Tables S1–S2.
