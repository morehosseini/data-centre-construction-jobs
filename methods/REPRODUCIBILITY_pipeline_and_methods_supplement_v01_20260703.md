# Reproducibility and Methods Supplement — full evidence pipeline

**Paper (current):** *Megawatts, but Few Permanent Jobs? An Agent-Assisted Evidence Review of the Data-Centre Construction Cliff*
**Target journal:** ECAM (Harvard referencing)
**Prepared:** 2026-07-03
**Last alignment pass:** 2026-07-17 (manuscript v24 / repository figure set v19)

---

> **Alignment banner (read first).** Historical sections below retain the original 2026-07-03
> audit narrative (including references to intermediate manuscript versions and the pre-integration
> 34-row base). **Authoritative submission numbers and figure map** are:
>
> | Item | Submission value |
> |---|---|
> | Corrected evidence base | **44 rows / 20 sources** (`evidence_tables/Table_S1_corrected_evidence_44rows.csv`) |
> | Quarantine log | **10 rows** (`Table_S2_quarantine_log.csv`) |
> | Spot-check | **34/44** complete (`ra_tasks/spotcheck/`) |
> | **Figure 1** | Evidence-synthesis **procedure** flowchart (`figures/Figure1_evidence_synthesis_procedure.*`) |
> | **Figure 2** | Employment intensity by evidence family (`figures/Figure2_employment_intensity_v19.*`, `fig2_generate.py`) |
> | **Figure 3** | Employment cliff, per-MW and per-dollar (`figures/Figure3_employment_cliff_v19.*`, `fig3_generate.py`) |
>
> Older repo “Figure 1 / Figure 2” intensity/cliff PNGs (2026-07-03) are archived under
> `figures/_superseded_20260703/` and must not be cited as the manuscript figures.
> Work-package discovery remains a discovery/triage layer; analysed metrics are only those in
> Table S1 after human correction.

---

## 1. Why this document exists

The task was to confirm that every procedure, model and notebook actually executed in this
project is documented transparently enough for a top-journal reader to audit and re-run the
evidence base. This supplement (a) audits what intermediate manuscript Methods drafts already
covered, (b) identifies what they omitted at the time of the 2026-07-03 audit, (c) supplies
ready-to-insert Methods text, and (d) provides a full notebook → inputs → outputs → run-ID
reproducibility appendix.

**Headline finding of the original audit (2026-07-03).** Intermediate Methods drafts accurately
documented the *original* two-stream deep search, the reference-verification and extraction
pipeline, and an earlier correction/QC pass that produced a **34-row** evidence base. They did
**not** yet fully document two components that had been built and executed:

1. the **work-package gap-search campaign** — seven Universal Deep Search Agent runs
   (notebooks 00–06) that targeted the specific comparator and jobs-per-dollar gaps set out
   in `DEEP_SEARCH_PLAN_equal_investment_job_comparators_v01_20260630.md`; and
2. the **post-search triage layer** (notebook 07) that scores, de-duplicates and prioritises
   the ~2,000 harvested sources into research-assistant (RA) verification workbooks.

**Current status (manuscript v24 / this repository):** those discovery layers are documented;
selected July additions were integrated after human coding, producing the **44-row / 20-source**
Table S1. Residual independent PDF spot-checks remain open for a minority of rows (see
`ra_tasks/spotcheck/`). Discovery-only yields must still not be treated as the analysed
evidence base.

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
  Corrected citable evidence (44 rows / 20 sources; was 34/12 before July integration)
  + manuscript Figures 1–3 + Tables S1–S2
  (submission Figs 2–3: figures/fig2_generate.py, figures/fig3_generate.py)
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
| `07_prepare_manuscript_tables_and_figures.ipynb` | Manuscript tables + figure datasets (older multi-panel pipeline; submission Figs 2–3 use `figures/fig2_generate.py` / `fig3_generate.py`) |
| `08_correct_and_rebuild_manuscript_evidence_table.ipynb` | Correction pass → corrected 34-row base (§3.7) |

Regeneration order for the manuscript outputs: **06 → 07 → 08** (06 builds the master evidence
table from reviewed inputs; 07 turns it into the manuscript table/figure files; 08 applies the
corrections register to 07's outputs in place). Figures are then drawn by
`10_redraw_figures_expanded_20260703.py` and submission metadata re-applied by
`11_postprocess_submission_metadata_20260703.py` (see §9).

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

---

## 8. Verification pass results and gap outcomes (2026-07-03)

The triage workbooks were merged into a single master queue of **445 unique candidate sources**
(`triage_outputs/MASTER_RA_verification_queue.xlsx`) and hand-verified. Outcome: **11 verified,
434 rejected, 0 needs_source**. Every row records `reports_usable_metric`, `verification_status`
and a coder ID; each verified row carries metric, unit, phase, job scope, denominator, page/table
and a verbatim quote. The 97% rejection rate reflects the deliberately over-collected OpenAlex
harvest; two high-priority government rows were correctly rejected (macro spending multipliers;
RIMS II method, no facility metric). A cleaned shortlist is in
`triage_outputs/verified_for_coding.{xlsx,csv}`.

### 8.1 Corrections applied before coding (audit trail)
- **Deduplication:** two "new" verified sources were already in the 34-row base
  (`cmp_src_0003` Wei/Kammen; `cmp_src_0002` Garrett-Peltier) — retained as confirmation, not
  re-added.
- **Reclassification:** the 0.7–2.0 workers/MW row is a data-centre benchmark, routed to the DC
  track, not the comparator table.
- **Normalisation:** Nevada/Tesla (project-total person-years; needs capex for job-years/$M) and
  Faraday (recoded to jobs per GWh); GlobalFoundries flagged to confirm peak-vs-total headcount.
- **needs_source resolution (web audit):** NIST/DOC CHIPS figures are blended
  construction+manufacturing aggregates → background only; Linesight is a qualitative off-site/MEP
  source echoing the Hamm figure → narrative only.

### 8.2 Gap scorecard against the work-package plan (A–J)
- **Met:** advanced manufacturing / gigafactory / semiconductor (WP C — GlobalFoundries, BlueOval
  SK, Nevada/Tesla, Faraday); renewable energy (WP F — Cameron & van der Zwaan, AEMO/UTS, plus two
  pre-existing base sources).
- **Resolved:** the "10 jobs/MW" rule (WP supplemental) screened and rejected as a DC coefficient.
- **Partial (below yield bar):** warehousing/fulfilment (WP B — Prologis only, one source);
  per-dollar comparator anchors (Minnesota 3.93 jobs/$M, Garrett-Peltier 7.49).
- **Open:** social infrastructure (WP D+E), localness/incentives/realised jobs (WP G+H+J),
  quantified off-site prefabrication (WP I); and the **data-centre jobs-per-dollar anchor
  (WP A, P0)**, addressed by derivation in §8.3.

### 8.3 Derivation of data-centre jobs per dollar (Work Package A)
Because no directly reported DC jobs-per-$ figure passed verification, the metric was **derived**
from cited facility-level figures and cross-checked two independent ways
(`notebooks/09_derive_dc_jobs_per_dollar.ipynb`; outputs in `supplementary/dc_jobs_per_dollar_*`).

Ready-to-insert manuscript text:

> **Data-centre jobs per dollar of investment.** Because no primary source reported a directly
> usable data-centre jobs-per-dollar coefficient with a transparent basis, this metric was derived
> from facility-level projects that disclose both capacity and investment alongside construction or
> operations headcount (Ryu and Hiatt, 2025, Appendix A1), and cross-checked against a
> capacity-bridged estimate (workers per MW ÷ capital cost per MW). Data-centre projects support on
> the order of 0.5 peak construction workers per US$1 million of total project investment (range
> ≈0.2–0.7; two routes concordant) and ≈0.1 permanent operations jobs per US$1 million (range
> ≈0.05–0.17). The denominator is total project investment — which is dominated by imported IT,
> power and cooling equipment rather than on-site labour — so construction-only intensities would be
> roughly double. For comparison, general construction activity supports about 3.93 jobs per US$1
> million of construction output (Minnesota Legislative Budget Office). A dollar invested in a data
> centre therefore yields materially fewer local construction jobs than the same dollar spent on
> conventional construction or social infrastructure, and the permanent per-dollar footprint is
> roughly five times smaller again — the equal-investment corollary of the employment cliff.

Caveats to state: total-investment (not construction-only) denominator; construction = peak
headcount vs operations = permanent FTE (not summed); the construction figure leans on one clean
project plus the MW bridge; and the input pages require human confirmation against the primary PDF
before citation. Present as a bounded range, not a point estimate.

### 8.4 Remaining limitations to declare in v10
Warehousing rests on a single source; social infrastructure, localness/incentives, and quantified
off-site labour did not yield citable metrics and remain future work; the DC jobs-per-dollar figure
is a derived, provenance-logged range pending primary-source page confirmation.
**Update 2026-07-03:** page confirmation completed — all four Hamm Appendix A1 project figures
verified verbatim at printed p.8–9 (PDF p.9–10); the 0.7–2.0 workers/MW benchmark at printed p.1
(PDF p.2) and the A2 size-bucket table at printed p.10 (PDF p.11).

---

## 9. Integration of verified evidence into the manuscript build (2026-07-03)

The verified rows from §8 were coded into the evidence pipeline and the manuscript outputs
rebuilt. Record of exactly what was done:

### 9.1 Verification completed before coding
- **Hamm page gate (human check):** all derivation inputs verified against
  `source_pdfs/Hamm_Institute_2025_Data_Center_Employment_Forecast.pdf` (see §8.4 update).
- **Nevada/Tesla normalisation (ra_0012):** the GOED 2014 legislative analysis (archived at
  leg.state.nv.us, 28th Special Session, Exhibit B) confirms construction person-years and gives
  the pro-forma denominator ($1.0B buildings + $3.95B equipment ≈ $4.95B initial investment) →
  **1.87 construction job-years per $1M initial investment** (≈9.3/$M vs building capex alone).
  Coded as a DERIVED value with both denominators stated.
- **GlobalFoundries peak-vs-total (ra_0016):** confirmed via the Feb-2024 Commerce/GF CHIPS
  announcements — 9,000 construction jobs are **cumulative over the multi-project program life**,
  not a simultaneous peak. Recoded as `construction_jobs_total_project_life` and excluded from
  peak-based cliff ratios.
- **Faraday (ra_0017):** recoded to 140 direct cell-manufacturing jobs per GWh p.a. (180/GWh incl.
  module/pack), operations phase, capacity denominator.

### 9.2 Additions register
`submission_00/evidence_additions_20260703/` holds two reviewed-schema CSVs:
`comparator_additions_20260703.csv` (8 rows, review ids cmp_metric_0101–0108) and
`data_centre_additions_20260703.csv` (2 derived jobs-per-dollar rows, dc_metric_0201–0202,
source dc_hamm_2025). All rows carry ra_decision, page/table, verbatim quote, URL and caveats.

### 9.3 Notebook changes (all logged in the notebooks themselves)
- **06** — (a) reads the additions CSVs when present and appends them AFTER the base tables;
  (b) `evidence_id` is now assigned globally after concatenation, reproducing the archived ids
  (dc ev_0001–0084, comparator ev_0085–0106) exactly, with additions receiving ev_0107–ev_0116;
  (c) one new metric-family rule (`cumulative construction jobs` → construction_jobs_headcount).
- **07** — added the missing `job_years_per_mw` branch in the single-value unit assignment (the
  two new wind employment factors otherwise fell into `other_numeric_context`).
- **08** — unchanged; corrections register applies only to pre-existing evidence ids.
- **10_redraw_figures_expanded_20260703.py** — *historical* (2026-07-03) figure script under the
  then-current numbering: “Figure 1” = per-MW intensity with wind comparators; “Figure 2” =
  two-panel cliff + per-$1M. **Superseded for submission** by manuscript renumbering
  (Figure 1 = procedure flowchart; Figures 2–3 = intensity and cliff) and the v19 scripts
  `figures/fig2_generate.py` / `figures/fig3_generate.py`.
- **11_postprocess_submission_metadata_20260703.py** — re-applies the ev_0018/ev_0055/ev_0058
  metadata fixes and submission-relative `source_raw_path` rewrites that
  `_build_submission_00.py` had applied downstream of notebook 08.

### 9.4 Rebuild + regression checks (all passed)
- Base master rows (106) byte-identical to the archived pre-rebuild master (0 differing cells).
- Base figure rows identical to the archived corrected figure dataset.
- Corrected Table S1 base rows byte-identical to the co-author-reviewed 34-row file after
  post-processing; new table = **44 rows / 20 sources** (`Table_S1_corrected_evidence_44rows.csv`).
- Spot-check queue regenerated (44 rows); new rows ev_0107–ev_0116 remain `spotcheck_required`.
- Superseded 2026-06-29 files preserved in `supplementary/_superseded_20260703/`.

### 9.5 Manuscript v10
`manuscript/manuscript_v10_evidence_integration_20260703.docx` — tracked changes (author
"Claude", 2026-07-03): §3.3 replaced with the work-package campaign + triage + verification/
integration paragraphs; §3.4 discovery-yield note; §3.6 counts 116/62; §3.7 corrected base
44 rows/20 sources; §3.8 derived jobs-per-dollar metric + derivation paragraph; Table 1 counts
updated and its note rewritten; Data-availability extended; §4.4 per-dollar findings paragraph +
wind comparator sentence; new Figure 1 caption; Figure 2 caption rewritten; Limitations
(source audit 44 rows; comparator coverage rewritten). Both embedded figures replaced with the
2026-07-03 versions (later superseded — see §9.7).

### 9.6 Still open (QA gates before submission)
1. Co-author spot-check of the 10 new rows (ev_0107–ev_0116) + Ania's 8 priority rows.
2. Mazi's 10-row inter-coder reliability sample (report % agreement in §7).
3. Warehousing and general-construction multiplier classes remain single-source (flagged).
4. ~~Update the GitHub mirror with the rebuilt tables, figures and scripts.~~ **Done** for
   manuscript v24 alignment (2026-07-17): Figures 1–3 + generation scripts + README/CITATION.

### 9.7 Manuscript figure renumbering and v19 redraw (2026-07-16 submission set)
By manuscript v24 the figures are:

1. **Figure 1** — evidence-synthesis procedure flowchart (not a results chart).
2. **Figure 2** — employment intensity by evidence family (`Figure2_employment_intensity_v19.*`).
3. **Figure 3** — employment cliff, per-MW and scope-marked per-dollar (`Figure3_employment_cliff_v19.*`).

Generation scripts: `figures/fig2_generate.py`, `figures/fig3_generate.py`. The 2026-07-03
intensity/cliff PNGs are archived under `figures/_superseded_20260703/`.
