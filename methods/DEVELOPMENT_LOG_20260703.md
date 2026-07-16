# Development log — 2026-07-03

## Control check on the gap-search campaign (notebooks 00–06)
- Verified all 7 Universal Deep Search Agent runs completed (8/8 slices, synthesis + QA present).
- Confirmed required inputs exist in every run folder for triage
  (FINAL_MERGED_SYNTHESIS.md, QA_REPORT.md, verified_sources.csv, datasets.csv, final_citation_audit.csv).
- Raw discovery yield: ~2,002 verified DOIs and ~404 datasets across the 7 runs.
- Note: `verified_dois` counts are a raw over-collected yield, not analysed evidence
  (e.g. WP B's top verified source is an off-topic criminal-justice paper). Triage + human
  verification is what converts leads into citable evidence.

## Notebook 07 — post-search triage: RUN COMPLETED for all 7 runs
- Ran the triage logic (relevance scoring, DOI/URL/title de-duplication, RA workbook build) for
  runs 00–06.
- Outputs written to `vscode_ready/notebooks/triage_outputs/run_*/`
  (`comparator_source_triage.csv`, `comparator_metric_review_template.csv`,
  `comparator_RA_review_workbook.xlsx`) + cross-run roll-up `_triage_summary_all_runs.csv`.
- Per-run: ~300–365 unique sources → 175–281 promoted → 90 RA review slots each (630 total).
- Reproduced the pre-existing WP B triage (run_20260701_193500) within rounding, confirming determinism.
- WP A (run_20260701_143537) triaged for completeness but flagged as a DC benchmark, not a comparator.

## Methods / reproducibility audit
- Audited manuscript §3 (v09). Existing text accurately covers the original two-stream search,
  reference verification, extraction, synthesis and the correction pass (notebook 08).
- Gap: §3.3, Table 1 and the Data-availability statement predate and do NOT document the
  work-package gap-search campaign or the triage layer.
- Produced `methods/REPRODUCIBILITY_pipeline_and_methods_supplement_v01_20260703.md` with:
  full two-pipeline register, exact models (deep-research-preview-04-2026 + gemini-3.1-pro-preview,
  google-genai, uds_hardened_v3), a §3 audit table, ready-to-insert Methods paragraphs, a notebook
  reproducibility appendix, and an honest limitations block.

## Records updated
- `run_results_index.json` — added `triage_stage` block (per-run counts + next step).
- `deep_search/README.md` — marked notebook 07 COMPLETED with pointer to the supplement.
- This log.

## Next actions (verification gate — nothing enters a finding until done)
1. Assign RA metric-review workbooks (high-priority + government/audit/method rows first).
2. Verify primary sources; record metric/unit/phase/denominator/direct-vs-total/page/quote.
3. Feed verified comparator rows into notebook 06 → rebuild via 08 → regenerate figures via 07.
4. Apply the DEEP_SEARCH_PLAN yield bar (≥2 citable sources, compatible units) before adding any
   comparator class to a finding.
5. Update manuscript §3.3, Table 1 and Data-availability using the supplement's §4 text (for v10).

## RA verification pass — completed & QA'd (Cursor RA, checked 2026-07-03)
- Master queue (445 unique sources) fully coded: 11 verified, 434 rejected, 0 needs_source.
- Independent check: all 445 have mandatory fields; 11/11 verified fully coded with page + quote;
  the two rejected high-priority government rows (Auerbach/Gorodnichenko macro multipliers; RIMS II)
  are correct rejections. 97% rejection reflects deliberate OpenAlex over-collection.
- Cleaned shortlist written: `triage_outputs/verified_for_coding.{xlsx,csv}`.
  → 8 NEW comparator rows, 2 confirmations of existing base sources, 1 reclassified to DC track.

### Fixes applied before coding into the evidence table
- Dedup: ra_0004 (Wei/Kammen = cmp_src_0003) and ra_0006 (Garrett-Peltier = cmp_src_0002) are
  ALREADY in the 34-row base → do not add as new rows (confirmation only).
- Reclassify: ra_0429 (0.7-2.0 workers/MW) is a data-centre benchmark, not a comparator → DC track.
- Normalise: ra_0012 (9,275 = project-total person-years; needs Tesla capex for job-years/$M),
  ra_0017 (recode to jobs per GWh). Confirm ra_0016 peak-vs-total (employment-cliff).

### needs_source resolved (web check)
- ra_0018 NIST/DOC CHIPS → rejected: only blended construction+manufacturing aggregates; background only.
- ra_0092 Linesight → rejected as metric: qualitative off-site/MEP narrative; its 0.7-2.0 workers/MW
  is the Hamm figure (ra_0429). Keep for off-site/MEP limitation prose only.

### Yield-bar status (new usable comparators)
- Advanced manufacturing / gigafactory / semiconductor: MET (GlobalFoundries, BlueOval SK, Nevada/Tesla, Faraday).
- Energy / renewables: MET (Cameron & van der Zwaan, AEMO/UTS) + 2 existing base sources.
- Warehousing / logistics: NOT MET — only Prologis (0.0145 jobs/m²); needs a 2nd quantitative source.
- Data-centre jobs-per-DOLLAR (WP A, P0): still NOT anchored — no verified DC per-$ figure; the direct
  bridge to the equal-investment question remains open.

### Next
Code the 8 new rows (after normalising ra_0012/ra_0017 and confirming ra_0016) into notebook 06 →
rebuild via 08 → figures via 07. Flag warehousing + DC-per-$ as remaining limitations in v10.

## DC jobs-per-dollar derivation (WP A gap) — 2026-07-03
- No verified DC per-$ source; derived from Hamm Institute (2025) Appendix A1 project figures.
- Notebook: submission_00/notebooks/09_derive_dc_jobs_per_dollar.ipynb (reproducible, provenance-tagged).
- Result: ~0.5 peak construction workers per $1M total investment (range 0.2-0.7; two routes agree);
  ~0.1 permanent jobs/$M (0.05-0.17). Comparator contrast: general construction ~3.93 jobs/$M.
- Denominator = total investment (not construction-only); flagged for human page-confirmation before citing.
- Methods supplement updated (new §8: verification results, gap scorecard, derivation, limitations).
- Outputs: supplementary/dc_jobs_per_dollar_{inputs_and_derivation.csv,summary.json}.

## Integration into manuscript build — COMPLETED (2026-07-03, later session)
1. **Hamm page gate PASSED:** all derivation inputs verified verbatim against the PDF
   (Appendix A1, printed p.8–9 / PDF p.9–10; benchmark 0.7–2.0 workers/MW printed p.1 / PDF p.2;
   A2 table printed p.10 / PDF p.11). The derived DC per-$ figures are now citable.
2. **Three fixes resolved:** Nevada/Tesla normalised to 1.87 construction job-years/$M initial
   investment (GOED 2014 pro-forma: $1.0B buildings + $3.95B equipment); GlobalFoundries 9,000
   confirmed as TOTAL over program life (Commerce/GF Feb-2024) and recoded (excluded from
   peak-based cliff ratios); Faraday recoded to 140 direct jobs/GWh p.a. (operations).
3. **Coding:** additions register `submission_00/evidence_additions_20260703/` (8 comparator +
   2 derived DC rows) → notebook 06 (patched: additions ingestion + global evidence ids
   preserving ev_0001–0106) → 07 (patched: job_years_per_mw unit branch) → 08 (unchanged).
   True dependency order is 06 → 07 → 08 (08 corrects 07's outputs in place).
4. **Regression checks passed:** 106 base master rows and 34 base Table-S1 rows byte-identical
   to the co-author-reviewed build; additions get ev_0107–ev_0116.
5. **Outputs refreshed:** Table_S1_corrected_evidence_44rows.csv (44 rows / 20 sources),
   spot-check queue 44 rows, figure dataset 54 rows; old files in supplementary/_superseded_20260703/.
   New figures: figure_01_..._expanded_20260703.png, figure_02_employment_cliff_and_per_dollar_20260703.png
   (script: notebooks/10_redraw_figures_expanded_20260703.py; metadata: 11_postprocess_...py).
6. **Manuscript v10 created with tracked changes:**
   manuscript/manuscript_v10_evidence_integration_20260703.docx — §3.3 (WP campaign, triage,
   verification/integration), §3.4 yield note, §3.6–3.7 counts (116/62; 44 rows/20 sources),
   §3.8 derived per-$ metric + derivation, Table 1 + note, Data availability, §4.4 per-dollar
   findings, Figure 1 caption added, Figure 2 caption rewritten, Limitations updated; embedded
   figures replaced. Methods supplement §9 records the full integration.
7. **Remaining QA gates:** co-author spot-check of ev_0107–ev_0116 (+ Ania's priority rows);
   Mazi's 10-row inter-coder sample; GitHub mirror refresh.

## 2026-07-17 — repository alignment with manuscript v24
- Replaced published figures with manuscript submission set:
  - Figure 1: evidence-synthesis procedure flowchart
  - Figures 2–3: v19 employment intensity + employment cliff (PDF/SVG/PNG/TIFF)
- Added `figures/fig2_generate.py` and `figures/fig3_generate.py` (source of record for MS Figs 2–3).
- Archived 2026-07-03 intensity/cliff PNGs under `figures/_superseded_20260703/`.
- Updated README, CITATION.cff, REPOSITORY_NOTES, figures/README, and REPRODUCIBILITY supplement
  banner to current title, 44/20 counts, 34/44 spot-check status, and Figures 1–3 map.
- Verified Figure 1 PNG and Figures 2–3 TIFF SHA-256 hashes match `manuscript_v24_20260716.docx` media.
