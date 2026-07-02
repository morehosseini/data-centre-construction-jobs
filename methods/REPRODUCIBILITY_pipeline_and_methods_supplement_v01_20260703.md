# Reproducibility and Methods Supplement — full evidence pipeline

**Paper:** *The hard hats behind the algorithm: construction-phase job creation by data centres*
**Target journal:** ECAM (Harvard referencing)
**Prepared:** 2026-07-03
**Status:** internal working document — source for updating manuscript §3 and the Data-availability statement in v10

---

## 1. Why this document exists

The task was to confirm that every procedure, model and notebook actually executed in this
project is documented transparently enough for a top-journal reader to audit and re-run the
evidence base. This supplement (a) audits what the current manuscript Methods (§3 of
`manuscript_v09`) already covers, (b) identifies what it omits, (c) supplies ready-to-insert
Methods text, and (d) provides a full notebook → inputs → outputs → run-ID reproducibility
appendix.

**Headline finding of the audit.** The v09 Methods accurately documents the *original*
two-stream deep search, the reference-verification and extraction pipeline, and the
correction/QC pass that produced the corrected 34-row evidence base. It does **not** yet
document two components that were built and executed after v09 was circulated:

1. the **work-package gap-search campaign** — seven Universal Deep Search Agent runs
   (notebooks 00–06) that targeted the specific comparator and jobs-per-dollar gaps set out
   in `DEEP_SEARCH_PLAN_equal_investment_job_comparators_v01_20260630.md`; and
2. the **post-search triage layer** (notebook 07) that scores, de-duplicates and prioritises
   the ~2,000 harvested sources into research-assistant (RA) verification workbooks.

These are currently a **documented source-discovery and triage layer**, not yet integrated
into the corrected evidence table. The Methods should describe them as such — transparently
scoped as leads awaiting primary-source verification — so the paper neither hides the work nor
overclaims it as analysed evidence.

---

## 2. The full pipeline at a glance

The project runs on **two connected pipelines**. Both are re-runnable notebooks; both log
their own inputs and outputs.

```
GAP DIAGNOSIS
  review_context/ + DEEP_SEARCH_PLAN (work packages A–J)
        │
        ▼
PIPELINE 1 — SOURCE DISCOVERY (agentic deep search)  [Gemini, google-genai]
  Original two streams  ....... Deep_Search_*_FRESH.ipynb  (DC + comparator)
  Gap-search campaign  ........ deep_search/vscode_ready/notebooks/00–06
        │  outputs per run: verified_sources.csv, datasets.csv,
        │  FINAL_MERGED_SYNTHESIS.md, QA_REPORT.md, run_manifest/environment,
        │  search_audit.jsonl, final_citation_audit.csv
        ▼
  TRIAGE  ..................... deep_search/vscode_ready/notebooks/07
        │  outputs per run: comparator_source_triage.csv,
        │  comparator_metric_review_template.csv, comparator_RA_review_workbook.xlsx
        ▼
PIPELINE 2 — EVIDENCE CODING & MANUSCRIPT OUTPUTS
  submission_00/notebooks/00–05 .. source recovery, full-text extraction, metric coding,
                                    RA review workbooks (DC + comparator)
  submission_00/notebooks/06 ..... build comparative evidence table
  submission_00/notebooks/08 ..... correction & rebuild (dedupe / quarantine / reclassify)
  submission_00/notebooks/07 ..... prepare manuscript tables & figures
        │
        ▼
  Corrected citable evidence (34 rows / 12 sources) + Figures 1–2 + Tables S1–S2
```

A reader can reproduce the analysed evidence base from Pipeline 2 alone (it is self-contained
from the retrieved source pack). Pipeline 1 documents *how sources were discovered*, which is
the part a methods referee will probe for search reproducibility and bias control.

---

## 3. Audit of current Methods (§3 of manuscript_v09)

| §3 subsection | Covers | Verdict |
|---|---|---|
| 3.1 Design and scope | Facility-attributable scope, phase split, exclusions | Adequate |
| 3.2 Employment boundary & work-location coding | Six-layer boundary framework | Adequate |
| 3.3 Two-stream agentic deep search | Original DC + comparator streams; slice logic; the **manual** ChatGPT/Gemini supplemental prompt (run 03, now superseded) | **Update needed** — describes the superseded manual run, not the agentic WP campaign that replaced it |
| 3.4 Reference verification | Deterministic DOI check vs Crossref/OpenAlex/DataCite/Zenodo; ~591 raw yield | Adequate for Pipeline-2 corpus; **counts need a note** that the WP campaign adds a further ~2,002 verified DOIs at discovery stage |
| 3.5 Full-text extraction & metric mining | 36 docs, 4,545 candidate mentions | Adequate |
| 3.6 Structured review & comparative synthesis | 106 → 52 rows | Adequate |
| 3.7 Evidence correction & QC | Dedupe / quarantine / reclassify → 34 rows | Adequate (this is notebook 08) |
| 3.8 Effect measures & harmonisation | Normalised metrics, evidence tags | Adequate |
| Table 1 pipeline counts | Old-pipeline counts only | **Add a second block** for the WP campaign + triage, clearly labelled "source-discovery / triage stage, not pooled" |
| Data availability & reproducibility | Prompts, logs, notebooks, tables in submission_00/; OSF/Zenodo DOI at submission | **Extend** to list the WP run manifests, audit logs and triage workbooks |

**Bottom line:** no existing claim is wrong, but three places (3.3, Table 1, Data-availability)
must be extended so the WP campaign and triage are on the record. Draft text for each is in §4.

---

## 4. Ready-to-insert Methods text (drop into §3, Australian English, third person)

### 4.1 Replace the "Supplemental gap-search protocol" paragraph in §3.3

> **Supplemental work-package gap search.** After the initial synthesis, a structured
> gap diagnosis (recorded in `DEEP_SEARCH_PLAN_equal_investment_job_comparators`) converted the
> manuscript's remaining weaknesses into ten work packages (A–J), centred on the
> equal-investment question — how a data centre compares with alternative built assets in local
> jobs per dollar of capital invested. Each work package was executed as an independent run of
> the same agentic deep-search pipeline (the Universal Deep Search Agent, hardening version
> `uds_hardened_v3`), using a grounded Gemini retrieval stack (`google-genai`; deep-research
> model `deep-research-preview-04-2026`, follow-up reasoning model `gemini-3.1-pro-preview`).
> Seven runs were completed between 1 and 2 July 2026 (Table X): off-site labour and the
> "10 jobs/MW" rule; data-centre jobs per dollar of capex; warehousing and fulfilment
> comparators; advanced-manufacturing and gigafactory comparators; local-workforce capture,
> incentives and ex-post audits; hospital, school and housing comparators; and a
> renewable-energy and off-site-prefabrication update. Every run decomposed its topic into eight
> evidence slices (evidence landscape, methods and approaches, applications and outcomes,
> quality/governance/risk, grey-literature validation, datasets, protocol refinement, and gap
> analysis), extracted nineteen evidence dimensions per source (including asset class, phase,
> metric value, unit, job scope, denominator, locality, verbatim quote, page or section, quality
> flag and risk-of-bias), applied backward/forward citation snowballing over an OpenAlex citation
> graph, and deterministically verified every DOI-shaped identifier against Crossref, OpenAlex,
> DataCite and Zenodo. All queries, retrieved URLs, interaction identifiers and citation
> decisions were logged (`search_audit.jsonl`, `final_citation_audit.csv`, `run_manifest.json`,
> `run_environment.json`).

### 4.2 Add a "Post-search triage" paragraph after §3.3

> **Post-search triage.** Because snowball expansion deliberately over-collects, each completed
> work-package dossier was passed through a deterministic, no-API triage notebook that pooled its
> verified sources, datasets and final-synthesis evidence rows; de-duplicated them on DOI, then
> URL, then normalised title; and scored each source for relevance using transparent, auditable
> rules (presence in the final synthesis table, citation-audit status, presence of a DOI,
> asset-class keywords, employment/capex/normalisation keywords, authoritative-source hints, and
> penalties for off-topic or citation-audit-invalid records). Sources meeting a relevance
> threshold were promoted into a research-assistant metric-review workbook that carries no
> extracted values — only the fields an assistant must complete after opening the primary source
> (metric, unit, phase, denominator, direct-versus-total job definition, page or table, and a
> verbatim quote). This step converts a large, noisy discovery set into a prioritised
> verification queue and does not itself produce findings.

### 4.3 Add to Table 1 (second block, clearly labelled)

> *Supplemental work-package source-discovery and triage stage (not pooled with the corrected
> evidence base):*
>
> | Pipeline stage | Count |
> |---|---|
> | Work-package agent runs completed | 7 (1–2 July 2026) |
> | DOI-verified records (raw discovery yield) | ~2,002 |
> | Dataset records identified | ~404 |
> | Unique sources after triage de-duplication | ~300–365 per run |
> | Sources promoted to RA verification queue | up to 90 per run (630 review slots) |
> | Status | source-discovery + triage complete; primary-source verification pending |

### 4.4 Extend the Data-availability statement

> **Data availability and reproducibility.** The project preserves, in `submission_00/`, the gap
> diagnosis and work-package plan, every deep-search run's manifest, environment record, search
> audit log, citation audit, verified-source and dataset tables, final merged synthesis and QA
> report (`deep_search/vscode_ready/notebooks/deep_search_outputs/run_*`), the post-search triage
> workbooks (`.../triage_outputs/run_*`), the extraction and coding notebooks, the corrected
> evidence tables, figure datasets, and the correction and spot-check logs. Notebooks carry
> locked run identifiers so that outputs are traceable to a specific dated run. A de-identified
> replication package will be deposited in OSF or Zenodo at submission and its DOI inserted in
> the final version.

---

## 5. Reproducibility appendix — notebook register

### 5.1 Pipeline 1 — source discovery (agentic deep search)

| Order | Notebook | Work package(s) | Run ID | Verified DOIs | Datasets |
|:---:|---|---|---|---:|---:|
| 00 | `00_WP_SUPPLEMENTAL_Ania_Offsite_Comparators_10jobsMW.ipynb` | Off-site labour; 10 jobs/MW; partial B/C/I | run_20260701_071034 | 298 | 63 |
| 01 | `01_WP_A_DC_Jobs_Per_Dollar_Capex.ipynb` | A (DC jobs per $ capex) | run_20260701_143537 | 244 | 58 |
| 02 | `02_WP_B_Warehousing_Fulfilment_Comparators.ipynb` | B | run_20260701_193500 | 303 | 57 |
| 03 | `03_WP_C_Advanced_Manufacturing_Gigafactories.ipynb` | C | run_20260702_065516 | 291 | 54 |
| 04 | `04_WP_GHJ_Localness_Incentives_Realised_Jobs.ipynb` | G, H, J | run_20260702_133630 | 282 | 60 |
| 05 | `05_WP_DE_Social_Infrastructure_Comparators.ipynb` | D, E | run_20260702_171638 | 287 | 54 |
| 06 | `06_WP_FI_Renewable_Energy_and_Offsite_Prefab_Update.ipynb` | F, I | run_20260702_202538 | 297 | 58 |
| — | **Total** | | | **~2,002** | **~404** |

Each run directory contains: `run_manifest.json`, `run_environment.json`, `topic_config.json`,
`search_audit.jsonl`, eight slice markdowns, `FINAL_MERGED_SYNTHESIS.md`, `QA_REPORT.md`,
`verified_sources.csv`, `datasets.csv`, `final_citation_audit.csv`, and a zipped dossier.
Engine/model provenance: `google-genai` 2.5.0; deep-research model `deep-research-preview-04-2026`;
follow-up model `gemini-3.1-pro-preview`; hardening `uds_hardened_v3_2026_06_14`.

### 5.2 Triage (notebook 07) — completed 2026-07-03

| Run (WP) | Unique sources | Promoted to RA | RA review rows | High priority |
|---|---:|---:|---:|---:|
| run_20260701_071034 (00 supplemental) | 363 | 187 | 90 | 59 |
| run_20260701_143537 (01 WP A, DC track) | 301 | 190 | 90 | 88 |
| run_20260701_193500 (02 WP B) | 365 | 195 | 90 | 57 |
| run_20260702_065516 (03 WP C) | 351 | 203 | 90 | 53 |
| run_20260702_133630 (04 WP G+H+J) | 351 | 175 | 90 | 53 |
| run_20260702_171638 (05 WP D+E) | 347 | 194 | 90 | 70 |
| run_20260702_202538 (06 WP F+I) | 359 | 281 | 90 | 108 |

Outputs per run under `deep_search/vscode_ready/notebooks/triage_outputs/run_*/`:
`comparator_source_triage.csv`, `comparator_metric_review_template.csv`,
`comparator_RA_review_workbook.xlsx` (7 sheets: README, source_triage, metric_review_template,
citation_quality_flags, synthesis_evidence_table, verified_sources_raw, datasets_raw).
Cross-run index: `triage_outputs/_triage_summary_all_runs.csv`.
Note: WP A (run 01) is a data-centre benchmark, not a comparator; its triage is provided for
completeness but should feed the DC metric-review track, not the comparator table.

### 5.3 Pipeline 2 — evidence coding & manuscript outputs

| Notebook | Role |
|---|---|
| `submission_00/notebooks/00_source_recovery_and_fulltext_status.ipynb` | DC source recovery / full-text status |
| `01_fulltext_extraction_and_metric_coding.ipynb` | DC full-text extraction, metric coding |
| `02_comparator_source_triage_and_RA_review_workbook.ipynb` | Comparator triage (parent of deep-search NB 07) |
| `03_comparator_source_recovery_and_fulltext_extraction.ipynb` | Comparator source recovery |
| `04_comparator_metric_extraction_and_review_workbook.ipynb` | Comparator metric extraction |
| `05_data_centre_metric_review_and_RA_workbook.ipynb` | DC metric RA review |
| `06_build_comparative_evidence_table.ipynb` | Build comparative evidence table |
| `07_prepare_manuscript_tables_and_figures.ipynb` | Manuscript tables + Figures 1–2 |
| `08_correct_and_rebuild_manuscript_evidence_table.ipynb` | Correction pass → corrected 34-row base (§3.7) |

Regeneration order for the manuscript outputs: **08 → 06 → 07**.

---

## 6. Honest limitations to state in the paper

- The work-package campaign is a **source-discovery and triage layer**. Its ~2,002 verified DOIs
  are a raw yield, not analysed evidence; the verified set knowingly over-collects (e.g. a large
  share of triaged records classify as "unclear/methods-only"). No WP-campaign source enters a
  finding until an assistant verifies the primary document.
- Comparator job-intensity metrics that can be pooled remain scarce; consistent with the v09
  position, non-energy comparators (warehousing, advanced manufacturing) are used narratively and
  are not pooled with the corrected evidence table until verification meets the plan's minimum
  yield bar (≥2 citable sources, compatible units, clear phase and denominator).
- The "10 jobs/MW construction vs 1 job/MW operations" rule was specifically screened and is
  **not** used as a data-centre coefficient; it appears mainly as a policy/tariff threshold.
- LLM-assisted discovery can miss or mis-rank sources; this is mitigated by deterministic DOI
  verification, full logging, and a human verification gate before any figure is cited.

---

## 7. Immediate next actions (verification gate)

1. Assign the RA metric-review workbooks (start with high-priority rows and government/audit/
   method sources) — verify primary source, record metric, unit, phase, denominator, direct-vs-
   total definition, page/table and quote.
2. Feed verified comparator rows into `submission_00/notebooks/06` → rebuild table via `08`,
   regenerate figures via `07`.
3. Apply the yield-bar test before any new comparator class is added to a finding.
4. Update manuscript §3.3, Table 1 and the Data-availability statement using the text in §4.
