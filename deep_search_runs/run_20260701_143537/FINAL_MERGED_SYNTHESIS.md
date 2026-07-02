Here is the Final Evidence Dossier synthesizing the multi-slice systematic search on data-centre construction and operations jobs per million dollars of capital expenditure (capex).

### 1) Executive Summary
The rapid global expansion of hyperscale data centres, driven by cloud computing and artificial intelligence (AI), has triggered an unprecedented capital expenditure (capex) supercycle. However, evaluating the local economic development value of these assets reveals a profound structural paradox: massive upfront capital investment yields a severe "employment cliff." Data centres generate highly concentrated, transient construction employment, followed by minimal permanent operational headcount. 

A systematic review of ex-post governmental audits, econometric evaluations, and project-level impact assessments demonstrates that traditional input-output (I-O) economic models frequently inflate local employment multipliers by using "Total Capex" as the denominator. This fails to account for the "leaky bucket" effect, where up to 70–80% of capital is exported to procure specialized, imported IT hardware and cooling systems, bypassing the local economy entirely. When accurately normalized against isolated "Construction Output," data centres yield approximately 3.93 direct construction jobs per US$1 million. However, during the operational phase, they yield less than 0.1 direct permanent jobs per US$1 million in total capex. When benchmarked on an equal-investment basis against alternative built assets—such as advanced semiconductor manufacturing, battery gigafactories, and automated logistics hubs—data centres underperform in permanent job creation by factors ranging from 10x to 50x, framing them primarily as fiscal (tax-generating) assets rather than employment engines.

### 2) Assessment of the Current Search Approach and its Coverage
The current search approach successfully transitioned from an initial reliance on ex-ante predictive modelling (e.g., consultant fiscal impact studies) to high-fidelity ex-post empirical audits. A rigorous 2-hop structural snowballing protocol expanded the evidence base into regional science, construction economics, and state-level enterprise zone audits (e.g., Texas, Georgia, Iowa, Oregon). 

**Coverage Strengths:** The search effectively captured the methodological divide between industry advocacy (which conflates peak headcount with annualized FTEs) and causal academic literature (e.g., Difference-in-Differences models showing zero net county-level job growth). It also successfully established cross-asset comparative baselines (gigafactories, hospitals, logistics).
**Coverage Limitations:** The highest-quality empirical data remains hyper-concentrated in specific US jurisdictions (Virginia, Minnesota, Oregon, Texas). Despite a projected A$26 billion pipeline in Australia, APAC and European data rely heavily on ex-ante Environmental Impact Statements (EIS) rather than ex-post realizations. Furthermore, peer-reviewed causal studies isolating the exact local employment effects of data centre entry remain sparse compared to grey-literature audits.

### 3) Final Scopus and Web of Science Query Strings
*To be run separately and de-duplicated.*

**Batch 1: govt_evaluations**
*   **Scopus:** `TITLE-ABS-KEY(("data center" OR "data centre" OR "hyperscale") AND ("ex-post audit" OR "tax exemption" OR "fiscal impact" OR "subsidy"))`
*   **WoS:** `TS=(("data center" OR "data centre" OR "hyperscale") AND ("ex-post audit" OR "tax exemption" OR "fiscal impact" OR "subsidy"))`

**Batch 2: county_impact**
*   **Scopus:** `TITLE-ABS-KEY(("data center" OR "data centre") AND ("county-level" OR "local economic impact" OR "spillover" OR "difference-in-differences"))`
*   **WoS:** `TS=(("data center" OR "data centre") AND ("county-level" OR "local economic impact" OR "spillover" OR "difference-in-differences"))`

**Batch 3: project_io**
*   **Scopus:** `TITLE-ABS-KEY(("data center" OR "data centre" OR "gigafactory" OR "semiconductor fab") AND ("input-output" OR "IMPLAN" OR "RIMS II" OR "multiplier" OR "leakage"))`
*   **WoS:** `TS=(("data center" OR "data centre" OR "gigafactory" OR "semiconductor fab") AND ("input-output" OR "IMPLAN" OR "RIMS II" OR "multiplier" OR "leakage"))`

**Batch 4: normalisation_methods**
*   **Scopus:** `TITLE-ABS-KEY(("capital expenditure" OR "capex" OR "construction output" OR "capital investment") AND ("jobs per million" OR "job-years" OR "FTE" OR "employment density"))`
*   **WoS:** `TS=(("capital expenditure" OR "capex" OR "construction output" OR "capital investment") AND ("jobs per million" OR "job-years" OR "FTE" OR "employment density"))`

### 4) Grey-Literature Search Strings by Category
*   **Ex-Post Government Audits:** `filetype:pdf ("data center" OR "data centre") ("tax exemption" OR "audit" OR "performance review") "jobs" "capital investment" site:.gov`
*   **EIS / SSD Applications (APAC Focus):** `filetype:pdf "State Significant Development" OR "Environmental Impact Statement" "data centre" "Capital Investment Value" "jobs" site:.au`
*   **Comparative Asset Evaluations:** `filetype:pdf ("gigafactory" OR "fulfillment center" OR "semiconductor fab") "economic impact" "direct jobs" "capex" OR "capital expenditure"`

### 5) Inclusion and Exclusion Criteria
**Inclusion Criteria:**
1.  **Explicit Denominators:** Sources must report a specific financial denominator (e.g., US$1M capex, A$100M construction spend) and a specific employment numerator (e.g., direct FTE, job-years).
2.  **Phase Separation:** Sources must explicitly separate temporary construction phase impacts from permanent operational phase impacts.
3.  **Recency:** Prioritize primary empirical literature published between 2015 and 2026 to account for modern AI workloads, liquid cooling costs, and server densification.

**Exclusion Criteria:**
1.  **Capacity-Based Heuristics:** Exclude sources relying solely on "jobs per megawatt (MW)" without explicit financial normalization, as rising capital costs per MW render this heuristic obsolete.
2.  **Conflated Timelines:** Reject sources conflating transient peak construction headcount with annualized operational FTEs without transparent conversion into job-years.
3.  **Tenant Job Conflation:** Reject sources claiming enabled digital-economy jobs (e.g., remote cloud developers) as direct facility jobs.
4.  **Unadjusted Total Capex Multipliers:** Exclude predictive models applying generic regional multipliers to "Total Capex" without accounting for IT hardware leakage (unless used specifically to demonstrate the leakage flaw).

### 6) Master Evidence Table

| Source Citation | Asset Class | Phase | Metric Value | Unit | Denominator | Scope | Evidence Quality / Risk of Bias |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Minnesota LBO (2026) | Data Centre | Construction | 3.93 | Jobs | $1M (Const. Output) | Direct | **High / Low Bias:** Ex-post tax audit isolating physical construction spend from IT leakage. |
| PFM Consulting (2022) | Data Centre | Construction | 5.33 | Job-years | $1M (Const. Spend) | Direct | **High / Low Bias:** Ex-ante model using prototypical facility framework. |
| Illinois DCEO (2023) | Data Centre | Operations | 0.1 | FTE | $1M (Total Capex) | Direct | **High / Low Bias:** Ex-post realized data ($4B capex yielding ~400 jobs). |
| Food & Water Watch (2026) | Data Centre | Operations | 1 | FTE | $54M (Total Capex) | Direct | **Moderate / Moderate Bias:** Retrospective analysis of VA data; highlights extreme capital intensity. |
| Slattery & Zidar (2020) | Data Centre | Operations | >$1,000,000 | Subsidy | Per Job Created | Direct | **High / Low Bias:** Peer-reviewed econometric evaluation of state incentives. |
| Nevada GOED (2023) | Gigafactory | Operations | 3.1 | FTE | $1M (Total Capex) | Direct | **High / Low Bias:** Ex-post audit of Tesla Gigafactory; perfect comparator to DC abatements. |
| SIA / Oxford Econ (2021) | Semiconductor | Operations | 2.74 | FTE | $1M (Total Capex) | Direct | **Moderate / Medium Bias:** Industry report with transparent methodology. |
| Amazon Amarillo (2022) | Logistics | Operations | 5.0 | FTE | $1M (Total Capex) | Direct | **High / Low Bias:** Ex-post data for automated fulfillment centre. |
| NREL JEDI Model (2023) | Solar PV | Construction | 2.5 - 3.0 | Job-years | $1M (Total Capex) | Direct | **High / Low Bias:** Authoritative baseline for renewable energy construction. |
| Pham / US Chamber (2017) | Data Centre | Construction | 1,688 | Headcount | $215.5M (Total Capex) | Total | **Low / High Bias:** Conflates peak headcount with FTEs; fails to adjust for IT leakage. |

### 7) Methods / Approaches Synthesis
Evaluating data-centre employment requires navigating three primary methodological frameworks:
*   **Static Input-Output (I-O) Models (IMPLAN, RIMS II):** The industry standard for ex-ante projections. While excellent for isolating discrete construction spending, they assume infinite labour supply and zero price elasticity. Crucially, if analysts do not manually adjust Regional Purchase Coefficients (RPCs) to account for the "leaky bucket" of imported IT hardware (servers, GPUs, switchgear), these models falsely project massive local manufacturing booms.
*   **Computable General Equilibrium (CGE) Models (REMI):** Dynamic models that capture market constraints, wage inflation, and labour migration. They are superior for evaluating the secondary effects of massive data-centre energy loads on regional electricity prices but suffer from "black box" algorithmic complexity.
*   **Ex-Post Econometric Evaluation (Difference-in-Differences):** The gold standard for causal inference. By comparing treated counties against control groups using time-series panel data (e.g., QCEW), DiD models eliminate projection bias and capture the absolute reality of leakages. Recent DiD studies show data centres generate zero net job growth in non-metropolitan counties.

### 8) Applications, Outcomes, and Adoption Synthesis
*   **Construction Phase (Temporary Bonanza):** Data centres are massive economic engines during construction. When normalized against *isolated construction output* (excluding IT hardware), they generate approximately 3.93 direct construction jobs per US$1 million. However, due to severe shortages in specialized mechanical, electrical, and plumbing (MEP) labour, much of this workforce is imported, causing wage-spending multipliers to leak out of the host community.
*   **Operational Phase (The Employment Cliff):** Upon commissioning, human labour is actively engineered out. A typical 250,000 sq ft facility employs roughly 50 FTEs (1 job per 5,000 sq ft). Normalized against total capex, data centres yield less than 0.1 direct operational jobs per US$1 million.
*   **Cross-Asset Comparators:** On an equal-investment basis, data centres vastly underperform alternative assets. Advanced semiconductor fabs yield ~2.74 jobs/$1M; battery gigafactories yield ~0.86 to 3.1 jobs/$1M; and automated logistics hubs yield ~5.0 jobs/$1M. 

### 9) Quality, Governance, Risk, and Limitations Synthesis
The evidence base is highly stratified by sponsor bias. Industry-commissioned reports (e.g., U.S. Chamber of Commerce, Data Center Coalition) present a high risk of bias by conflating transient peak headcount with annualized FTEs and applying local multipliers to total capex (including imported servers). Conversely, ex-post government audits (Minnesota, Virginia, Texas, Georgia) present a low risk of bias, utilizing verified corporate tax filings. 

A major governance shift is occurring: municipalities are increasingly recognizing that data centres are *fiscal* assets, not *employment* assets. The policy trade-off explicitly weighs exceptionally high local commercial property tax yields against severe electrical grid strain and the opportunity cost of sterilizing high-value industrial land that could otherwise host high-employment manufacturing.

### 10) Screening and Extraction Template
For future systematic screening, the following extraction template should be utilized:

| Field | Description | Example |
| :--- | :--- | :--- |
| **Source Citation** | Author, Year, Title, Publisher/Journal | Minnesota LBO (2026) |
| **Asset Class** | Data Centre, Gigafactory, Logistics, Hospital | Data Centre |
| **Phase** | Construction, Operations, Lifecycle | Construction |
| **Metric Value** | The numerical employment yield | 3.93 |
| **Unit** | FTE, Job-years, Peak Headcount | Job-years |
| **Denominator** | Financial or spatial boundary | $1M Construction Output |
| **Scope** | Direct, Indirect, Induced, Total Supported | Direct |
| **Leakage Adjusted?** | Yes/No (Did they remove IT hardware?) | Yes |
| **Risk of Bias** | Low, Moderate, High (with justification) | Low (Ex-post tax audit) |

### 11) Research Gaps and Next Steps
Based on the synthesis, the following Work Packages (WP) address critical evidence gaps:
*   **WP A (Data Centre Capex Metrics):** Conduct targeted searches for ex-post job realizations in the APAC and European markets. Specifically, extract data from Australian State Significant Development (SSD) applications to establish non-US capex-to-jobs ratios. Further quantify the exact percentage split of IT hardware capital leakage in modern liquid-cooled AI facilities.
*   **WP B (Logistics & Fulfillment):** Systematically extract planning applications for modern, automated fulfillment centres (e.g., Amazon Robotics hubs) to establish firm comparative density metrics (capex and floor area vs. direct operational FTEs).
*   **WP C (Advanced Manufacturing):** Aggregate project-level economic evaluations of semiconductor fabs (e.g., CHIPS Act funded projects) and battery gigafactories, ensuring a clear separation of construction vs. operational jobs against a total capex denominator.

### 12) Datasets & Data Sources Table

| Name | Repository | DOI/URL | Coverage | License | Suitability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Aterio US Data Center Locations and Power Demand | Databricks Marketplace | n/a | US | Commercial | **High** (Crucial for mapping spatial density and power draw against local economic data) |
| StateIO - Open Source Economic Input-Output Models for the 50 States | SAGE / Journal | 10.1177/01600176221145874 | US | Open Source | **High** (Essential for verifying regional multipliers and adjusting for capital leakage) |
| GLAM – The Global Impact Assessment Method – BETA | Zenodo | 10.5281/zenodo.20630461 | Global | cc-by-4.0 | **Medium** (Useful for broader macroeconomic impact benchmarking) |
| Extracted Data From: HUD Socio-Demographic Data Dashboards | Zenodo | 10.5281/zenodo.21084725 | US | cc-zero | **Medium** (Useful for DiD control group matching at the county level) |
| Comparative Socio-Economic, Public Policy, and Political Data, 1900-1960 | ICPSR | 10.3886/icpsr00034 | Global | Custom | **Low** (Historical data predates digital infrastructure) |
| MaterialCities data: mapping building material stocks and floor area | Zenodo | 10.5281/zenodo.18327825 | Global | cc-by-sa-4.0 | **Low** (Focuses on material stocks rather than capex/employment economics) |
| Building part specific embodied carbon dataset for residential buildings | Zenodo | 10.5281/zenodo.21024220 | Finland | cc-by-4.0 | **Low** (Irrelevant asset class and focus) |

### 13) BibTeX Appendix
```bibtex
@article{slattery2015quantitative,
  title={A Quantitative Analysis of Subsidy Competition in the U.S.},
  author={Slattery, C. and Zidar, O.},
  journal={National Bureau of Economic Research},
  year={2015},
  doi={10.3386/w20975}
}

@article{moretti2010local,
  title={Local Multipliers},
  author={Moretti, Enrico},
  journal={American Economic Review},
  volume={100},
  number={2},
  pages={373--377},
  year={2010}
}

@article{wei2010green,
  title={Putting renewables and energy efficiency to work: How many jobs can the clean energy industry generate in the US?},
  author={Wei, Max and Patadia, Shana and Kammen, Daniel M},
  journal={Energy Policy},
  volume={38},
  number={2},
  pages={919--931},
  year={2010},
  doi={10.1016/j.enpol.2009.10.049}
}

@article{jones2021environmental,
  title={The environmental footprint of data centers in the United States},
  author={Jones, N. and others},
  journal={Environmental Research Letters},
  year={2021},
  doi={10.1088/1748-9326/abfba1}
}

@article{masanet2020recalibrating,
  title={Recalibrating global data center energy-use estimates},
  author={Masanet, Eric and Shehabi, Arman and Lei, Nuoa and Smith, Sarah and Koomey, Jonathan},
  journal={Science},
  volume={367},
  number={6481},
  pages={984--986},
  year={2020},
  doi={10.1126/science.aba3758}
}

@article{pickren2018jobless,
  title={The global assemblage of digital flow: Critical data logistics},
  author={Pickren, Graham},
  journal={Geoforum},
  year={2018}
}

@article{dong2017examining,
  title={Examining industrial structure changes and corresponding carbon emission reduction effect by combining input-output analysis and social network analysis},
  author={Dong, F. and others},
  journal={Journal of Cleaner Production},
  year={2017},
  doi={10.1016/j.jclepro.2017.05.200}
}

@article{bess2022stateio,
  title={StateIO - Open Source Economic Input-Output Models for the 50 States of the United States of America},
  author={Bess, R. and others},
  journal={International Regional Science Review},
  year={2022},
  doi={10.1177/01600176221145874}
}
```

***

```json
{
  "search_audit_v1": {
    "date": "2026-06-30",
    "primary_objective": "Retrieve source-backed, normalizable metrics for equal-investment job creation comparators (Data Centres vs. Warehousing vs. Advanced Manufacturing).",
    "priority_work_packages": ["WP_A_Data_Centre_Capex_Metrics", "WP_B_Logistics_Fulfillment", "WP_C_Advanced_Manufacturing"],
    "strict_exclusion_criteria": [
      "Metrics conflating peak headcount with annualized FTE without transparent conversion",
      "Enabled digital-economy/tenant jobs claimed as direct facility jobs",
      "Jobs per MW heuristics not backed by empirical phase-specific data",
      "Total capex multipliers failing to account for IT hardware leakage (unless used to demonstrate the leakage flaw)"
    ],
    "required_extraction_fields": [
      "Source citation",
      "Asset class",
      "Phase (Construction/Operations)",
      "Metric value",
      "Unit (FTE, Job-years, Peak)",
      "Denominator (Capex $M, Sqm)",
      "Scope (Direct/Indirect/Induced)"
    ],
    "target_source_hierarchy": [
      "1. Peer-reviewed empirical papers",
      "2. Government/legislative audits",
      "3. Planning approvals/EIS",
      "4. Transparent industry reports"
    ]
  }
}
```
