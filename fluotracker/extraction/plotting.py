import trackpy as tp
import pandas as pd

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
        im1 = ax1.imshow(frames[0])
        ax1_divider = make_axes_locatable(ax1)
        cax1 = ax1_divider.append_axes("right", size="7%", pad="2%")
        fig.colorbar(im1, cax=cax1)
        ax1.grid(False)
        ax1.set_title('Frame: {:d}'.format(i))

        ax2.hist(frame.flatten(), bins=50, log=True, color='darkblue', width=9)
        ax2.set_title('Intensity Histogram')

    fig.suptitle('Movie: ' + name)
    fig.tight_layout()
    return fig


def plot_tracks_infos(tracks, name, frame=None):
    plt, sns = set_defaults()

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle(name)

    if frame is not None:
        im = ax1.imshow(frame)
        fig.colorbar(im, ax=ax1)
        ax1.grid(False)
    tp.plot_traj(tracks, ax=ax1)
    ax1.set_title('{:d} particle tracks'.format(tracks['particle'].nunique()))

    particle_infos = (
        tracks
        .groupby('particle')
        .apply(lambda df: pd.Series({
            'min_frame': df['frame'].min(),
            'max_frame': df['frame'].max(),
            'n_frames': len(df),
            'raw_mass': df['raw_mass'].median()
        }))
        .reset_index()
    )

    ax2.hist(particle_infos['n_frames'], bins=50, log=True)
    ax2.set_xlabel('Number of frames')
    ax2.set_ylabel('Number of particles')

    ax3.barh(y=particle_infos['particle'],
             width=particle_infos['n_frames'],
             left=particle_infos['min_frame'],
             height=4 if particle_infos['particle'].max() > 100 else 1)
    ax3.set_xlabel('Frame index')
    ax3.set_ylabel('Particle index')

    ax4.loglog(particle_infos['n_frames'], particle_infos['raw_mass'], '.', alpha=0.5)
    ax4.set_xlabel('Number of frames')
    ax4.set_ylabel('median raw_mass')

    return fig
