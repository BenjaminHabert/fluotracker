"""
This module makes it easy to load / save files from the `data/` directory.

In particular we add functions to load frames from a .tif movie
"""
import os

DATA = "/absolute/path/to/data/"  # specific to you!


def inventory():
    """prints the list of files in the directory (goes into subfolders)

    Example
    -------

    >>> inventory()
    raw/
    raw/movie8.tif
    processed/
    processed/movie8_tracks.csv
    """
    print('Needs to be implemented')


def get_movies_paths(relative_path):
    """Returns the list of .tif movies in a subfolder

    Example
    -------

    >>> get_movies_paths('raw/')
    {"movie8": "/absolute/path/to/data/raw/movie8.tif"}

    Parameters
    ----------
    relative_path: str
        the subfolder in `data/` where the movies are

    Returns
    -------
    paths: dict
        dictionary movie_name -> movie absolue path
    """
    return {}


def get_name_and_path(relative_path):
    """Returns filename (no extension) and absolute filepath from  input relative_path

    Parameters
    ----------
    relative_path: str
        relative_path to file from `data/` root folder

    Returns
    -------
    name, path: tuple of str
        name: filename with no extension (and no spaces?)
        path: absolute path to file
    """
    name = relative_path
    absolute_path = "NOT FOUND"
    return (name, absolute_path)


def create_abspath(relative_path, folder=None):
    """Returns absolute path in the data/ folder"""
    return relative_path


def load_movie_frames_and_name(movie_relative_path):
    """Returns frames as numpy array"""
    frames = []
    name = "movie_name_extracted_from_path_no_extension"
    return frames, name


def save_dataframe(df, relative_path, folder=None):
    """Saves pandas dataframe as csv in the `data/` folder"""
    # make full path DATA + folder (if exists) + relative_path
    # save dataframe to csv file
    pass
