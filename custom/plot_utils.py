import numpy as np
from pandas import to_datetime
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


def get_xticks_labels(reports_dates, full=False):
    if full:
        reports_dates.sort_values(inplace=True)
        sel_dates = reports_dates[0::2]
        labels = [t.strftime("%d\n%b") for t in sel_dates]
        ticks = np.arange(0, len(reports_dates), 2)
    else:
        ticks = set([x.strftime("%Y-%m-01") for x in reports_dates])
        ticks = sorted(ticks)
        labels = [to_datetime(t).strftime("%b\n%Y")
                  if (i == 1 or to_datetime(t).strftime("%m") == "01") or full
                  else to_datetime(t).strftime("%b")
                  for i, t in enumerate(ticks)]
        labels[0] = ""
    labels = list(map(str.title, labels))
    return ticks, labels


def plot_1dbox_infinite_walls(b_color="tab:green", w_color="tab:blue"):

    L = 10
    step = L/2

    fig, ax = plt.subplots()

    # remove spines
    for _, spine in ax.spines.items():
        spine.set_visible(False)
    ax.set_yticks([])

    # set plot limits
    ax.set_ylim(0,)
    ax.set_xlim(-L, L*2)
    _, ymax = ax.get_ylim()

    # set ticks labels
    zeros = [0, L]
    zero_labels = dict(zip(zeros, ["0", "L"]))
    xticks = np.arange(-10, L*2+step, step)
    xlabels = ["" if x not in zeros else zero_labels[x] for x in xticks]
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels)

    # draw axis with arrow

    # vertical axis
    arrowprops = dict(arrowstyle="->",
                      linewidth=1.5,
                      color=w_color)
    for zero in zeros:
        ax.annotate("", xy=(zero, ymax), xytext=(zero, 0), arrowprops=arrowprops)

    # abscissa
    arrowprops_ = dict(arrowstyle="<->",
                       linewidth=1,
                       color="k")
    ax.annotate("", xy=(-L, 0), xytext=(L*2, 0), arrowprops=arrowprops_)

    # highlight the box
    ax.axvspan(xmin=0, xmax=L, color=b_color, alpha=0.01)

    # highlight the walls
    ax.axvspan(xmin=L, xmax=L*2, color=w_color, alpha=0.10)
    ax.axvspan(xmin=0, xmax=-L, color=w_color, alpha=0.10)

    # add potential values
    props = dict(fontweight="bold")
    # inside the box
    at = AnchoredText("V=0", frameon=False, loc="lower center", prop=props)
    ax.add_artist(at)

    # walls
    at1 = AnchoredText("V=\u221e", frameon=False, loc="center left", pad=step, prop=props)
    ax.add_artist(at1)

    at2 = AnchoredText("V=\u221e", frameon=False, loc="center right", pad=step, prop=props)
    ax.add_artist(at2)

    fig.tight_layout()
    plt.show()
