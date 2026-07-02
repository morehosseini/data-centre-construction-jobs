# Deep Search Agent Library

Consolidated home for all Universal Deep Search Agent notebooks, aligned with:

`DEEP_SEARCH_PLAN_equal_investment_job_comparators_v01_20260630.md`

## Folder layout

```
deep_search/
├── README.md
├── DEEP_SEARCH_PLAN_...md
├── SUPPLEMENTAL_DEEP_SEARCH_PROMPT_v01_20260629.md   ← original manual prompt (archived)
├── _build_deep_search_notebooks.py
├── _template/
├── already_run/
│   ├── 01_… 02_…  (agent runs)
│   ├── 03_RUN_MANIFEST.json   ← manual pilot (superseded)
│   └── outputs/
└── to_run/
    ├── WP_SUPPLEMENTAL_Ania_Offsite_Comparators_10jobsMW.ipynb   ← replaces run 03
    └── WP_A … WP_FI
```

## VS Code — ready-to-run workspace (recommended)

Open **`vscode_ready/DC_deep_search.code-workspace`** in VS Code. One-time setup (already run if `.venv` exists):

```bash
cd submission_00/deep_search/vscode_ready
./setup_env.sh
```

Includes: `.env` (from prior runs), Python 3.12 `.venv`, Jupyter kernel **DC Deep Search (.venv)**, numbered notebooks `00`–`06` in `notebooks/`.

## Setup before running (manual / to_run path)

1. Create a `.env` file in `deep_search/` or `to_run/` with `GEMINI_API_KEY=...`
2. Open the notebook from `to_run/` so outputs land in `./deep_search_outputs/run_<RUN_ID>/`
3. Run the offline self-test cell, review Cell 0 `TOPIC`, then start the paid pipeline

## Already run

| ID | Notebook / run | Status | Run ID | Outputs |
|:---:|---|---|---|---|
| **01** | `01_Data_Centre_Job_Creation_BROAD.ipynb` | completed | `run_20260620_151510` | `already_run/outputs/run_20260620_151510` |
| **02** | `02_Construction_Asset_Comparators_BROAD.ipynb` | completed | `run_20260622_085057` | `already_run/outputs/run_20260622_085057` |
| **03** | Manual ChatGPT + Gemini (no agent) | **superseded** | `manual_20260629` | `methods/deep-research-report.md`, `Data Centre Employment Metrics Research.md` |

Run **03** produced useful leads but is not methods-defensible (no logged agent pipeline). **Superseded by** `WP_SUPPLEMENTAL_…` run `run_20260701_071034` (see completed table below).

## Completed — vscode_ready notebooks 00–06 (2026-07-01 to 2026-07-02)

All runs finished with **8/8 slices**, `FINAL_MERGED_SYNTHESIS.md`, `QA_REPORT.md`, and zipped dossiers. Index: `vscode_ready/run_results_index.json`.

| Order | Notebook | WP | Run ID | Verified DOIs | Datasets |
|:---:|---|:---:|:---:|---:|---:|
| **00** | `00_WP_SUPPLEMENTAL_Ania_Offsite_Comparators_10jobsMW.ipynb` | SUPPLEMENTAL | `run_20260701_071034` | 298 | 63 |
| **01** | `01_WP_A_DC_Jobs_Per_Dollar_Capex.ipynb` | A | `run_20260701_143537` | 244 | 58 |
| **02** | `02_WP_B_Warehousing_Fulfilment_Comparators.ipynb` | B | `run_20260701_193500` | 303 | 57 |
| **03** | `03_WP_C_Advanced_Manufacturing_Gigafactories.ipynb` | C | `run_20260702_065516` | 291 | 54 |
| **04** | `04_WP_GHJ_Localness_Incentives_Realised_Jobs.ipynb` | G+H+J | `run_20260702_133630` | 282 | 60 |
| **05** | `05_WP_DE_Social_Infrastructure_Comparators.ipynb` | D+E | `run_20260702_171638` | 287 | 54 |
| **06** | `06_WP_FI_Renewable_Energy_and_Offsite_Prefab_Update.ipynb` | F+I | `run_20260702_202538` | 297 | 58 |

Outputs live under `vscode_ready/notebooks/deep_search_outputs/run_<RUN_ID>/`. Notebooks have `RUN_ID` locked — re-run **Quality Checks & Export** only unless starting a new paid search.

Discarded partial runs (audit trail): `vscode_ready/notebooks/_discarded_partial_runs/`.

## Post-search triage (notebook 07)

After deep-search runs complete, open **`vscode_ready/notebooks/07_postsearch_comparator_triage_and_RA_workbook.ipynb`**. Set `RUN_TAG` to a completed `run_*` folder (see `run_results_index.json`), run all cells. Outputs land in `vscode_ready/notebooks/triage_outputs/<RUN_TAG>/`.

Preflight (no API): `cd vscode_ready && .venv/bin/python verify_notebook07_env.py`

**Status — COMPLETED 2026-07-03.** Notebook 07 has been run for all 7 runs (00–06). Outputs are in
`vscode_ready/notebooks/triage_outputs/run_*/`, with a cross-run roll-up at
`triage_outputs/_triage_summary_all_runs.csv`. Each run yields up to 90 RA review slots
(`comparator_metric_review_template.csv` / `comparator_RA_review_workbook.xlsx`). WP A (run
`run_20260701_143537`) is a data-centre benchmark and should feed the DC metric-review track, not
the comparator table. **Next step: RA primary-source verification before any figure is cited.**
Full pipeline register and ready-to-insert Methods text:
`../methods/REPRODUCIBILITY_pipeline_and_methods_supplement_v01_20260703.md`.

## Methods traceability

Each agent run produces under `deep_search_outputs/run_<RUN_ID>/`:

- `run_manifest.json`, `run_environment.json`, `search_audit.jsonl`
- `topic_config.json`, slice markdowns, `FINAL_MERGED_SYNTHESIS.md`, `QA_REPORT.md`
- `verified_sources.csv`, `datasets.csv`

Use these — not the markdown summaries alone — when writing the manuscript methods sentence on supplemental source discovery.

## Regenerating notebooks

```bash
cd submission_00/deep_search
python3 _build_deep_search_notebooks.py
```

## After a run

1. Compare new `FINAL_MERGED_SYNTHESIS.md` to pilot files in `methods/` if replacing run 03
2. Triage with `submission_00/notebooks/02_comparator_source_triage_and_RA_review_workbook.ipynb`
3. Verify primary PDFs before coding into the evidence table
4. Update `*_MANIFEST.json` to `completed` with `run_id`