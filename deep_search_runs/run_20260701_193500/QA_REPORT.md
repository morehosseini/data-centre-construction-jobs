# QA Report
Run: run_20260701_193500

## Coverage & provenance
- Total unique URLs: 598
- Deterministically verified DOIs: 303
- DOI-shaped strings confirmed invalid: 124
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 4013

## Source-lane status
- crossref: ok=303 fail=0
- datacite: ok=3 fail=0
- openalex: ok=128 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 295
- openalex.org: 160
- doi.org: 59
- goodjobsfirst.org: 5
- www.epi.org: 5
- www.prologis.com: 5
- jlarc.virginia.gov: 4
- www.bea.gov: 3
- www.brookings.edu: 3
- www.cbre.com: 3
- www.naiop.org: 3
- bpf.org.uk: 2
- goed.nv.gov: 2
- laborcenter.berkeley.edu: 2
- mn.gov: 2
- www.bls.gov: 2
- www.energy.gov: 2
- www.gov.uk: 2
- apps.who.int: 1
- assets.publishing.service.gov.uk: 1

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://apps.who.int/iris/handle/10665/250047
- 403 HEAD rejected | https://crsreports.congress.gov/product/pdf/R/R46581
- 403 HEAD rejected | https://doi.org/10.1002/pam.22271
- 403 HEAD rejected | https://doi.org/10.1080/24694452.2020.1835461
- 403 HEAD rejected | https://doi.org/10.1086/705716
- 403 HEAD rejected | https://doi.org/10.1093/ej/ueaa085
- 403 HEAD rejected | https://doi.org/10.1093/jeea/jvaa046
- 403 HEAD rejected | https://doi.org/10.1093/jeea/jvab012
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lby047
- 403 HEAD rejected | https://doi.org/10.1093/oxrep/graa015
- 403 HEAD rejected | https://doi.org/10.1093/qje/qju013
- 403 HEAD rejected | https://doi.org/10.1093/rfs/hhac011
- 403 HEAD rejected | https://doi.org/10.1108/ECAM-05-2019-0265
- 403 HEAD rejected | https://doi.org/10.1111/jors.12464
- 403 HEAD rejected | https://doi.org/10.1111/tesg.12245
- 403 HEAD rejected | https://doi.org/10.1162/003355303322552801
- 403 HEAD rejected | https://doi.org/10.1177/0739456X18786392
- 403 HEAD rejected | https://doi.org/10.1257/aer.100.2.373
- 403 HEAD rejected | https://doi.org/10.1257/jep.34.2.90
- 403 HEAD rejected | https://doi.org/10.1287/mnsc.2020.3812
- 403 HEAD rejected | https://doi.org/10.1287/mnsc.2023.01168
- 403 HEAD rejected | https://eta.lbl.gov/publications/united-states-data-center-energy
- 403 HEAD rejected | https://goodjobsfirst.org/amazon-tracker
- 403 HEAD rejected | https://goodjobsfirst.org/data-centers
- 403 HEAD rejected | https://goodjobsfirst.org/financial-exposure
- 403 HEAD rejected | https://goodjobsfirst.org/money-lost-to-the-cloud
- 403 HEAD rejected | https://openalex.org/W1504338911
- 403 HEAD rejected | https://openalex.org/W1516534262
- 403 HEAD rejected | https://openalex.org/W1549280300
- 403 HEAD rejected | https://openalex.org/W1564759675
Potential broken links:
- 404 | https://bpf.org.uk/media/2784/bpf-what-warehousing-where-report-2019.pdf
- 404 | https://bpf.org.uk/our-work/research-and-briefings/levelling-up-the-logic-of-logistics
- 404 | https://dceo.illinois.gov/content/dam/soi/en/web/dceo/aboutdceo/reports/2023-data-center-report.pdf
- 404 | https://development.ohio.gov/home/news-and-events/all-news/2022-0121-intel-selects-ohio-for-historic-investment
- 404 | https://doi.org/10.1016/j.jtrangeo.2018.12.020
- 404 | https://doi.org/10.1016/j.jtrangeo.2019.102511
- 404 | https://doi.org/10.1016/j.jtrangeo.2023.103580
- 404 | https://doi.org/10.1016/j.jue.2022.103444
- 404 | https://doi.org/10.1080/00330124.2022.2148560
- 404 | https://doi.org/10.1080/01446193.2022.2057741
- 404 | https://doi.org/10.1080/01446193.2022.2064344
- 404 | https://doi.org/10.1111/ilr.12129
- 404 | https://doi.org/10.1177/0263775818804282
- 404 | https://doi.org/10.1177/08912424221102280
- 404 | https://doi.org/10.1177/0950017017742069
- 404 | https://doi.org/10.1257/jep.34.3.90
- 404 | https://doi.org/10.1287/mnsc.2023.00392
- 404 | https://goed.nv.gov/tesla-announces-3-6-billion-expansion
- 404 | https://goed.nv.gov/wp-content/uploads/2021/08/Tesla-Economic-Impact-Summary.pdf
- ERR | https://goodjobsfirst.org/wp-content/uploads/2022/01/megadeals2021.pdf
- 403 | https://governor.kansas.gov/governor-laura-kelly-announces-panasonic-energy-to-build-megafactory-in-kansas
- ERR | https://investors.micron.com/news-releases/news-release-details/micron-announces-historic-investment-100-billion-build-megafab
- ERR | https://jlarc.wa.gov/reports/2022/DataCenters/p_1.html
- 404 | https://laborcenter.berkeley.edu/the-future-of-warehouse-work
- 404 | https://mn.gov/deed/assets/data-center-eval-2021_tcm1045-465492.pdf
- 404 | https://mn.gov/deed/assets/data-center-tax-exemption-report_tcm1045-495943.pdf