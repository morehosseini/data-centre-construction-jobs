# Spot-check workflow

## Files

| File | Purpose |
| :--- | :--- |
| `source_spotcheck_queue.csv` | 34 rows to verify against source PDFs in `../source_pdfs/` |
| `spotcheck_pass_fail_log.csv` | Results log |

## Current status (29 Jun 2026)

An automated context-quote audit marked all 34 rows **pass**. During co-author review:

1. **Ania** — independently verify the 8 priority rows listed in `COAUTHOR_REVIEW_CHECKLIST.md` against the PDFs/HTML in `source_pdfs/`. Update `reviewer`, `review_date`, and `notes` columns.
2. **Mazi** — re-code a 10-row sample; report % agreement to Reza for §7 Limitations.

## PDF locations

Paths in `source_spotcheck_queue.csv` point to `submission_00/source_pdfs/`. Twelve unique source files cover all 34 rows (some sources contribute multiple metrics).