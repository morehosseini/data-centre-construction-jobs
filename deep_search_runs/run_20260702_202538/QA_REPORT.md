# QA Report
Run: run_20260702_202538

## Coverage & provenance
- Total unique URLs: 600
- Deterministically verified DOIs: 297
- DOI-shaped strings confirmed invalid: 67
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 4249

## Source-lane status
- crossref: ok=297 fail=0
- datacite: ok=3 fail=0
- openalex: ok=129 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 321
- openalex.org: 160
- doi.org: 28
- www.nrel.gov: 5
- www.planningportal.nsw.gov.au: 5
- www.energy.gov: 4
- aemo.com.au: 3
- opus.lib.uts.edu.au: 3
- rael.berkeley.edu: 3
- www.cleanenergycouncil.org.au: 3
- www.linesight.com: 3
- www.prologis.com: 3
- www.semiconductors.org: 3
- goodjobsfirst.org: 2
- jlarc.virginia.gov: 2
- uptimeinstitute.com: 2
- www.bain.com: 2
- www.cbre.com: 2
- www.construction.com: 2
- www.irena.org: 2

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://aemo.com.au
- 403 HEAD rejected | https://aemo.com.au/-/media/files/major-publications/isp/2024/isf-report-australian-electricity-workforce-for-the-2024-isp.pdf
- 403 HEAD rejected | https://aemo.com.au/en/energy-systems/major-publications/integrated-system-plan-isp
- 403 HEAD rejected | https://doi.org/10.1080/01446190500184444
- 403 HEAD rejected | https://doi.org/10.1080/01446190600827058
- 403 HEAD rejected | https://doi.org/10.3390/buildings9020038
- 403 HEAD rejected | https://eta.lbl.gov/publications/best-practices-data-centers-lessons
- 403 HEAD rejected | https://goodjobsfirst.org/data-center-subsidies-an-update
- 403 HEAD rejected | https://goodjobsfirst.org/money-lost-to-the-cloud
- 403 HEAD rejected | https://openalex.org/W1482180939
- 403 HEAD rejected | https://openalex.org/W1483121473
- 403 HEAD rejected | https://openalex.org/W153298446
- 403 HEAD rejected | https://openalex.org/W1728410617
- 403 HEAD rejected | https://openalex.org/W1748265057
- 403 HEAD rejected | https://openalex.org/W1964517869
- 403 HEAD rejected | https://openalex.org/W1966941463
- 403 HEAD rejected | https://openalex.org/W1967954450
- 403 HEAD rejected | https://openalex.org/W1968200193
- 403 HEAD rejected | https://openalex.org/W1968424563
- 403 HEAD rejected | https://openalex.org/W1970867726
- 403 HEAD rejected | https://openalex.org/W1970971825
- 403 HEAD rejected | https://openalex.org/W1972965101
- 403 HEAD rejected | https://openalex.org/W1976793263
- 403 HEAD rejected | https://openalex.org/W1977428702
- 403 HEAD rejected | https://openalex.org/W1978906769
- 403 HEAD rejected | https://openalex.org/W1984224922
- 403 HEAD rejected | https://openalex.org/W1991991538
- 403 HEAD rejected | https://openalex.org/W1994828539
- 403 HEAD rejected | https://openalex.org/W1995790959
- 403 HEAD rejected | https://openalex.org/W2002828685
Potential broken links:
- 404 | https://doi.org/10.1016/j.autcon.2021.103945
- 404 | https://doi.org/10.1061/(ASCE
- 404 | https://doi.org/10.1146/annurev-resource-100815-095449
- 404 | https://download.schneider-electric.com/files?p_Doc_Ref=SPD_WP227_EN
- 404 | https://irle.berkeley.edu/publications/research-briefs/the-future-of-warehouse-work
- 404 | https://leg.wa.gov/jlarc/reports/2021/DataCenters/p/default.html