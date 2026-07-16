# Repository Notes

This is a pre-submission / submission-aligned reproducibility package. It intentionally excludes:

- unsubmitted manuscript drafts;
- third-party PDFs and full-text source files;
- API keys, `.env` files, local environments, and local run folders;
- superseded archive material and notebook backups (except figures archived under
  `figures/_superseded_20260703/` for audit);
- the agentic deep-search notebooks that call the paid Gemini API (the work-package
  `WP_*.ipynb` notebooks and the two original `Deep_Search_*_FRESH.ipynb` notebooks) — these
  are internal orchestration code, not needed to reproduce the analysed evidence base. Their
  full outputs are preserved instead in `deep_search_runs/`, and the deterministic (no-API)
  post-search triage notebook is published.

Notebook outputs have been cleared before publication to remove local machine
paths and environment traces. The preserved run artifacts under
`deep_search_runs/` are the auditable record of the completed discovery runs.

## Alignment with manuscript v24 (2026-07-16)

| Item | Status |
|---|---|
| Title | *Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence Review of the Data-Centre Construction Cliff* |
| Evidence base | 44 corrected rows / 20 sources (Table S1); 10-row quarantine (Table S2) |
| Spot-check | 34/44 rows (77%) complete in `ra_tasks/spotcheck/` |
| Figure 1 | Procedure flowchart (`figures/Figure1_evidence_synthesis_procedure.*`) |
| Figures 2–3 | v19 submission set + `fig2_generate.py` / `fig3_generate.py` |
| Superseded figures | Old 2026-07-03 intensity/cliff PNGs under `figures/_superseded_20260703/` |

The current licence is all rights reserved. Replace `LICENSE` and update
`CITATION.cff` if a permissive licence or repository DOI is added later.
