import matplotlib
import numpy as np
from cycler import cycler
import pickle
import sys

class fig_size:
    textwidth = 234  # full columnwidth
    golden = (np.sqrt(5)+1)/2
    w = textwidth/2-5
    single12       = {'width': w, 'height': w/golden}   # 1/2 width - 5pt (use with side-by-side)
    w = textwidth/3-5
    single13       = {'width': w, 'height': w/golden}   # 1/3 width - 5pt (use with side-by-side-by-side)
    w = textwidth-10
    singlefull     = {'width': w, 'height': w/golden}   # full width - 10pt


def set_figure(fontsize=9, width=251.0, heightratio=None, height=None):
    r"""
    Parameters
    ----------
    fontsize : float
        sets the intended fontsize

    width : float
        sets the intended width in pts

    Notes
    -----
    To set equal to the columnwidth of the article:

    In the tex file 'Column width: \the\columnwidth' will print this size
    alternatively, '\message{Column width: \the\columnwidth}' will print to the log

    \linewidth should be used in place of \columnwidth if the figure is used
    within special enviroments (e.g. minipage)

    https://matplotlib.org/stable/tutorials/introductory/customizing.html
    https://scipy-cookbook.readthedocs.io/items/Matplotlib_LaTeX_Examples.html
    https://tex.stackexchange.com/questions/16942/difference-between-textwidth-linewidth-and-hsize
    """
    fig_width_pt = width
    inches_per_pt = 1.0/72.27               # Convert pt to inch
    fig_width = fig_width_pt*inches_per_pt  # width in inches

    if heightratio is None:
        heightratio = (np.sqrt(5)-1.0)/2.0  # Aesthetic ratio
    if height is None:
        fig_height = fig_width*heightratio      # height in inches
    else:
        fig_height = height*inches_per_pt
    fig_size = [fig_width, fig_height]
    params = {#'backend': 'pdf',
              'text.usetex': True,
              'text.latex.preamble': r"""
                                      \usepackage{amsmath}
                                      """,
              # fonts
              'font.family': 'serif',
              'font.serif': 'Nimbus Roman No9 L',
              # font sizes
              'axes.labelsize': fontsize,
              'font.size': fontsize,
              'axes.titlesize': fontsize,
              'legend.fontsize': fontsize,
              'xtick.labelsize': fontsize,
              'ytick.labelsize': fontsize,
              # figure size
              'figure.figsize': fig_size,
              'figure.constrained_layout.use': True,
              # line styling
              'lines.linewidth': 2,
              # legend
              'legend.frameon': False,
              # spines
              'axes.spines.top': True,
              'axes.spines.right': True,
              # saving
              'savefig.bbox': 'tight',
              'savefig.pad_inches': 1/72,
              # grid
              'grid.color': '0.7',
              'grid.linewidth': 0.2,
              # ticks
              #'xtick.direction': 'inout',
              #'ytick.direction': 'inout',
              'xtick.direction': 'in',
              'ytick.direction': 'in',
              'xtick.major.width':   0.6,
              'xtick.minor.width':   0.4,
              'ytick.major.width':   0.6,
              'ytick.minor.width':   0.4,
              'xtick.major.size':    3.5,
              'xtick.minor.size':    2,
              'ytick.major.size':    3.5,
              'ytick.minor.size':    2,
              # markers
              #'legend.numpoints': 2,
              # colors
              'axes.prop_cycle': cycler('color',
                                        ['tab:blue',
                                         'tab:red',
                                         'tab:green',
                                         'tab:orange',
                                         'tab:purple',
                                         'tab:brown',
                                         'tab:pink',
                                         'tab:gray',
                                         'tab:olive',
                                         'tab:cyan']),
              # axes
              'axes.linewidth': 0.6,
              }
    matplotlib.rcParams.update(params)


def data_load(fname):
    with open(fname, 'rb') as f:
        return pickle.load(f)

def data_save(fname, obj):
    with open(fname, 'wb') as f:
        pickle.dump(obj, f)

def get_pdf_name():
    return '.'.join(sys.argv[0].split('.')[:-1]) + '.pdf'

def save_or_show(**kwargs):
    if '--savefig' in sys.argv:
        matplotlib.pyplot.savefig(get_pdf_name(), **kwargs)
    else:
        matplotlib.pyplot.show()

calligraphic_O = True
Oh = r'\mathcal{O}' if calligraphic_O else 'O'

def bigO(N, t, last_k):
    logN = np.log(N[-last_k:])
    logt = np.log(t[-last_k:])
    return np.polyfit(logN, logt, 1)[0]

def format_bigO_label(label, N, t, last_k):
    exp = bigO(N, t, last_k)
    if abs(round(exp) - exp) < 1e-2:
        exp = str(int(round(exp)))
    else:
        exp = f'{exp:.2f}'

    if exp == '1':
        return label + ', $' + Oh + '(N)$'
    else:
        return label + ', $' + Oh + '(N^{' + exp + '})$'
