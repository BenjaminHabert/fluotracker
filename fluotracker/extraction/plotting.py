import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable


def set_defaults():
    """Set default parameters for plotting in a notebook."""
    sns.set()
    plt.rcParams['savefig.dpi'] = 120
    plt.rcParams['figure.dpi'] = 120
    plt.rcParams['figure.figsize'] = (8, 4)
    plt.rcParams['figure.facecolor'] = "white"
    plt.rcParams['savefig.facecolor'] = "white"

    return plt, sns


def plot_frames_from_movie(frames, name):
    plt, sns = set_defaults()

    indexes = [0, int(len(frames) / 2), len(frames) - 1]
    frames_to_plot = [frames[i] for i in indexes]
    n_frames = len(frames_to_plot)

    fig, rows = plt.subplots(n_frames, 2, figsize=(10, 5 * n_frames))

    for i, frame, (ax1, ax2) in zip(indexes, frames_to_plot, rows):
        im1 = ax1.imshow(frames[0], vmin=0, vmax=255)
        ax1_divider = make_axes_locatable(ax1)
        cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
        fig.colorbar(im1, cax=cax1)
        ax1.grid(False)
        ax1.set_title('Frame: {:d}'.format(i))

        ax2.hist(frame.flatten(), bins=np.arange(0, 261, 10), log=True, color='darkblue', width=9)
        ax2.set_xlim([0, 261])
        ax2.set_title('Intensity Histogram')

    fig.suptitle('Movie: ' + name)
    fig.tight_layout()
    return fig
