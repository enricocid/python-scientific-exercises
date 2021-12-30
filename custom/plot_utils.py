import numpy as np
from pandas import to_datetime


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
