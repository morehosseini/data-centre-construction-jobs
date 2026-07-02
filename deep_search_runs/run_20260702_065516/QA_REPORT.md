# QA Report
Run: run_20260702_065516

## Coverage & provenance
- Total unique URLs: 698
- Deterministically verified DOIs: 291
- DOI-shaped strings confirmed invalid: 104
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 4244

## Source-lane status
- crossref: ok=291 fail=0
- datacite: ok=3 fail=0
- openalex: ok=129 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 271
- openalex.org: 161
- doi.org: 126
- www.nist.gov: 15
- www.energy.gov: 13
- www.brookings.edu: 11
- goodjobsfirst.org: 6
- legis.wisconsin.gov: 4
- www.epi.org: 4
- www.semiconductors.org: 4
- comptroller.texas.gov: 2
- esd.ny.gov: 2
- goed.nv.gov: 2
- gvcc.duke.edu: 2
- in.micron.com: 2
- semiconductor.samsung.com: 2
- www.anl.gov: 2
- www.chicagofed.org: 2
- www.gao.gov: 2
- www.georgia.org: 2

## WARN: Aggregators detected
- Verify primary publisher/DOI sources manually.

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://crsreports.congress.gov/product/pdf/R/R46581
- 403 HEAD rejected | https://doi.org/10.1002/pmj.21409
- 403 HEAD rejected | https://doi.org/10.1039/D1EE01530C
- 403 HEAD rejected | https://doi.org/10.1080/00343409312331347655
- 403 HEAD rejected | https://doi.org/10.1080/01944360408976336
- 403 HEAD rejected | https://doi.org/10.1080/09535314.2017.1301395
- 403 HEAD rejected | https://doi.org/10.1086/698859
- 403 HEAD rejected | https://doi.org/10.1086/701424
- 403 HEAD rejected | https://doi.org/10.1086/722703
- 403 HEAD rejected | https://doi.org/10.1093/cje/beu037
- 403 HEAD rejected | https://doi.org/10.1093/cjres/rsu019
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lbw018
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lbw038
- 403 HEAD rejected | https://doi.org/10.1093/oxrep/grw022
- 403 HEAD rejected | https://doi.org/10.1093/qje/qjt034
- 403 HEAD rejected | https://doi.org/10.1108/ECAM-07-2020-0583
- 403 HEAD rejected | https://doi.org/10.1111/1468-2427.00184
- 403 HEAD rejected | https://doi.org/10.1111/j.0017-4815.2004.00238.x
- 403 HEAD rejected | https://doi.org/10.1111/j.1468-0009.2007.00501.x
- 403 HEAD rejected | https://doi.org/10.1111/j.1468-2427.2008.00826.x
- 403 HEAD rejected | https://doi.org/10.1111/jiec.12072
- 403 HEAD rejected | https://doi.org/10.1111/jiec.12733
- 403 HEAD rejected | https://doi.org/10.1111/jors.12495
- 403 HEAD rejected | https://doi.org/10.1126/science.1256973
- 403 HEAD rejected | https://doi.org/10.1126/science.191.4227.535
- 403 HEAD rejected | https://doi.org/10.1126/science.abo7027
- 403 HEAD rejected | https://doi.org/10.1126/science.abq7781
- 403 HEAD rejected | https://doi.org/10.1162/003355303322552801
- 403 HEAD rejected | https://doi.org/10.1162/REST_a_00604
- 403 HEAD rejected | https://doi.org/10.1177/0019793916660067
Potential broken links:
- 404 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/484133/employment_densities_guide_3rd_edition.pdf
- ERR | https://connect.ncdot.gov/projects/research/RNAProjDocs/2013-19FinalReport_Vol-1.pdf
- 404 | https://cset.georgetown.edu/publication/the-chips-act-and-the-semiconductor-workforce
- 404 | https://development.ohio.gov/wps/wcm/connect/gov/42551405-8854-469b-8321-42013b290c52/Intel+Annual+Report+2023.pdf
- 404 | https://doi.org/10.1007/s00168-020-00994-x
- 404 | https://doi.org/10.1007/s12122-010-9095-z
- 404 | https://doi.org/10.1016/j.enpol.2023.113540
- 404 | https://doi.org/10.1017/S0143814X1700008X
- 404 | https://doi.org/10.1061/(ASCE
- 404 | https://doi.org/10.1061/JCEMD4.COENG-12853
- 404 | https://doi.org/10.1068/a250087
- 404 | https://doi.org/10.1080/00130095.2021.1969714
- 404 | https://doi.org/10.1080/00207738.2018.1473098
- 404 | https://doi.org/10.1080/0034340042000201840
- 404 | https://doi.org/10.1080/0034340042000201865
- 404 | https://doi.org/10.1080/00343400701281758
- 404 | https://doi.org/10.1080/00343404.2020.1739257
- 404 | https://doi.org/10.1080/0042098984861
- 404 | https://doi.org/10.1080/0144164032000028732
- 404 | https://doi.org/10.1080/01446193.2012.687823
- 404 | https://doi.org/10.1080/01944363.2015.1085328
- 404 | https://doi.org/10.1080/01944363.2023.2173360
- 404 | https://doi.org/10.1080/07352166.2022.2071285
- 404 | https://doi.org/10.1080/09535314.2022.2078278
- 404 | https://doi.org/10.1080/14615517.2017.1327452
- 404 | https://doi.org/10.1086/663986
- 404 | https://doi.org/10.1108/ECAM-01-2021-0062
- 404 | https://doi.org/10.1111/ecge.12228
- 404 | https://doi.org/10.11684/eaer.2020.24.4.349
- 404 | https://doi.org/10.1177/0019793918773574
- 404 | https://doi.org/10.1177/0022185613504473