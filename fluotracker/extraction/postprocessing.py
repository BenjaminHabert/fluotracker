import numpy as np
import pandas as pd


def add_rotated_coordinates(tracks):
    """Rotate coordinates towards the right.

    Parameters
    ----------
    tracks: pd.DataFrame
        as created by trackpy. Contains columns: particle, x, y.

    Returns
    -------
    tracks: pd.DataFrame
        same dataframe with extra columns: x_rotated, y_rotated

    """
    rotated = (
        tracks
        .groupby('particle')
        .apply(_rotate_single_track)
        .reset_index()
        .drop('level_1', axis=1)
    )
    tracks = tracks.merge(rotated, on=['particle', 'frame'])
    return tracks


def _rotate_single_track(df):
    coords = df.loc[:, ['x', 'y']].values
    coords = coords - coords[0, :]

    distances = (coords ** 2).sum(axis=1)
    furthest = np.argmax(distances)

    theta = np.arctan2(coords[furthest, 1], coords[furthest, 0])
    rotation = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    coords = np.matmul(coords, rotation)
    return pd.DataFrame({
        'frame': df['frame'].values,
        'x_rotated': coords[:, 0],
        'y_rotated': coords[:, 1],
    })
