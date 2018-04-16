"""
This module makes it easy to load / save files from the `data/` directory.

In particular we add functions to load frames from a .tif movie
"""
import os

import numpy as np
import pandas as pd

this_folder = os.path.dirname(__file__)
DATA_FOLDER = os.path.abspath(os.path.join(this_folder, '../../data'))
print('[files.py]: data folder is: ' + DATA_FOLDER)


def inventory():
    """Print the list of files in the directory (goes into subfolders).

    Example
    -------
    >>> inventory()
    raw/
    raw/movie8.tif
    processed/
    processed/movie8_tracks.csv
    """
    for root, dirs, files in os.walk(DATA_FOLDER):
        local_root = root.replace(DATA_FOLDER, '<data>')
        print(os.path.join(local_root))
        for file in files:
            print(os.path.join(local_root, file))


def create_abspath(relative_path):
    """Return absolute path in the data/ folder."""
    if os.path.isabs(relative_path):
        absolute_path = relative_path
        if not absolute_path.startswith(DATA_FOLDER):
            print('WARNING! you are trying to load or save from :')
            print(relative_path)
            print('which is not in the local data/ folder:')
            print(DATA_FOLDER)
            print('Does your relative path star with "/" ?')
    else:
        absolute_path = os.path.join(DATA_FOLDER, relative_path)
    return absolute_path


def load_movie_frames(movie_relative_path):
    """Return frames as numpy array.

    Parameters
    ----------
    movie_relative_path: str
        chemin d'accès vers le fichier de film (chemin relatif depuis le dossier data/)

    Returns
    -------
    frames: np.array
        le contenu du fichier de film

    Examples
    --------
    >>> frames = load_movie_frames("raw/movie8.tif")
    >>> frames.shape
    (800, 800, 135)

    """
    movie_absolute_path = create_abspath(movie_relative_path)
    print("Loading movie from " + movie_absolute_path)

    # TODO: implémenter la fonction qui utilise numpy pour lire le contenu du .tif
    # pour l'instant on retourne un "faux" objet
    return np.array([1, 2, 3])


def _validate_dataframe_file_extension(absolute_path):
    """Return file extension if valid."""
    _, extension = os.path.splitext(absolute_path)
    valid_extensions = ['.csv', '.pickle']
    if extension not in valid_extensions:
        error_info = '\n'.join([
            'Cannot process file: ' + absolute_path,
            'Possible extensions are: ' + str(valid_extensions)
        ])
        raise ValueError(error_info)
    return extension


def save_dataframe(df, relative_path):
    """Save pandas dataframe as csv in the `data/` folder."""
    absolute_path = create_abspath(relative_path)
    extension = _validate_dataframe_file_extension(absolute_path)

    print('Saving dataframe to: ' + absolute_path)
    os.makedirs(os.path.dirname(absolute_path), exist_ok=True)

    if extension == '.csv':
        df.to_csv(absolute_path, index=False, sep=',')
    elif extension == '.pickle':
        df.to_pickle(absolute_path)


def load_dataframe(relative_path):
    """Load pandas dataframe from path relative do data/ folder."""
    absolute_path = create_abspath(relative_path)
    extension = _validate_dataframe_file_extension(absolute_path)

    print('Loading dataframe from: ' + absolute_path)
    if extension == '.csv':
        return pd.read_csv(absolute_path)
    elif extension == '.pickle':
        return pd.read_pickle(absolute_path)


# # FINALEMENT tout ça n'est pas super utile au moins pour l'instant:
#
# def get_movies_paths(relative_path):
#     """Returns the list of .tif movies in a subfolder
#
#     Example
#     -------
#
#     >>> get_movies_paths('raw/')
#     {"movie8": "/absolute/path/to/data/raw/movie8.tif"}
#
#     Parameters
#     ----------
#     relative_path: str
#         the subfolder in `data/` where the movies are
#
#     Returns
#     -------
#     paths: dict
#         dictionary movie_name -> movie absolue path
#     """
#     return {}
#
#
# def get_name_and_path(relative_path):
#     """Returns filename (no extension) and absolute filepath from  input relative_path
#
#     Parameters
#     ----------
#     relative_path: str
#         relative_path to file from `data/` root folder
#
#     Returns
#     -------
#     name, path: tuple of str
#         name: filename with no extension (and no spaces?)
#         path: absolute path to file
#     """
#     name = relative_path
#     absolute_path = "NOT FOUND"
#     return (name, absolute_path)
