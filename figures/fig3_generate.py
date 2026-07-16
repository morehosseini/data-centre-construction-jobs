#!/usr/bin/env python3
"""Generate Figure 3: the scope-marked data-centre employment cliff."""

import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "dc_figures_mplconfig"))

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
from PIL import Image

OUT_DIR = Path(__file__).resolve().parent
STEM = "Figure3_employment_cliff_v19"
MM = 1 / 25.4

C_ACCENT = "#0072B2"  # Okabe-Ito blue
C_DARK = "#2B2B2B"
C_GREY = "#5B5B5B"
C_RANGE = "#6E6E6E"
C_MUTED = "#555555"
C_RULE = "#B8B8B8"

FONT_PATH = font_manager.findfont("Arial", fallback_to_default=False)

mpl.rcParams.update({
    "font.family": "Arial",
    "font.sans-serif": ["Arial"],
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7.3,
    "ytick.labelsize": 7.2,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "axes.linewidth": 0.55,
    "xtick.major.width": 0.5,
    "ytick.major.width": 0.5,
    "xtick.major.size": 2.8,
    "ytick.major.size": 2.8,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def _style_spines(ax, left=True):
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    if left:
        ax.spines["left"].set_color(C_GREY)
    else:
        ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color(C_GREY)
    ax.tick_params(colors=C_DARK)


def _study_marker(ax, x, y, size=8.2):
    ax.plot(x, y, marker="s", ms=size, mfc=C_ACCENT, mec=C_DARK,
            mew=0.7, linestyle="none", zorder=5)


def _open_marker(ax, x, y, size=6.0):
    ax.plot(x, y, marker="o", ms=size, mfc="white", mec=C_GREY,
            mew=1.25, linestyle="none", zorder=5)


def _vertical_range(ax, x, lo, hi):
    ax.plot([x, x], [lo, hi], color=C_RANGE, lw=1.65, zorder=2)
    cap = 0.035
    for y in (lo, hi):
        ax.plot([x - cap, x + cap], [y, y], color=C_RANGE, lw=1.35, zorder=2)


def _horizontal_range(ax, y, lo, hi):
    ax.plot([lo, hi], [y, y], color=C_RANGE, lw=1.65, zorder=2)
    cap = 0.13
    for x in (lo, hi):
        ax.plot([x, x], [y - cap, y + cap], color=C_RANGE, lw=1.35, zorder=2)


def panel_a(ax):
    x_con, x_ops = 0.0, 1.0
    con, ops = 1.0, 0.24

    # Discrete ranges only: no polygon or interpolation between unlike units.
    _vertical_range(ax, x_con, 0.7, 2.0)
    _vertical_range(ax, x_ops, 0.15, 0.35)
    ax.annotate(
        "", xy=(x_ops, ops), xytext=(x_con, con),
        arrowprops=dict(arrowstyle="->", color=C_ACCENT, lw=2.3,
                        shrinkA=5, shrinkB=5),
        zorder=3,
    )
    _study_marker(ax, x_con, con)
    _study_marker(ax, x_ops, ops)

    ax.text(x_con - 0.07, con, "1.0", ha="right", va="center",
            fontsize=8.2, color=C_DARK)
    ax.text(x_ops + 0.07, ops, "0.24", ha="left", va="center",
            fontsize=8.2, color=C_DARK)
    ax.text(x_con + 0.07, 2.02, "0.7–2.0", ha="left", va="bottom",
            fontsize=7.2, color=C_MUTED)
    ax.text(x_ops + 0.07, 0.37, "0.15–0.35", ha="left", va="bottom",
            fontsize=7.2, color=C_MUTED)

    ax.text(
        0.50, 0.82, "Phase transition\n(no ratio inferred)",
        ha="center", va="bottom", fontsize=7.2, color=C_DARK,
        linespacing=1.08,
    )
    ax.text(
        0.50, 1.02,
        "Source-native endpoints; arrow is a visual link only\n(no interpolation or unit-consistent ratio)",
        transform=ax.transAxes, ha="center", va="bottom",
        fontsize=7, color=C_MUTED, style="italic", linespacing=1.1,
    )

    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(0, 2.18)
    ax.set_xticks([x_con, x_ops])
    ax.set_xticklabels(["Construction (peak)\nworkers/MW", "Operations\nFTE/MW"])
    ax.set_ylabel("Reported intensity per MW\n(source-native units)",
                  color=C_DARK, labelpad=4)
    ax.set_yticks([0, 0.5, 1.0, 1.5, 2.0])
    _style_spines(ax)

    # Developer values are shown in a separate inset so the central cliff is legible.
    inset = ax.inset_axes([0.48, 0.68, 0.48, 0.24])
    inset.set_xlim(0, 4.0)
    inset.set_ylim(-0.35, 0.65)
    inset.plot([1.3, 3.6], [0, 0], color=C_RULE, lw=1.0, zorder=1)
    for value in (1.3, 2.5, 3.6):
        _open_marker(inset, value, 0, size=5.0)
        inset.text(value, 0.22, f"{value:.1f}", ha="center", va="bottom",
                   fontsize=7, color=C_DARK)
    inset.set_title("Developer announcements\n(projected workers/MW)",
                    loc="left", pad=2, fontsize=7, color=C_MUTED,
                    fontweight="normal")
    inset.set_xticks([0, 2, 4])
    inset.set_yticks([])
    inset.tick_params(axis="x", labelsize=7, colors=C_MUTED, pad=1)
    for spine in ("left", "top", "right"):
        inset.spines[spine].set_visible(False)
    inset.spines["bottom"].set_color(C_RULE)

    ax.text(-0.08, 1.075, "a", transform=ax.transAxes,
            fontsize=12, fontweight="bold", color=C_DARK,
            va="bottom", ha="left", clip_on=False)


def panel_b_top(ax):
    y = 0.0
    ops, con = 0.1, 0.5
    _horizontal_range(ax, y, 0.05, 0.17)
    _horizontal_range(ax, y, 0.2, 0.7)
    ax.plot([ops, con], [y, y], color=C_ACCENT, lw=2.3, zorder=3)
    _study_marker(ax, ops, y, size=7.8)
    _study_marker(ax, con, y, size=7.8)

    ax.text(ops, 0.42, "0.1 operations jobs\n(0.05–0.17)",
            ha="center", va="bottom", fontsize=7.2, color=C_DARK,
            linespacing=1.1)
    ax.text(con, 0.42, "0.5 peak construction workers\n(0.2–0.7)",
            ha="center", va="bottom", fontsize=7.2, color=C_DARK,
            linespacing=1.1)

    ax.set_xlim(0, 0.85)
    ax.set_ylim(-0.72, 1.15)
    ax.set_yticks([])
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.2))
    ax.set_xlabel("Direct jobs per US$1M total project investment",
                  color=C_MUTED, labelpad=7)
    ax.set_title(
        "Data centres — sensitivity descriptors (0–0.8 scale)",
        fontsize=7.4, color=C_MUTED, loc="left", pad=5,
        fontweight="normal",
    )
    _style_spines(ax, left=False)
    ax.text(
        0.5, -0.53,
        "Sensitivity only—time bases differ;\nno ratio is inferred.",
        transform=ax.transAxes, ha="center", va="top", fontsize=7,
        color=C_MUTED, style="italic", linespacing=1.08, clip_on=False,
    )
    ax.text(0.0, 1.22, "b", transform=ax.transAxes,
            fontsize=12, fontweight="bold", color=C_DARK,
            va="bottom", ha="left", clip_on=False)


def panel_b_bottom(ax):
    rows = [
        (2.0, "Renewables — total I-O FTE / US$1M spending", 7.49),
        (1.0, "Energy efficiency — total I-O FTE / US$1M spending", 7.72),
        (0.0, "Computer/electronic mfg — total I-O FTE / US$1M spending", 4.74),
    ]
    for y, label, value in rows:
        ax.plot([0, value], [y, y], color=C_RANGE, lw=1.25, zorder=2)
        _open_marker(ax, value, y, size=5.9)
        ax.text(value + 0.16, y, f"{value:.2f}", ha="left", va="center",
                fontsize=7.2, color=C_DARK)
        ax.text(0.10, y + 0.27, label, ha="left", va="bottom",
                fontsize=7, color=C_DARK, clip_on=False)

    ax.set_xlim(0, 8.7)
    ax.set_ylim(-0.55, 2.75)
    ax.set_yticks([])
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(2))
    ax.set_xlabel("Projected total I-O FTE per US$1M spending\n(Garrett-Peltier 2017)",
                  color=C_MUTED, linespacing=1.1)
    ax.set_title(
        "Different scale (0–8.7) and denominator ↓\nContext only—not a ranking",
        fontsize=7.2, color=C_MUTED, loc="left", pad=6,
        fontweight="normal",
    )
    _style_spines(ax, left=False)


def build_figure():
    # 180 mm wide: journal double-column figure.
    fig = plt.figure(figsize=(180 * MM, 112 * MM))
    outer = gridspec.GridSpec(
        1, 2, figure=fig, width_ratios=[1.05, 1.0],
        wspace=0.30, left=0.07, right=0.985, top=0.88, bottom=0.18,
    )
    ax_a = fig.add_subplot(outer[0, 0])
    right = gridspec.GridSpecFromSubplotSpec(
        2, 1, subplot_spec=outer[0, 1],
        height_ratios=[0.88, 1.18], hspace=1.24,
    )
    ax_bt = fig.add_subplot(right[0, 0])
    ax_bb = fig.add_subplot(right[1, 0])

    panel_a(ax_a)
    panel_b_top(ax_bt)
    panel_b_bottom(ax_bb)

    handles = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=C_ACCENT,
               markeredgecolor=C_DARK, markeredgewidth=0.7, markersize=6.0,
               label="Study bottom-up / derived descriptor"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor="white",
               markeredgecolor=C_GREY, markeredgewidth=1.2, markersize=5.8,
               label="Projected / external I-O context"),
    ]
    leg = fig.legend(
        handles=handles, loc="lower center", bbox_to_anchor=(0.52, 0.025),
        ncol=2, frameon=False, fontsize=7, handletextpad=0.4,
        columnspacing=1.2, borderaxespad=0,
    )
    for text in leg.get_texts():
        text.set_color(C_DARK)
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
