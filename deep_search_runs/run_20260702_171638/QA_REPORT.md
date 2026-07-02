# QA Report
Run: run_20260702_171638

## Coverage & provenance
- Total unique URLs: 743
- Deterministically verified DOIs: 287
- DOI-shaped strings confirmed invalid: 92
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 3706

## Source-lane status
- crossref: ok=287 fail=0
- datacite: ok=3 fail=0
- openalex: ok=130 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 327
- openalex.org: 160
- doi.org: 122
- www.gov.uk: 6
- www.infrastructureaustralia.gov.au: 6
- grattan.edu.au: 5
- sgsep.com.au: 5
- www.epi.org: 5
- www.aha.org: 4
- www.infrastructure.nsw.gov.au: 4
- goodjobsfirst.org: 3
- www.abs.gov.au: 3
- www.aihw.gov.au: 3
- www.nahb.org: 3
- www.planningportal.nsw.gov.au: 3
- www.vhba.vic.gov.au: 3
- jlarc.virginia.gov: 2
- americaninnovation.org: 2
- peri.umass.edu: 2
- www.alia.org.au: 2

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://apps.who.int/iris/bitstream/handle/10665/250047/9789241511308-eng.pdf
- 403 HEAD rejected | https://bphc.hrsa.gov/data-research
- 403 HEAD rejected | https://crsreports.congress.gov/product/pdf/R/R46581
- 403 HEAD rejected | https://doi.org/10.1002/hec.4450
- 403 HEAD rejected | https://doi.org/10.1002/pmj.21409
- 403 HEAD rejected | https://doi.org/10.1080/01446193.2018.1476729
- 403 HEAD rejected | https://doi.org/10.1080/01446193.2020.1795217
- 403 HEAD rejected | https://doi.org/10.1080/014461997372809
- 403 HEAD rejected | https://doi.org/10.1080/014461997372926
- 403 HEAD rejected | https://doi.org/10.1080/01616846.2016.1245003
- 403 HEAD rejected | https://doi.org/10.1080/10511482.2018.1524443
- 403 HEAD rejected | https://doi.org/10.1086/669539
- 403 HEAD rejected | https://doi.org/10.1086/705716
- 403 HEAD rejected | https://doi.org/10.1093/cjres/rsad004
- 403 HEAD rejected | https://doi.org/10.1093/epolic/eiy014
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lbab005
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lbx024
- 403 HEAD rejected | https://doi.org/10.1093/oep/gpv027
- 403 HEAD rejected | https://doi.org/10.1093/qje/qjt034
- 403 HEAD rejected | https://doi.org/10.1093/restud/rds010
- 403 HEAD rejected | https://doi.org/10.1108/ECAM-02-2017-0035
- 403 HEAD rejected | https://doi.org/10.1111/ecot.12157
- 403 HEAD rejected | https://doi.org/10.1111/ecot.12213
- 403 HEAD rejected | https://doi.org/10.1111/j.1468-2257.2005.00267.x
- 403 HEAD rejected | https://doi.org/10.1111/j.1475-6773.2005.00497.x
- 403 HEAD rejected | https://doi.org/10.1111/joes.12046
- 403 HEAD rejected | https://doi.org/10.1111/jors.12479
- 403 HEAD rejected | https://doi.org/10.1111/ntwe.12239
- 403 HEAD rejected | https://doi.org/10.1126/science.287.5456.1207
- 403 HEAD rejected | https://doi.org/10.1162/REST_a_00457
Potential broken links:
- ERR | http://jlarc.virginia.gov/pdfs/reports/Rpt518.pdf
- ERR | https://agedcare.royalcommission.gov.au
- 404 | https://doi.org/10.1007/s00168-014-0612-4
- 404 | https://doi.org/10.1016/0143-6228(92
- 404 | https://doi.org/10.1016/0197-3975(92
- 404 | https://doi.org/10.1016/0272-7757(92
- 404 | https://doi.org/10.1016/0304-3932(89
- 404 | https://doi.org/10.1016/j.econedurev.2019.101907
- 404 | https://doi.org/10.1016/j.energy.2019.116962
- 404 | https://doi.org/10.1016/j.enpol.2021.112402
- 404 | https://doi.org/10.1016/j.habitatint.2019.102074
- 404 | https://doi.org/10.1016/j.habitatint.2021.102427
- 404 | https://doi.org/10.1016/j.habitatint.2022.102521
- 404 | https://doi.org/10.1016/j.ijpe.2021.108124
- 404 | https://doi.org/10.1016/j.jpubeco.2015.11.004
- 404 | https://doi.org/10.1016/j.jue.2021.103433
- 404 | https://doi.org/10.1016/j.socscimed.2020.113051
- 404 | https://doi.org/10.1016/j.telpol.2022.102356
- 404 | https://doi.org/10.1061/(ASCE
- 404 | https://doi.org/10.1068/c9846
- 404 | https://doi.org/10.1080/00343404.2023.2284992
- 404 | https://doi.org/10.1080/01446190.2020.1769748
- 404 | https://doi.org/10.1080/01446190110035674
- 404 | https://doi.org/10.1080/01446193.2016.1245440
- 404 | https://doi.org/10.1080/01446193.2020.1824271
- 404 | https://doi.org/10.1080/02673037.2017.1363871
- 404 | https://doi.org/10.1080/09535314.2019.1683115
- 404 | https://doi.org/10.1080/09692290.2021.1947356
- 404 | https://doi.org/10.1080/10511482.2016.1245207
- 404 | https://doi.org/10.1080/15623599.2020.1824676
- 404 | https://doi.org/10.1093/0195035275.001.0001
- 404 | https://doi.org/10.1177/0042098019881381