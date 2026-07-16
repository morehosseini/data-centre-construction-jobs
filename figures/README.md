# Figures

| Manuscript | Files |
|------------|--------|
| **Figure 1** | `Figure1_evidence_synthesis_procedure.{png,pdf}` — evidence-synthesis procedure |
| **Figure 2** | `Figure2_employment_intensity_v19.{pdf,svg,png,tiff}` — employment intensity by evidence family |
| **Figure 3** | `Figure3_employment_cliff_v19.{pdf,svg,png,tiff}` — employment cliff (per-MW and per-dollar) |

## Regenerate Figures 2–3

```bash
pip install matplotlib
python3 fig2_generate.py
python3 fig3_generate.py
```

Values are taken from the manuscript evidence summary (Table 2 / related results sections).
