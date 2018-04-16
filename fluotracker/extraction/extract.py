import pandas as pd


def extract_tracks_from_frames(frames):
    """Extract tracks as dataframe from movie frames.

    Parameters
    ----------
    frames: np.array
        les différentes images chargées depuis le fichier .tif
        en tant que numpy array

    Returns
    -------
    tracks: pd.DataFrame
        les déplacements des nanoparticules dans le film sous la forme
        d'un dataframe pandas. C'est trackpy qui fait la plupart du travail

    """
    print('[extract.py] Running extraction from tracks')

    # TODO: remplacer le code par la réelle extraction
    tracks = pd.DataFrame({
        'x': [1, 2.3, 3, 4],
        'y': [1, 1.1, 1, 1.2],
        'time': [0, 1, 2, 3]
    })
    return tracks
