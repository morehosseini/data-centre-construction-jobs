# Deep Search Plan: Equal-Investment Job Creation Comparators

Date: 2026-06-30

Manuscript: *The hard hats behind the algorithm: construction-phase job creation by data centres - a structured evidence synthesis with implications for Australia's build-out*

Purpose: convert the latest manuscript weaknesses into a prompt-ready research plan. Another AI assistant should be able to use each work package below to write targeted Deep Research prompts, retrieve source leads, and produce source-verification tables.

## 1. Starting Diagnosis

The latest manuscript already addresses the core story: data centres create real but temporary construction employment and relatively little long-term operational employment. It also handles direct versus total-supported jobs, gross versus net claims, and the employment cliff reasonably well.

The remaining weakness is sharper and more reader-facing:

> If a community receives the same capital investment, for example A$1 billion, how does a data centre compare with alternative built assets in local jobs during construction and after completion?

The manuscript currently promises per-dollar comparison, but the findings mostly foreground per-MW data-centre metrics and a small number of energy-sector comparator metrics. The next research task is therefore not a broad literature review. It is a targeted search for citable, normalisable, source-backed metrics that help answer the equal-investment and opportunity-cost question.

## 2. Rules For Every Deep Search Prompt

Every prompt derived from this plan should include these rules.

### 2.1 Source priority

Prioritise sources in this order:

1. Peer-reviewed empirical papers.
2. Government, parliamentary, audit, or legislative evaluation reports.
3. Planning approvals, environmental assessments, development agreements, community-benefit agreements, and official economic-development documents.
4. Transparent industry reports with methods and tables.
5. Company announcements only when they report capex, facility scale, phase, and jobs clearly.

### 2.2 Evidence boundaries

Do not merge these categories unless the source explicitly does so:

- direct on-site construction labour;
- off-site prefabrication and modular MEP labour;
- upstream equipment manufacturing;
- direct facility operations;
- indirect and induced supply-chain employment;
- causal local employment effects;
- enabled digital-economy or tenant jobs.

Never treat enabled AI, cloud, software, or tenant jobs as facility-attributable data-centre jobs unless a causal study explicitly links data-centre entry to local employment change.

Do not use a "10 jobs/MW construction versus 1 job/MW operations" rule as a data-centre coefficient unless a primary source clearly defines it as data-centre-specific, empirical, and phase-specific. Prior searches indicate that this phrase appears mainly as a policy or tariff threshold, not a measured coefficient.

### 2.3 Required extraction fields

Every usable source lead must be extracted into a table with these fields:

| Field | Required detail |
|---|---|
| Source citation | Author/body, year, title, publisher/journal |
| URL or DOI | Direct link to source |
| Source type | Academic, government, planning, economic development, industry, company |
| Asset class | Data centre, hospital, school, housing, warehouse, fulfilment centre, transport infrastructure, renewable energy, advanced manufacturing, semiconductor, battery gigafactory, other |
| Project or sector | Specific project, portfolio, sector, national program |
| Geography | Country, state, city/region |
| Phase | Construction, operations, lifecycle, local economy, supply chain |
| Metric value | Exact number as reported |
| Unit | Jobs, FTE, peak workers, job-years, jobs per $M, jobs per MW, jobs per sqm, jobs per bed, jobs per dwelling, percent effect |
| Scope | Direct, direct + indirect, direct + indirect + induced, causal net, enabled/context |
| Timing | Peak, annual, construction-period total, person-years, permanent FTE, projected, realised |
| Denominator | Capex, MW, floor area, beds, dwellings, lane-km, GWh, facility count, duration |
| Locality | Whether jobs are local, regional, national, imported, or unclear |
| Verbatim quote | Short quote supporting the metric |
| Page/section | Page, table, figure, section, or line |
| Quality flag | High, medium, low |
| Caveat | Why the metric is or is not comparable |
| Manuscript use | Main finding, bounded comparator, limitation, background only, reject |

### 2.4 Normalisation rules

Normalise only when the source gives enough fields to do so transparently.

Acceptable derived metrics include:

- construction jobs per US$1M or A$1M capex;
- construction job-years per US$1M or A$1M capex;
- operational FTE per US$1M or A$1M capex;
- direct jobs per million square feet or per 100,000 sqm;
- operational FTE per bed, per dwelling, or per facility where relevant;
- jobs per MW only for assets where MW is a meaningful denominator.

Do not collapse peak headcount, annual FTE, construction job-years, permanent operations jobs, indirect/induced jobs, and causal percentage effects into one number.

### 2.5 Minimum yield bars

For a new comparator class to support a manuscript finding:

- at least two citable sources;
- compatible or transparently bridgeable units;
- clear job scope;
- clear phase;
- clear denominator.

If the yield bar is not met, the topic should remain a limitation or future-work item.

## 3. Work Package A - Data-Centre Jobs Per Dollar Of Investment

Priority: P0 - must do.

### Why this matters

The manuscript already states that data-centre jobs should be normalised per MW and per dollar of capex, but the findings do not yet give readers a clear data-centre jobs-per-dollar benchmark. This is the direct bridge to the "same capital investment" question.

### Research objective

Find source-backed metrics that connect data-centre capex to construction jobs, operational jobs, job-years, or local economic employment effects.

### Target evidence

Look for data-centre sources that report at least two of:

- capex or construction spending;
- MW or floor area;
- construction jobs, peak workers, annual construction FTE, or construction job-years;
- operational FTE;
- indirect/induced jobs;
- construction duration;
- local/regional scope.

### Known leads to verify or expand

- Minnesota high-tech data-centre tax exemption evaluation: direct and total jobs per US$1M construction output; leakage of imported servers/electrical equipment.
- Prince William County data-centre fiscal/economic impact analysis: annual construction spending and direct/indirect/induced jobs.
- Morrow County data-centre economic impact analysis: US$8B / 1,000 MW / 8-year buildout / construction FTE / ongoing jobs.
- Pham 2017: typical large data centre, US$215.5M, 1,688 total local construction jobs, 157 local operation-phase jobs.
- Yue and Zeng 2026: US$500M to US$1B facility, 30-100 permanent workers; comparison to a US$500M auto plant.
- Food and Water Watch 2026: 1 job per US$13M capex, if source-verified and caveated.
- PwC / Data Center Coalition economic contribution reports: use only as national input-output context, not as facility direct jobs unless tables are transparent.

### Example search strings

- "data center economic impact construction jobs capital investment jobs per million"
- "data centre economic impact capex construction jobs operations FTE"
- "data center fiscal impact analysis construction spending direct jobs"
- "data center tax exemption evaluation jobs per million construction output"
- "data center jobs per capital investment permanent jobs"
- "data center construction jobs FTE years megawatt capital investment"
- "hyperscale data center capital investment permanent jobs construction jobs economic impact"

### Desired output

A table with all usable data-centre per-dollar or capex-linked rows, plus a short recommendation:

- What range can the manuscript safely state for data-centre construction jobs per US$1M/A$1M?
- What range can it state for permanent operational jobs per US$1M/A$1M?
- Which values are direct only, total-supported, or causal?
- Which values are projected versus realised?
- Which values are local, state, national, or unclear?

### Manuscript use if successful

Add a short paragraph and/or a small table in Section 4.4:

> On a same-investment basis, data centres appear strongest as temporary construction projects and weakest as permanent direct employers. The exact ratio depends on whether the source counts direct site jobs, total-supported jobs, or causal net local effects.

## 4. Work Package B - Warehousing, Logistics, And Fulfilment Centres

Priority: P0 - high-value comparator.

### Why this matters

Fulfilment centres and warehouses are close comparators for local communities because they are large-footprint, industrial-zoned, often automated facilities. They compete with data centres for land, roads, grid connections, and community approval, but often have very different operating employment densities.

### Research objective

Find citable project-level and sector-level metrics for construction and operational jobs in warehouses, logistics hubs, distribution centres, and fulfilment centres, preferably with capex and floor area.

### Target evidence

High-value rows report:

- capex;
- floor area or site area;
- construction jobs or peak workforce;
- permanent operational jobs;
- direct versus indirect scope;
- official source or planning source.

### Known leads to verify or expand

- Amazon Johnston Robotics Fulfillment Center, Rhode Island: facility size, capex, construction-related jobs, full-time associates.
- Amazon Baton Rouge and Shreveport robotics fulfilment centres, Louisiana: capex, footprint, construction jobs, full-time jobs.
- Amazon Carencro and Clarksville fulfilment centres: operations-only direct jobs with floor area/capex.
- UK HCA Employment Density Guide and BPF/Prologis logistics density sources: sqm per FTE, good for operations-density comparators.
- Planning applications or economic impact statements for Amazon, Walmart, Target, DHL, FedEx, Maersk, or major logistics parks.

### Example search strings

- "fulfillment center capital investment construction jobs full time jobs square feet"
- "Amazon fulfillment center construction jobs capital investment square feet"
- "warehouse economic impact construction jobs permanent jobs capex"
- "logistics park planning application employment density FTE square metres"
- "employment density guide storage distribution sqm per FTE"
- "fulfilment centre jobs per square metre employment density"
- "distribution center direct jobs per million investment"

### Desired output

A source table and a normalisation table with:

- construction jobs per US$100M capex;
- operational jobs per US$100M capex;
- operational jobs per million square feet or per 100,000 sqm;
- notes on whether the floor area is gross floor area, foundation footprint, or site area.

### Manuscript use if successful

Use as a bounded comparator:

> Warehousing and fulfilment facilities show that large, automated industrial assets can still carry much higher operational headcounts than data centres, especially when measured by floor area or capex. However, project announcements must be labelled as projected direct jobs, not causal local effects.

## 5. Work Package C - Advanced Manufacturing, Gigafactories, And Semiconductor Fabs

Priority: P0 - high-value comparator.

### Why this matters

Advanced manufacturing facilities can be similarly capital-intensive, power-intensive, and infrastructure-heavy, but they are production workplaces rather than digital infrastructure platforms. They are ideal for showing that capital intensity alone does not determine job creation.

### Research objective

Find direct construction and operational employment metrics for battery gigafactories, EV plants, semiconductor fabs, and similar advanced manufacturing assets, with clear capex and phase boundaries.

### Target evidence

Prioritise sources that separate:

- peak construction headcount;
- construction person-years;
- operational permanent jobs;
- direct versus indirect/induced jobs;
- capex for building versus equipment;
- floor area and production capacity.

### Known leads to verify or expand

- Nevada GOED Tesla expansion board packet: US$1.6B construction, US$2.0B equipment, 9,275 direct construction jobs as person-years, 3,000 direct operating jobs.
- DOE BlueOval SK environmental assessment: peak construction manpower and facility size.
- BlueOval SK official job announcements: operations jobs, construction jobs, project scale.
- Battery-cell production jobs/GWh sources, if they are transparent and recent.
- Semiconductor fab project documents: TSMC Arizona, Intel Ohio, Micron New York, Samsung Taylor, but use carefully because many headline job figures mix direct, indirect, induced, supplier, and regional jobs over long periods.

### Example search strings

- "gigafactory environmental assessment peak construction manpower operational jobs"
- "battery plant capital investment construction jobs permanent jobs square feet"
- "semiconductor fab environmental assessment construction workforce permanent jobs capital investment"
- "Tesla Nevada GOED construction jobs person years operating jobs"
- "BlueOval SK environmental assessment construction manpower jobs"
- "battery cell manufacturing jobs per GWh permanent employment"
- "advanced manufacturing facility jobs per million capital investment"

### Desired output

A table separating:

- construction peak workers;
- construction job-years/person-years;
- permanent operations jobs;
- capex for construction;
- capex for equipment;
- total capex;
- scope caveats.

### Manuscript use if successful

Use to add a stronger equal-investment contrast:

> A capital-intensive production facility can support far more permanent employment than a comparably priced data centre, even when both require large power connections and specialised construction.

## 6. Work Package D - Hospitals, Health Facilities, And Social Infrastructure

Priority: P1 - important if the paper wants a broader community-assets frame.

### Why this matters

Community readers often compare data centres not only with industrial assets but with hospitals, schools, universities, housing, and public infrastructure. These assets may have higher operating employment and clearer local-service benefits.

### Research objective

Find credible construction and operational employment metrics for hospitals and health facilities that include capex and facility scale.

### Target evidence

Look for:

- hospital construction project economic impact reports;
- jobs per construction spend;
- permanent hospital FTE per bed or per floor area;
- planning business cases with capital cost and staffing;
- official health infrastructure project reports;
- Australian and international examples.

### Example search strings

- "hospital construction economic impact jobs capital investment"
- "hospital project capital cost permanent staff jobs construction jobs"
- "health infrastructure business case construction jobs operational jobs"
- "hospital jobs per bed FTE capital cost"
- "new hospital construction jobs permanent jobs economic impact"
- "Australian hospital construction jobs capital investment permanent staff"

### Desired output

At minimum:

- two project-level rows with construction jobs and capex;
- two operations rows with FTE and beds/floor area/capex;
- clear distinction between hospital jobs as facility operations versus wider health-system employment.

### Manuscript use if successful

Use cautiously in a community-opportunity-cost paragraph or supplementary table. Do not force hospitals into the core quantitative figure unless units are compatible.

## 7. Work Package E - Schools, Universities, Housing, And Civic Buildings

Priority: P1 - useful for community opportunity-cost framing, but may be heterogeneous.

### Why this matters

The reader question is about what else a community might get for the same capital investment. Schools, housing, and civic buildings may not be perfect analogues, but they are politically salient alternatives.

### Research objective

Find reliable construction-phase and operations-phase employment metrics for non-industrial built assets.

### Target asset classes

- schools and universities;
- social and affordable housing;
- residential construction;
- public buildings and civic infrastructure;
- mixed-use precincts.

### Example search strings

- "school construction economic impact jobs capital investment"
- "university campus construction jobs permanent jobs capital project"
- "affordable housing construction jobs per million investment"
- "residential construction jobs per million dollars investment"
- "housing construction employment multiplier jobs per million"
- "public building construction jobs per million investment"
- "input output construction jobs per million building investment Australia"

### Desired output

Separate:

- construction jobs per US$1M/A$1M;
- permanent operational jobs, if any;
- induced/community-service benefits if the source reports them;
- whether jobs are direct construction jobs or input-output total jobs.

### Manuscript use if successful

Likely a short discussion paragraph or supplementary comparator table:

> Broader community assets are not functional substitutes for data centres, but they clarify the opportunity-cost question because the same capital envelope can create different mixes of construction jobs, permanent jobs, and public-service value.

## 8. Work Package F - Renewable Energy, Grid, And Energy-Efficiency Comparators

Priority: P1 - update and contextualise existing comparator evidence.

### Why this matters

The manuscript already uses energy-sector comparators. The next search should update or triangulate those numbers with more recent sources and Australian context.

### Research objective

Find recent and citable jobs-per-dollar, jobs-per-MW, job-years, and O&M employment estimates for renewable energy, grid infrastructure, storage, transmission, and energy efficiency.

### Known sources to extend

- Green versus brown jobs per US$1M spending.
- Wei et al. renewable job-years per MW/GWh.
- NREL JEDI model documentation and project outputs.
- IRENA renewable energy and jobs reports.
- Clean Energy Council or Australian government workforce reports.
- Transmission/grid construction labour studies.

### Example search strings

- "renewable energy jobs per million investment construction operations"
- "wind farm construction jobs per MW O&M jobs per MW"
- "solar farm construction jobs per MW operations jobs per MW"
- "battery storage construction jobs per MW MWh operations jobs"
- "transmission line construction jobs per million investment"
- "Australia renewable energy workforce jobs per MW construction"
- "energy efficiency jobs per million investment input output"

### Desired output

A table separating:

- construction job-years per MW;
- O&M jobs per MW;
- jobs per US$1M/A$1M investment;
- direct versus total-supported jobs;
- projected versus realised.

### Manuscript use if successful

Use to strengthen or update the existing energy comparator paragraph, not to replace the broader logistics/manufacturing comparator search.

## 9. Work Package G - Localness, Labour Leakage, And Imported/Specialist Workforce

Priority: P0 - needed for the "local community jobs" part of the reader question.

### Why this matters

The manuscript says local jobs matter, but it does not yet quantify how much construction labour, equipment labour, or operational labour is genuinely local. This is central to community benefit.

### Research objective

Find evidence on the local share of data-centre jobs and comparator-asset jobs, including imported specialist labour, local-hire requirements, local procurement, apprenticeships, and workforce development commitments.

### Target evidence

Search for:

- local-hire or community-benefit clauses in data-centre approvals;
- reports on imported construction labour for data centres;
- apprenticeship and training commitments tied to data centres;
- local procurement or local-content requirements;
- planning reports that separate local, regional, and non-local jobs;
- evidence on off-site equipment and manufacturing leakage.

### Known leads

- Mayer 2023 on temporality and mobile construction labour.
- Minnesota evaluation on imported servers/electrical equipment leakage.
- Commonwealth March 2026 expectations of data centres and AI infrastructure developers.
- NSW inquiry submissions on skills and workforce.
- Local development agreements for US data-centre projects.
- Community-benefit agreements for large infrastructure, hospitals, warehouses, or manufacturing projects.

### Example search strings

- "data center local hire agreement construction jobs"
- "data centre community benefit agreement local workforce"
- "data center construction workforce local imported labour"
- "data centre apprenticeships local workforce participation requirements"
- "data center economic impact local jobs leakage imported equipment"
- "data center development agreement local hiring training"
- "local content requirements data center construction"

### Desired output

A table with:

- local share if reported;
- local-hire commitments;
- apprenticeship/training commitments;
- geography;
- whether the source reports actual outcomes or only commitments;
- whether requirements are binding, voluntary, or aspirational.

### Manuscript use if successful

Add a short sentence to the discussion:

> The employment value to host communities depends not only on the headline number of jobs, but on the share of work captured locally rather than by imported specialist labour, off-site manufacturers, or non-local supply chains.

## 10. Work Package H - Incentives, Approvals, And Opportunity Cost Per Job

Priority: P0 - needed for the "community opportunity cost" weakness.

### Why this matters

Readers want to know whether land, power, water, tax incentives, approvals, and community concessions buy many jobs or few jobs. This work package should support a careful opportunity-cost paragraph.

### Research objective

Find evidence on public incentives, tax abatements, infrastructure concessions, grid/power commitments, water use, land use, and cost per job for data centres and comparator assets.

### Target evidence

Look for:

- incentive per job;
- tax abatement per permanent job;
- public infrastructure cost per job;
- power capacity allocated per job;
- water/land footprint per job;
- fiscal cost-benefit studies;
- subsidy evaluations;
- ex-post audits of promised versus realised jobs.

### Known leads

- Virginia JLARC data-centre reports.
- Good Jobs First data-centre subsidy reports.
- Food and Water Watch 2026.
- Gargano and Giacoletti 2025, data-centre incentives.
- Minnesota tax-exemption evaluation.
- Local government fiscal impact reports.
- State economic-development incentive agreements.

### Example search strings

- "data center tax incentives cost per job"
- "data centre subsidy permanent jobs cost per job"
- "data center fiscal impact tax abatement jobs"
- "data center promised jobs realised jobs incentives"
- "data center power capacity jobs per megawatt public incentives"
- "data center water use jobs per acre"
- "economic development incentives data centers employment outcomes"
- "data center tax exemption evaluation jobs"

### Desired output

For each source:

- incentive amount or public cost;
- jobs promised;
- jobs realised, if available;
- phase: construction, operations, direct, total-supported;
- cost per permanent direct job;
- fiscal revenue/cost;
- power/water/land constraints, if reported;
- source caveats.

### Manuscript use if successful

Add an opportunity-cost paragraph:

> For host governments, the relevant question is not only whether data centres create jobs, but whether the jobs created justify scarce land, grid capacity, water allocation, and public incentives compared with other assets. The evidence suggests that this test is strongest for temporary construction and weakest for permanent direct employment, unless approvals are tied to local-content, training, and transparent reporting requirements.

## 11. Work Package I - Off-Site Prefabrication, Modular MEP, And Equipment Manufacturing

Priority: P1 - important limitation, probably not a headline quantified finding.

### Why this matters

Current site-based data-centre employment estimates may undercount factory labour, equipment manufacturing, and modular assembly. However, prior searches found little project-level quantification.

### Research objective

Find whether any newer or more specific sources quantify off-site prefabrication, modular MEP, power skids, cooling systems, transformer/generator manufacturing, or electrical room assembly for data-centre projects.

### Target evidence

High-value evidence would report:

- number of workers in off-site assembly tied to a data-centre project;
- labour-hour split between site and factory;
- percentage of MEP work shifted off site;
- supplier jobs attributable to a data-centre order;
- factory capacity and data-centre module output;
- geographic location of off-site work.

### Example search strings

- "data center prefabricated modular MEP labour hours"
- "data centre power skid manufacturing jobs"
- "data center modular construction offsite labour employment"
- "data centre prefabricated electrical rooms factory workforce"
- "data center cooling plant prefabrication manufacturing jobs"
- "data center transformer generator supply chain employment"
- "data centre offsite construction labour shift factory"

### Desired output

Classify each source as:

- quantified project-level evidence;
- quantified but not data-centre-specific;
- qualitative data-centre evidence;
- general modular construction workforce evidence;
- reject.

### Manuscript use if successful

Only add quantified findings if project-level or data-centre-specific units are clear. Otherwise, strengthen the limitation:

> Site-based and local-impact estimates likely undercount off-site prefabrication and upstream equipment manufacturing, but the current literature does not yet support a transferable data-centre-specific coefficient.

## 12. Work Package J - Realised Versus Projected Jobs

Priority: P1 - supports credibility and protects against announcement bias.

### Why this matters

Developer and economic-development announcements can overstate local job creation. The manuscript already distinguishes projected versus realised, but the equal-investment comparison will be stronger if it includes outcome verification.

### Research objective

Find studies or audits comparing promised and realised jobs for data centres and comparator assets.

### Target evidence

Search for:

- ex-post audits;
- incentive compliance reports;
- job creation verification reports;
- development agreement compliance records;
- realised employment after facility opening;
- promised versus actual jobs.

### Example search strings

- "data center promised jobs actual jobs audit"
- "data centre incentive compliance jobs created"
- "data center development agreement job creation compliance"
- "economic development project promised versus actual jobs data center"
- "fulfillment center promised jobs actual jobs"
- "gigafactory promised jobs actual jobs audit"
- "state incentive compliance report data center jobs"

### Desired output

A table with:

- promised jobs;
- realised jobs;
- time elapsed;
- direct versus total scope;
- enforcement mechanism;
- source reliability.

### Manuscript use if successful

Use to strengthen methods and discussion:

> Project announcements should be treated as upper-bound or projected values unless compliance or outcome data confirm realised employment.

## 13. Cross-Asset Comparison Framework To Build After Searches

After the searches, the assistant should build a comparison table with these columns:

| Asset class | Construction metric | Operations metric | Denominator | Direct/total scope | Locality evidence | Best use in manuscript |
|---|---|---|---|---|---|---|
| Data centre | Peak workers/MW; jobs per $M; job-years if available | FTE/MW; FTE per $M | MW, capex | Direct and total separate | Weak to medium | Core finding |
| Fulfilment/warehouse | Construction jobs per capex/floor area | FTE per capex/floor area | Capex, floor area | Usually direct/projected | Medium if official project source | Bounded comparator |
| Advanced manufacturing | Peak workers, person-years per capex | Direct permanent jobs per capex | Capex, floor area, output capacity | Direct and total separate | Medium | Bounded comparator |
| Renewable/grid/energy efficiency | Job-years/MW, jobs/$M | O&M/MW | MW, GWh, capex | Often total-supported | Variable | Existing energy comparator |
| Hospitals/social infrastructure | Construction jobs/$M | FTE/bed, FTE/capex | Capex, beds, floor area | Direct and total separate | Potentially strong | Community opportunity-cost context |
| Schools/housing/civic assets | Construction jobs/$M | Asset-specific operations | Capex, dwellings, floor area | Often input-output | Variable | Supplementary context |

## 14. Final Deliverables Expected From The Research Phase

Each Deep Research run should produce:

1. Evidence memo: short answer-first summary.
2. Usable source table: all candidate source-backed metrics.
3. Weak/rejected source table: unclear units, secondary summaries, unsupported claims, mixed scopes.
4. Source-verification queue: primary PDFs/pages to retrieve and check.
5. Manuscript-use recommendation: main finding, bounded comparator, limitation, or reject.
6. Suggested manuscript text: 1-2 paragraphs only after source verification.

## 15. Decision Rules For Manuscript Integration

Use the new evidence only if it improves the paper without weakening its boundary discipline.

Add as a main finding when:

- the source is primary or near-primary;
- units and phase are clear;
- at least two sources support the comparator class;
- direct/total and projected/realised status are visible.

Add as a bounded comparator when:

- sources are official but project-specific;
- units differ but can be shown side by side;
- the claim is illustrative, not a universal coefficient.

Keep as limitation/future work when:

- the evidence is qualitative only;
- source scope is unclear;
- the source mixes direct, indirect, induced, and enabled jobs;
- denominator is missing;
- only one source exists.

Reject when:

- the source is a generated summary with no primary citation;
- the number is a policy threshold rather than observed or modelled employment;
- job type, phase, geography, or denominator cannot be identified;
- the source supports enabled digital-economy jobs rather than facility-attributable jobs.

## 16. Recommended Prompt Sequence

Run the prompt sequence in this order:

1. Data-centre jobs per dollar and capex-linked metrics.
2. Warehousing, logistics, and fulfilment comparators.
3. Advanced manufacturing, gigafactory, and semiconductor comparators.
4. Localness, labour leakage, and imported/specialist workforce.
5. Incentives, approvals, and opportunity cost per job.
6. Hospitals and social infrastructure comparators.
7. Schools, housing, and civic buildings comparators.
8. Renewable energy, grid, and energy-efficiency update.
9. Off-site prefabrication, modular MEP, and equipment manufacturing.
10. Realised versus projected jobs.

The first five are the highest priority because they directly repair the current manuscript weakness: the lack of a concrete equal-investment, local-community comparison.
