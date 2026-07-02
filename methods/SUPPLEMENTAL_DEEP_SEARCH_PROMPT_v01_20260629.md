# Supplemental Deep Search Prompt v01

**Date prepared:** 2026-06-29  
**Prepared for:** ChatGPT Deep Research and Gemini Deep Research  
**Manuscript:** *The hard hats behind the algorithm: construction-phase job creation by data centres — a structured evidence synthesis with implications for Australia's build-out*  
**Purpose:** Source-discovery and evidence-gap testing for Ania's comments on off-site MEP/prefabrication, logistics/warehousing comparators, advanced manufacturing/gigafactory comparators, and the proposed "10 jobs/MW versus 1 job/MW" rule.  
**Status:** Prompt and run metadata. Outputs from ChatGPT/Gemini must be treated as source-discovery leads until the underlying sources are retrieved, verified, coded, and reconciled with the manuscript evidence table.

## Run Metadata

The supplemental deep searches were run using:

| Tool | Model/settings recorded by user | Purpose |
|---|---|---|
| ChatGPT Deep Research | ChatGPT 5.5; intelligence = high | Parallel source-discovery run using the prompt below |
| Gemini Deep Research | Gemini Pro 3.1; extended thinking | Parallel source-discovery run using the prompt below |

The returned outputs were saved in the project root as:

| Output file | Notes |
|---|---|
| `deep-research-report.md` | Root-level Markdown output saved 2026-06-29; contains Deep Research-style turn citations |
| `Data Centre Employment Metrics Research.md` | Root-level Markdown output saved 2026-06-29; contains numbered source references |

These outputs should be treated as source-discovery leads only. Any proposed source, metric, or quotation must still be retrieved from the underlying source document and coded into the evidence table before it can support manuscript findings.

## Reproducibility Protocol

Run the same prompt separately in:

1. ChatGPT Deep Research
2. Gemini Deep Research

For each run, save the full output, date, tool/model if visible, and any source list or export. Do not treat generated summaries as evidence. Only source-backed values with retrievable citations, clear units, and direct quotations should be considered for the manuscript.

## Prompt

```text
We are preparing an academic construction-management paper on data-centre job creation. The current evidence base supports direct data-centre construction intensity of about 0.7-2.0 peak workers/MW and operational intensity of about 0.15-0.35 FTE/MW, but a co-author raised a limitation: much data-centre construction employment may occur off-site through MEP prefabrication, modular assemblies, electrical skids, generators, transformers, cooling equipment, and other supply-chain manufacturing. We also need better comparators beyond energy assets, especially logistics/warehousing/fulfilment centres and advanced manufacturing/gigafactories.

Run a targeted evidence search, not a general narrative search.

Research questions:
1. What source-backed evidence exists on off-site prefabrication, modular MEP, equipment manufacturing, or supply-chain labour for data-centre construction?
2. Are there citable metrics for logistics/warehousing/fulfilment-centre construction and operations jobs, such as jobs per floor area, jobs per capex, peak construction workforce, construction job-years, or operational jobs per facility?
3. Are there citable metrics for advanced manufacturing/gigafactory construction and operations jobs in comparable units?
4. Is there any credible source for a "10 jobs/MW during construction versus 1 job/MW during operations" rule for data centres? If yes, identify the source, exact unit, scope, geography, and whether it refers to peak jobs, annual FTE, job-years, direct jobs, total supported jobs, or supply-chain jobs.

Prioritise sources in this order:
- Peer-reviewed papers
- Government or parliamentary reports
- Planning approvals, development agreements, or official economic-development documents
- Credible industry reports with transparent methods
- Company announcements only if they report facility size, capex, phase, and jobs clearly

For every usable source, extract:
- Full citation
- URL/DOI
- Asset type: data centre, warehouse/fulfilment, logistics, advanced manufacturing/gigafactory
- Employment phase: on-site construction, off-site prefabrication, equipment manufacturing, direct operations, indirect/induced supply-chain, enabled economy, community-benefit works
- Metric value
- Unit
- Geography
- Direct vs total-supported scope
- Peak jobs vs annual FTE vs job-years
- Projected vs realised
- Facility size, MW, floor area, capex, or duration if available
- Verbatim source quote
- Page/section location
- Quality/caveat notes

Important boundaries:
- Do not merge on-site construction labour with off-site prefabrication or equipment manufacturing unless the source explicitly does so.
- Do not treat enabled AI/IT jobs as facility-attributable jobs unless a causal source links data-centre entry to local employment change.
- Do not use "10 jobs/MW vs 1 job/MW" unless the source and unit are clear.
- Separate direct jobs, total supported jobs, induced jobs, job-years, and causal effects.

Deliverables:
1. A concise evidence memo with findings and caveats.
2. A table of all usable metric rows.
3. A rejected/weak-source table explaining why each weak source should not be used.
4. A clear recommendation: whether the manuscript can safely expand beyond energy comparators, or whether these topics should remain limitations/future work.

Minimum yield bar:
- To add a new comparator class to the manuscript findings, require at least two citable sources with compatible units and clear job scope.
- If the yield bar is not met, recommend keeping the topic in limitations/future work only.
```

## Output-Handling Rules

When outputs are returned:

1. Save each tool's output as a dated file in the project folder.
2. Extract source leads into a table with URL/DOI, source type, metric, unit, quote, and caveat fields.
3. Retrieve and verify the underlying source documents before adding rows to the manuscript evidence base.
4. Quarantine unsupported generated claims, unverifiable URLs, unclear units, and values that mix direct, indirect, induced, job-year, and causal-effect scopes.
5. Add only source-verified and unit-compatible metrics to the manuscript findings.
