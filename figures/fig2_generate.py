#!/usr/bin/env python3
"""Generate Figure 2: independent source-native employment-intensity facets."""

import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "dc_figures_mplconfig"))

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
from PIL import Image

OUT_DIR = Path(__file__).resolve().parent
STEM = "Figure2_employment_intensity_v19"
MM = 1 / 25.4

C_ACCENT = "#0072B2"  # Okabe-Ito blue
C_DARK = "#2B2B2B"
C_GREY = "#555555"
C_RANGE = "#777777"
C_MUTED = "#555555"
C_RULE = "#B8B8B8"
C_GRID = "#E7E7E7"

FONT_PATH = font_manager.findfont("Arial", fallback_to_default=False)

mpl.rcParams.update({
    "font.family": "Arial",
    "font.sans-serif": ["Arial"],
    "font.size": 8,
    "axes.labelsize": 7.2,
    "axes.titlesize": 8.2,
    "xtick.labelsize": 7,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "axes.linewidth": 0.55,
    "xtick.major.width": 0.5,
    "xtick.major.size": 2.6,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def _style_axis(ax, title, xlim, ticks):
    ax.set_title(title, loc="left", pad=6, color=C_DARK, fontweight="normal")
    ax.set_xlim(*xlim)
    ax.set_xticks(ticks)
    ax.set_yticks([])
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=C_GRID, lw=0.45)
    for spine in ("left", "top", "right"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(C_GREY)
    ax.tick_params(axis="x", colors=C_DARK, pad=2)


def _row_label(ax, y, text):
    ax.text(
        -0.035, y, text,
        transform=ax.get_yaxis_transform(),
        ha="right", va="center", fontsize=7.2, color=C_DARK,
        linespacing=1.12, clip_on=False,
    )


def _range(ax, y, lo, hi, color=C_RANGE):
    ax.plot([lo, hi], [y, y], color=color, lw=1.65,
            solid_capstyle="butt", zorder=2)
    cap = 0.12
    for x in (lo, hi):
        ax.plot([x, x], [y - cap, y + cap], color=color, lw=1.25, zorder=2)


def _marker(ax, x, y, kind, size=6.5):
    if kind == "study":
        ax.plot(x, y, marker="s", ms=size, mfc=C_ACCENT, mec=C_DARK,
                mew=0.65, linestyle="none", zorder=4)
    elif kind == "verified":
        ax.plot(x, y, marker="o", ms=size, mfc=C_DARK, mec=C_DARK,
                mew=0.8, linestyle="none", zorder=4)
    elif kind == "projected":
        ax.plot(x, y, marker="o", ms=size, mfc="white", mec=C_GREY,
                mew=1.25, linestyle="none", zorder=4)
    else:
        raise ValueError(f"Unknown marker kind: {kind}")


def build_figure():
    # 95 mm wide: journal single-column figure. Independent axes are deliberate.
    fig = plt.figure(figsize=(95 * MM, 145 * MM))
    gs = fig.add_gridspec(
        3, 1, height_ratios=[1.0, 1.0, 1.32],
        left=0.405, right=0.965, top=0.91, bottom=0.175, hspace=0.56,
    )
    ax_con = fig.add_subplot(gs[0, 0])
    ax_ops = fig.add_subplot(gs[1, 0])
    ax_eng = fig.add_subplot(gs[2, 0])

    # Facet 1: data-centre construction, independent 0-4 scale.
    _style_axis(
        ax_con, "Data centres — construction\n(peak workers/MW)",
        (0, 4.25), [0, 1, 2, 3, 4],
    )
    ax_con.set_ylim(-0.52, 1.5)
    _range(ax_con, 1.0, 0.7, 2.0)
    _marker(ax_con, 1.0, 1.0, "study", size=6.9)
    _row_label(ax_con, 1.0, "Bottom-up model\n(hyperscale mid)")
    ax_con.text(2.10, 1.0, "1.0  (0.7–2.0)", ha="left", va="center",
                fontsize=7.2, color=C_DARK)

    announcement_points = (1.3, 2.5, 3.6)
    ax_con.plot([min(announcement_points), max(announcement_points)], [0, 0],
                color=C_RANGE, lw=1.1, zorder=2)
    for x in announcement_points:
        _marker(ax_con, x, 0, "projected", size=5.9)
        ax_con.text(x, 0.22, f"{x:.1f}", ha="center", va="bottom",
                    fontsize=7, color=C_DARK)
    _row_label(ax_con, 0, "Project announcements\n(developer, projected)")

    # Facet 2: operations, independent 0-1.3 scale.
    _style_axis(
        ax_ops, "Data centres — operations\n(FTE/MW)",
        (0, 1.30), [0, 0.25, 0.50, 0.75, 1.00, 1.25],
    )
    ax_ops.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%.2g"))
    ax_ops.set_ylim(-0.52, 1.5)
    _range(ax_ops, 1.0, 0.15, 0.35)
    _marker(ax_ops, 0.24, 1.0, "study", size=6.9)
    _row_label(ax_ops, 1.0, "Bottom-up model")
    ax_ops.text(0.39, 1.0, "0.24  (0.15–0.35)", ha="left", va="center",
                fontsize=7.2, color=C_DARK)

    _marker(ax_ops, 1.12, 0, "projected", size=6.3)
    _row_label(ax_ops, 0, "Advocacy national\nestimate (flagged)")
    ax_ops.text(1.08, 0, "1.12\n(≈5× model)", ha="right", va="center",
                fontsize=7, color=C_DARK, linespacing=1.08)

    # Facet 3: energy benchmarks, independent 0-11 scale.
    _style_axis(
        ax_eng, "Energy comparators\n(job-years/MW)",
        (0, 11.25), [0, 2, 4, 6, 8, 10],
    )
    ax_eng.set_ylim(-0.72, 2.52)
    energy_rows = [
        (2.0, "Wind construction factor", 2.65, "2.65"),
        (1.0, "Wind mfg + installation\n(literature median)", 8.1, "8.1"),
        (0.0, "Wind sector model\n(annual installation)", 10.0,
         "≈10 job-years/MW\n(+0.4 O&M*)"),
    ]
    for y, label, value, display in energy_rows:
        _marker(ax_eng, value, y, "verified", size=6.4)
        _row_label(ax_eng, y, label)
        if value < 9:
            # Keep direct labels visibly detached from circular marks at print size.
            ax_eng.text(value + 0.36, y, display, ha="left", va="center",
                        fontsize=7.2, color=C_DARK)
        else:
            ax_eng.text(value - 0.38, y - 0.16, display, ha="right", va="top",
                        fontsize=7.2, color=C_DARK, linespacing=1.08)

    ax_eng.annotate(
        "Not a data-centre\nrule of thumb",
        xy=(10.0, 0), xytext=(4.20, 0.50),
        ha="left", va="center", fontsize=7, color=C_MUTED, linespacing=1.1,
        arrowprops=dict(arrowstyle="-", color=C_RULE, lw=0.65),
        annotation_clip=False,
    )

    # A shared provenance key, with shape carrying the study highlight in B/W.
    handles = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=C_ACCENT,
               markeredgecolor=C_DARK, markeredgewidth=0.65, markersize=6.0,
               label="Study bottom-up estimate"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=C_DARK,
               markeredgecolor=C_DARK, markersize=5.8,
               label="Verified external estimate"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="white",
               markeredgecolor=C_GREY, markeredgewidth=1.2, markersize=5.8,
               label="Projected / advocacy estimate"),
    ]
    leg = fig.legend(
        handles=handles, loc="lower center", bbox_to_anchor=(0.52, 0.025),
        ncol=1, frameon=False, fontsize=7, handletextpad=0.45,
        labelspacing=0.28, borderaxespad=0,
    )
    for text in leg.get_texts():
        text.set_color(C_DARK)

    fig.text(
        0.52, 0.155,
        "* O&M term: operating jobs/MW (different time basis).\n"
        "Independent axes preserve source-native units.\n"
        "Values are not comparable across facets.",
        ha="center", va="top", fontsize=7, color=C_MUTED, style="italic",
        linespacing=1.12,
    )
    return fig


def _save_outputs(fig):
    pdf = OUT_DIR / f"{STEM}.pdf"
    svg = OUT_DIR / f"{STEM}.svg"
    png = OUT_DIR / f"{STEM}.png"
    tiff = OUT_DIR / f"{STEM}.tiff"
    grey = OUT_DIR / f"{STEM}_greyscale_check.png"

    fig.savefig(pdf, dpi=600)
    fig.savefig(svg)
    fig.savefig(png, dpi=600)

    with Image.open(png) as im:
        rgb = im.convert("RGB")
        rgb.save(tiff, format="TIFF", compression="tiff_lzw", dpi=(600, 600))
        rgb.convert("L").save(grey, format="PNG", dpi=(600, 600))

    for path in (pdf, svg, png, tiff, grey):
        print(f"Wrote {path}")


def main():
    print(f"Using Arial font: {FONT_PATH}")
    fig = build_figure()
    _save_outputs(fig)
    plt.close(fig)


if __name__ == "__main__":
    main()
