# Data-centre construction-phase job creation — evidence and reproducibility repository

Replication and reproducibility materials for the study *The hard hats behind the algorithm:
construction-phase job creation by data centres — a structured evidence synthesis with
implications for Australia's build-out.*

Corresponding author: **Dr M. Reza Hosseini**, Faculty of Architecture, Building and Planning,
The University of Melbourne (`mreza.hosseini@unimelb.edu.au`). Co-authors to be confirmed at
submission. Target journal: *Engineering, Construction and Architectural Management* (ECAM).

**Licence:** all rights reserved for pre-submission review. See `LICENSE`.

**Status:** pre-submission. The work-package deep-search campaign and triage are a documented
*source-discovery and triage layer*; comparator sources await research-assistant primary-source
verification before entering the analysed evidence base. See `methods/` for the full pipeline
description and honest limitations.

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
│   │                       (submission pipeline; regeneration order 08 → 06 → 07)
│   └── deep_search/         Work-package gap-search agents 00–06 + post-search triage 07
├── deep_search_runs/       Curated key artifacts for each of the 7 completed agent runs
│                           (manifest, environment, topic config, synthesis, QA, verified
│                            sources, datasets, citation audit, search audit log)
├── ra_tasks/               Research-assistant verification workbooks (triage output per run)
│                           + co-author spot-check queue
├── evidence_tables/        Corrected 34-row evidence base, quarantine log, corrections log,
│                           comparative tables, figure datasets, scale-context table
├── figures/                Figures 1–2 (PNG)
├── references/             Verified source metadata (.bib / .ris / .csv)
├── requirements.txt        Python dependencies for notebook reruns
├── CITATION.cff            Repository citation metadata
└── LICENSE                 Pre-submission all-rights-reserved notice
```

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
analysed evidence).

**Triage (notebook 07).** A deterministic, no-API step pools each run's verified sources,
datasets and synthesis rows; de-duplicates on DOI → URL → title; scores relevance with
transparent rules; and emits a research-assistant metric-review workbook (`ra_tasks/`). Nothing
becomes a finding until an assistant opens the primary source and records the metric, unit,
phase, denominator, direct-vs-total definition, page/table and a verbatim quote.

**Pipeline 2 — evidence coding and manuscript outputs.** Full-text extraction, metric mining,
structured review, and an explicit correction pass (dedupe / quarantine / reclassify) yielding a
corrected, citable base of 34 rows from 12 sources, then normalised effect measures and Figures
1–2. Regeneration order: `08 → 06 → 07`.

Full detail, exact counts and ready-to-cite methods text:
`methods/REPRODUCIBILITY_pipeline_and_methods_supplement_v01_20260703.md`.

## Reproducing

Deep-search runs require a paid Gemini API key and are locked to dated run IDs; they are not
re-run to reproduce results. The analysed evidence base is reproducible from Pipeline 2, which is
self-contained from the retrieved source pack. The triage step (notebook 07) is fully
reproducible offline from the artifacts in `deep_search_runs/`.

Install the notebook dependencies with:

```bash
pip install -r requirements.txt
```

## Data and copyright note

This repository contains the project's own generated outputs and **bibliographic metadata**
(titles, DOIs, URLs) about third-party sources. It does **not** redistribute third-party
copyrighted PDFs, and it excludes the unsubmitted manuscript draft, API keys and environment
files. Sources can be retrieved by readers from the DOIs/URLs in `references/` and
`deep_search_runs/*/verified_sources.csv`.

## Citation

Hosseini, M. R., et al. (2026). *The hard hats behind the algorithm: construction-phase job
creation by data centres.* Manuscript in preparation. Repository DOI to be minted at submission.
See `CITATION.cff` for repository citation metadata.
