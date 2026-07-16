# Data-centre construction-phase job creation — evidence and reproducibility repository

Replication and reproducibility materials for the study:

> **Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence Review of the Data-Centre Construction Cliff**

Corresponding author: **Dr M. Reza Hosseini**, Faculty of Architecture, Building and Planning,
The University of Melbourne (`mreza.hosseini@unimelb.edu.au`). Co-authors to be confirmed at
submission. Target journal: *Engineering, Construction and Architectural Management* (ECAM).

**Licence:** all rights reserved for pre-submission review. See `LICENSE`.

**Status:** manuscript submission package (aligned with manuscript v24, 2026-07-16). The work-package
deep-search campaign and triage are a documented *source-discovery and triage layer*. The analysed
evidence base is a human-corrected register of **44 rows from 20 sources** (Table S1), including
data-centre and comparator metrics; source-level spot-checking is complete for **34/44 rows (77%)**,
with residual independent PDF confirmation pending for the July additions as labelled in the
spot-check queue. See `methods/` for the full pipeline description and honest limitations.

**Supplementary tables.** `evidence_tables/Table_S1_corrected_evidence_44rows.csv` and
`evidence_tables/Table_S2_quarantine_log.csv` are Tables S1 and S2 referenced in the manuscript.
They are supplementary data files hosted only in this repository — they are **not** reproduced or
appended in the manuscript PDF itself.

---

## What this repository contains

This repository documents, end to end, how the study's employment evidence was discovered,
verified, coded, corrected and normalised — so a reader can audit and re-run the workflow. It
deliberately favours transparency over volume: the analysed evidence base is small and
hand-checked, and every automated step logs its own inputs and outputs.

```
data-centre-construction-jobs/
├── methods/                Reproducibility supplement, gap-search plan, search protocol,
│                           deep-search agent README, development log
├── notebooks/
│   ├── evidence_pipeline/  Source recovery → extraction → coding → correction → tables/figures
│   │                       (submission pipeline; regeneration order 06 → 07 → 08)
│   └── deep_search/        Post-search triage (notebook 07 — deterministic, no API key)
├── deep_search_runs/       Curated key artifacts for each of the 7 completed agent runs
│                           (manifest, environment, topic config, synthesis, QA, verified
│                            sources, datasets, citation audit, search audit log)
├── ra_tasks/               Research-assistant verification workbooks (triage output per run)
│                           + co-author spot-check queue
├── evidence_tables/        Corrected 44-row evidence base (Table S1), quarantine log (Table S2),
│                           corrections log, comparative tables, figure datasets, scale-context
│                           table, and the jobs-per-dollar derivation inputs
├── figures/                Manuscript Figures 1–3 (PNG/PDF; Fig 2–3 also SVG/TIFF) + generation
│                           scripts for Figs 2–3; superseded 2026-07-03 PNGs archived under
│                           figures/_superseded_20260703/
├── references/             Verified source metadata (.bib / .ris / .csv)
├── requirements.txt        Python dependencies for notebook reruns
├── CITATION.cff            Repository citation metadata
└── LICENSE                 Pre-submission all-rights-reserved notice
```

**A note on what is *not* here.** The work-package agent notebooks that actually run the "Universal
Deep Search Agent" against a paid Gemini API (the seven `WP_*.ipynb` gap-search notebooks and the
two original `Deep_Search_*_FRESH.ipynb` broad-search notebooks) are **not published** in this
repository. They are internal orchestration code, are not meaningfully re-runnable by a reader
without the authors' API credentials and account-scoped run IDs, and are not needed to reproduce
the analysed evidence base. Their outputs are fully preserved instead: every run's manifest,
environment, topic configuration, synthesis, QA report, verified-source list, dataset inventory
and search-audit log are curated in `deep_search_runs/`, and the deterministic post-search triage
that turns those artifacts into the RA review workbooks (notebook 07) *is* published, since it
makes no API calls. See `methods/deep_search_agent_README.md` for what the agent notebooks did.

## Manuscript figure map (v24)

| Manuscript | Repository files | Caption (short) |
|---|---|---|
| **Figure 1** | `figures/Figure1_evidence_synthesis_procedure.{png,pdf}` | Evidence-synthesis procedure |
| **Figure 2** | `figures/Figure2_employment_intensity_v19.*` + `fig2_generate.py` | Employment intensity per MW by evidence family |
| **Figure 3** | `figures/Figure3_employment_cliff_v19.*` + `fig3_generate.py` | Employment cliff (per-MW and per-dollar descriptors) |

See `figures/README.md` for regeneration instructions and the note on superseded 2026-07-03 files.

## The two pipelines

**Pipeline 1 — source discovery (agentic deep search).** A custom "Universal Deep Search Agent"
(hardening `uds_hardened_v3`) built on a grounded Gemini retrieval stack (`google-genai`;
deep-research model `deep-research-preview-04-2026`, follow-up model `gemini-3.1-pro-preview`).
After an initial two-stream search, a structured gap diagnosis
(`methods/DEEP_SEARCH_PLAN_...md`) was converted into ten work packages (A–J) and executed as
seven runs (1–2 July 2026). Each run decomposes its topic into eight evidence slices, extracts
nineteen evidence dimensions per source, applies backward/forward citation snowballing, and
deterministically verifies every DOI against Crossref, OpenAlex, DataCite and Zenodo. Raw
discovery yield ≈ 2,002 verified DOIs and ≈ 404 datasets (a deliberately over-collected set, not
analysed evidence). The agent notebooks themselves are not published — see above.

**Triage (notebook 07).** A deterministic, no-API step pools each run's verified sources,
datasets and synthesis rows; de-duplicates on DOI → URL → title; scores relevance with
transparent rules; and emits a research-assistant metric-review workbook (`ra_tasks/`). Nothing
becomes a finding until an assistant opens the primary source and records the metric, unit,
phase, denominator, direct-vs-total definition, page/table and a verbatim quote.

**Pipeline 2 — evidence coding and manuscript outputs.** Full-text extraction, metric mining,
structured review, and an explicit correction pass (dedupe / quarantine / reclassify) yielding a
corrected, citable base of **44 rows from 20 sources** (Table S1), a 10-row quarantine log
(Table S2), normalised effect measures, and manuscript **Figures 1–3**. Table/dataset regeneration
order: `06 → 07 → 08` (06 builds the master evidence table from reviewed inputs, 07 turns it into
manuscript table/figure files, 08 applies the corrections register in place). **Submission
Figures 2–3** are regenerated with `figures/fig2_generate.py` and `figures/fig3_generate.py`
(values from manuscript Table 2 / sections 4.4 and 5).

Full detail, exact counts and ready-to-cite methods text:
`methods/REPRODUCIBILITY_pipeline_and_methods_supplement_v01_20260703.md`
(see the alignment banner at the top of that file for manuscript v24 figure numbering and counts).

## Reproducing

Deep-search runs require a paid Gemini API key and are locked to dated run IDs; they are not
re-run to reproduce results, and the notebooks that ran them are not published here (see above).
The analysed evidence base is reproducible from Pipeline 2, which is self-contained from the
retrieved source pack. The triage step (notebook 07) is fully reproducible offline from the
artifacts in `deep_search_runs/`. Submission Figures 2–3:

```bash
pip install -r requirements.txt
cd figures
python3 fig2_generate.py
python3 fig3_generate.py
```

## Data and copyright note

This repository contains the project's own generated outputs and **bibliographic metadata**
(titles, DOIs, URLs) about third-party sources. It does **not** redistribute third-party
copyrighted PDFs, and it excludes the unsubmitted manuscript draft, API keys, environment files,
and the agentic deep-search notebooks (see above). Sources can be retrieved by readers from the
DOIs/URLs in `references/` and `deep_search_runs/*/verified_sources.csv`.

## Citation

Hosseini, M. R., et al. (2026). *Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence
Review of the Data-Centre Construction Cliff.* Manuscript in preparation. Repository DOI to be
minted at submission. See `CITATION.cff` for repository citation metadata.
