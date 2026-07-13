# Repository Notes

This is a pre-submission reproducibility package. It intentionally excludes:

- unsubmitted manuscript drafts;
- third-party PDFs and full-text source files;
- API keys, `.env` files, local environments, and local run folders;
- superseded archive material and notebook backups;
- the agentic deep-search notebooks that call the paid Gemini API (the work-package
  `WP_*.ipynb` notebooks and the two original `Deep_Search_*_FRESH.ipynb` notebooks) — these
  are internal orchestration code, not needed to reproduce the analysed evidence base. Their
  full outputs are preserved instead in `deep_search_runs/`, and the deterministic (no-API)
  post-search triage notebook is published.

Notebook outputs have been cleared before publication to remove local machine
paths and environment traces. The preserved run artifacts under
`deep_search_runs/` are the auditable record of the completed discovery runs.

The current licence is all rights reserved. Replace `LICENSE` and update
`CITATION.cff` if a permissive licence or repository DOI is added later.
