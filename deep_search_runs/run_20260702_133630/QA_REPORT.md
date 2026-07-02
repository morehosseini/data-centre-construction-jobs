# QA Report
Run: run_20260702_133630

## Coverage & provenance
- Total unique URLs: 747
- Deterministically verified DOIs: 282
- DOI-shaped strings confirmed invalid: 106
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 3835

## Source-lane status
- crossref: ok=282 fail=0
- datacite: ok=3 fail=0
- openalex: ok=130 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 342
- openalex.org: 160
- doi.org: 110
- goodjobsfirst.org: 13
- jlarc.virginia.gov: 6
- comptroller.texas.gov: 5
- goed.nv.gov: 5
- www.lincolninst.edu: 5
- www.brookings.edu: 4
- www.parliament.nsw.gov.au: 4
- jlarc.wa.gov: 3
- sos.oregon.gov: 3
- www.auditor.illinois.gov: 3
- aemo.com.au: 2
- dls.maryland.gov: 2
- ilsr.org: 2
- leg.wa.gov: 2
- research.upjohn.org: 2
- www.audits.ga.gov: 2
- www.eca.europa.eu: 2

## WARN: Aggregators detected
- Verify primary publisher/DOI sources manually.

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://aemo.com.au/-/media/files/electricity/nem/planning_and_forecasting/nem_esoo/2023/2023-electricity-statement-of-opportunities.pdf
- 403 HEAD rejected | https://aemo.com.au/.../2023-electricity-statement-of-opportunities.pdf
- 403 HEAD rejected | https://doi.org/10.1002/pmj.21409
- 403 HEAD rejected | https://doi.org/10.1080/00141844.2018.1471513
- 403 HEAD rejected | https://doi.org/10.1080/01944360208976281
- 403 HEAD rejected | https://doi.org/10.1080/01944360408976336
- 403 HEAD rejected | https://doi.org/10.1080/01944360903490923
- 403 HEAD rejected | https://doi.org/10.1086/652282
- 403 HEAD rejected | https://doi.org/10.1093/qje/qjt034
- 403 HEAD rejected | https://doi.org/10.1093/qje/qju012
- 403 HEAD rejected | https://doi.org/10.1108/09699980810902712
- 403 HEAD rejected | https://doi.org/10.1111/anti.12595
- 403 HEAD rejected | https://doi.org/10.1111/cico.12193
- 403 HEAD rejected | https://doi.org/10.1111/irel.12222
- 403 HEAD rejected | https://doi.org/10.1111/j.1467-9663.2010.00611.x
- 403 HEAD rejected | https://doi.org/10.1111/j.1468-2230.2004.00493.x
- 403 HEAD rejected | https://doi.org/10.1111/j.1944-8287.2010.01077.x
- 403 HEAD rejected | https://doi.org/10.1111/pbaf.12265
- 403 HEAD rejected | https://doi.org/10.1111/puar.13328
- 403 HEAD rejected | https://doi.org/10.1111/puar.13350
- 403 HEAD rejected | https://doi.org/10.1111/puar.13353
- 403 HEAD rejected | https://doi.org/10.1111/puar.13427
- 403 HEAD rejected | https://doi.org/10.1126/science.aba3758
- 403 HEAD rejected | https://doi.org/10.1145/3531146.3533234
- 403 HEAD rejected | https://doi.org/10.1177/0163443720904601
- 403 HEAD rejected | https://doi.org/10.1177/0309132516664800
Potential broken links:
- 404 | https://audgen.michigan.gov/wp-content/uploads/2021/12/r271040020-0015.pdf
- ERR | https://biz.loudoun.gov/wp-content/uploads/2023/04/Data-Center-Revenue-Report-2023.pdf
- 465 | https://cardozolawreview.com/do-community-benefits-agreements-benefit-communities
- 404 | https://comptroller.texas.gov/transparency/reports/data-centers
- 404 | https://dls.maryland.gov/pubs/prod/TaxFiscal/Evaluation-of-the-Data-Center-Sales-and-Use-Tax-Exemption.pdf
- 404 | https://dls.maryland.gov/pubs/prod/TaxFiscal/Evaluation-of-the-Sales-and-Use-Tax-Exemption-for-Data-Centers.pdf
- 404 | https://doi.org/10.1002/pmj.21595
- 404 | https://doi.org/10.1016/S0263-7863(00
- 404 | https://doi.org/10.1016/j.energy.2019.116962
- 404 | https://doi.org/10.1016/j.ijproman.2020.03.006
- 404 | https://doi.org/10.1016/j.jue.2022.103500
- 404 | https://doi.org/10.1016/j.telpol.2020.102065
- 404 | https://doi.org/10.1017/9781316997406
- 404 | https://doi.org/10.1017/9781316997428
- 404 | https://doi.org/10.1017/S0143814X1600018X
- 404 | https://doi.org/10.1038/s41612-021-00173-6
- 404 | https://doi.org/10.1061/(ASCE
- 404 | https://doi.org/10.1080/0034340042000201865
- 404 | https://doi.org/10.1080/01441647.2018.1506194
- 404 | https://doi.org/10.1080/01446193.2017.1315154
- 404 | https://doi.org/10.1080/01944363.2020.1852102
- 404 | https://doi.org/10.1080/01944363.2022.2123385
- 404 | https://doi.org/10.1080/13604813.2016.1162584
- 404 | https://doi.org/10.1080/1369118X.2017.1328626
- 404 | https://doi.org/10.1111/ijur.12365
- 404 | https://doi.org/10.1111/j.1467-8306.2008.00609.x
- 404 | https://doi.org/10.1177/0042098018776900
- 404 | https://doi.org/10.1177/0160449X20913361
- 404 | https://doi.org/10.1177/0160449X20951171
- 404 | https://doi.org/10.1177/0162243919859636
- 404 | https://doi.org/10.1177/0263775818806568
- 404 | https://doi.org/10.1177/0275074013500612
- 404 | https://doi.org/10.1177/0308518X211029402