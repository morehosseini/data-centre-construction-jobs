# QA Report
Run: run_20260701_071034

## Coverage & provenance
- Total unique URLs: 686
- Deterministically verified DOIs: 298
- DOI-shaped strings confirmed invalid: 85
- DOI-shaped strings unverified/transient: 0
- OpenAlex works in graph: 180
- Citation edges: 3992

## Source-lane status
- crossref: ok=298 fail=0
- datacite: ok=3 fail=0
- openalex: ok=128 fail=3 (HTTP 503)
- zenodo: ok=3 fail=0

## Slice & synthesis completeness
- Planned slices: 8
- Represented in final synthesis: 8
- Missing/non-included from synthesis: none
- Final-synthesis corpus size: 200000 chars

## Domain frequency (Top 20)
- vertexaisearch.cloud.google.com: 376
- openalex.org: 160
- doi.org: 97
- goodjobsfirst.org: 4
- www.energy.gov: 4
- www.mckinsey.com: 4
- www.nrel.gov: 3
- assets.publishing.service.gov.uk: 2
- bpf.org.uk: 2
- goed.nv.gov: 2
- laborcenter.berkeley.edu: 2
- mn.gov: 2
- www.prologis.com: 2
- www.semiconductors.org: 2
- datacentercoalition.org: 1
- gvcc.duke.edu: 1
- jlarc.virginia.gov: 1
- leg.wa.gov: 1
- libertystreeteconomics.newyorkfed.org: 1
- mitpress.mit.edu: 1

## Broken-link sampling (HEAD then GET fallback; capped at 100)
HEAD rejected but not necessarily broken:
- 403 HEAD rejected | https://doi.org/10.1002/pmj.21409
- 403 HEAD rejected | https://doi.org/10.1080/01446190010020435
- 403 HEAD rejected | https://doi.org/10.1080/01446190500184444
- 403 HEAD rejected | https://doi.org/10.1080/01446190601071821
- 403 HEAD rejected | https://doi.org/10.1080/09613218.2019.1669009
- 403 HEAD rejected | https://doi.org/10.1086/653714
- 403 HEAD rejected | https://doi.org/10.1086/705716
- 403 HEAD rejected | https://doi.org/10.1093/cjres/rsad015
- 403 HEAD rejected | https://doi.org/10.1093/icc/11.3.451
- 403 HEAD rejected | https://doi.org/10.1093/jeg/lbaa014
- 403 HEAD rejected | https://doi.org/10.1108/14714170910931552
- 403 HEAD rejected | https://doi.org/10.1108/14714171111104637
- 403 HEAD rejected | https://doi.org/10.1108/IJPPM-02-2016-0038
- 403 HEAD rejected | https://doi.org/10.1111/1468-2427.12612
- 403 HEAD rejected | https://doi.org/10.1111/anti.12878
- 403 HEAD rejected | https://doi.org/10.1111/ecge.12068
- 403 HEAD rejected | https://doi.org/10.1111/j.0040-747X.2004.00294.x
- 403 HEAD rejected | https://doi.org/10.1177/2053951718820549
- 403 HEAD rejected | https://doi.org/10.1257/aer.100.2.373
- 403 HEAD rejected | https://doi.org/10.1257/jep.29.3.3
- 403 HEAD rejected | https://doi.org/10.1257/jep.34.2.90
- 403 HEAD rejected | https://doi.org/10.3141/2410-12
Potential broken links:
- 404 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/484133/employment_densities_guide_3rd_edition.pdf
- 404 | https://bpf.org.uk/media/3351/bpf-levelling-up-the-logic-of-logistics-report.pdf
- 404 | https://datacentercoalition.org/wp-content/uploads/2023/09/PwC-Economic-Contributions-of-the-US-Data-Center-Industry-2023.pdf
- 404 | https://doi.org/10.1016/S0969-7012(00
- 404 | https://doi.org/10.1016/j.autcon.2021.103868
- 404 | https://doi.org/10.1016/j.enpol.2023.113459
- 404 | https://doi.org/10.1016/j.jtrangeo.2007.08.005
- 404 | https://doi.org/10.1016/j.jtrangeo.2018.12.020
- 404 | https://doi.org/10.1016/j.polgeo.2023.102875
- 404 | https://doi.org/10.1017/S0143814X1600015X
- 404 | https://doi.org/10.1038/s41467-022-34365-3
- 404 | https://doi.org/10.1057/s42214-021-00104-0
- 404 | https://doi.org/10.1061/(ASCE
- 404 | https://doi.org/10.1080/00343400701530882
- 404 | https://doi.org/10.1080/00343404.2020.1762814
- 404 | https://doi.org/10.1080/01446190701401686
- 404 | https://doi.org/10.1080/01944363.2021.1983756
- 404 | https://doi.org/10.1080/10630732.2019.1576466
- 404 | https://doi.org/10.1080/10630732.2021.1985546
- 404 | https://doi.org/10.1080/17421772.2017.1270478
- 404 | https://doi.org/10.1080/17452007.2018.1438015
- 404 | https://doi.org/10.1108/ECAM-04-2018-0151
- 404 | https://doi.org/10.1108/IJPDLM-02-2017-0073
- 404 | https://doi.org/10.1146/annurev-resource-100815-095449
- 404 | https://doi.org/10.1177/0309132517726734
- 404 | https://doi.org/10.1177/0891242410383228
- 404 | https://doi.org/10.1177/0891242418783447
- 404 | https://doi.org/10.1177/0891242419842718
- 404 | https://doi.org/10.1177/0891242420923483
- 404 | https://doi.org/10.1177/08912424221130691
- 404 | https://doi.org/10.1177/08912424231155333
- 404 | https://doi.org/10.1177/1729881419858273
- 404 | https://doi.org/10.1177/25148486211002575
- 404 | https://doi.org/10.1257/jep.34.3.90
- 404 | https://doi.org/10.2139/ssrn.3829731