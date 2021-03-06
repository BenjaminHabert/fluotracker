"""
Lance le processus d'extraction sur l'ensemble des films.

Les étapes sont les suivantes:

 - récupère tous les fichiers .tif qui sont dans le dossier data/raw/

 - pour chacun de ces films, on créé un nouveau répertoire dans data/movies
   et on copie dedans le film d'origine. On obtient par exemple:
   - data/movies/movie8/movie.tif
   - data/movies/nanodiament_super_brillant/movie.tif
   (REMARQUE: on a donc plusieurs sauvegardes du même fichier; peut être à modifier si les films
    sont trop volumineux).

 - Pour chaque dossier de data/movies/ (et donc pour chaque film) on fait l'extraction
   qui est décrite par la fonction extract_tracks_from_movie(folder, name):
   - conversion en frames Numpy
   - applique un filte en ondelettes
   - récupère les tracks avec trackpy
   - filtrer les tracks selon certains critères (longueur..)
   - appliquer une rotation à toutes les trajectoires filtrées pour que les particules
     se déplacent vers la droite
     
 - Au cours de ce processus, plusieurs fichiers intermédiaires sont générés (array Numpy, images,
   fichiers csv avec les trajectoires). Pour un film, toutes ces données sont enregistrées dans
   /data/movies/nom_du_film/
   
Pour lancer le code:

$ source activate.sh
$ python fluotracker/extraction/run_extraction.py
"""


import os
import shutil

import numpy as np
import matplotlib
matplotlib.use('Agg')


from fluotracker.io import files
from fluotracker.extraction import (
    extract,
    filter,
    preprocessing,
    plotting,
    postprocessing,
)


def run():
    prepare_movie_folders()
    extract_tracks_from_movies()


def prepare_movie_folders():
    folder = files.create_abspath('raw/')
    movies = movies = [
        {
            'name': os.path.splitext(filename)[0],
            'path': os.path.join(folder, filename)
        }
        for filename in os.listdir(folder)
        if filename.endswith('.tif')
    ]
    for movie in movies:
        new_path = files.create_abspath('movies/' + movie['name'] + '/movie.tif',
                                        create_folders=True)
        shutil.copy(movie['path'], new_path)


def extract_tracks_from_movies():
    folder = files.create_abspath('movies/')
    movies = [
        {
            'name': dirname,
            'path': os.path.join(folder, dirname)
        }
        for dirname in os.listdir(folder)
        if os.path.isdir(os.path.join(folder, dirname))
    ]
    for movie in movies:
        extract_tracks_from_movie(movie['path'], movie['name'])


def extract_tracks_from_movie(folder, name):
    print('Extracting movie: ' + name)
    _convert_movie_to_frames(folder, name)
    _preprocess_frames(folder, name)
    _extract_tracks(folder, name)
    _filter_tracks(folder, name)
    _rotate_tracks(folder, name)
    print('Extraction complete for movie: ' + name)


def _convert_movie_to_frames(folder, name):
    path = os.path.join(folder, 'movie.tif')

    frames = files.load_movie_frames(path)
    outpath = os.path.join(folder, 'frames.npy')
    np.save(outpath, frames)

    fig = plotting.plot_frames_from_movie(frames, name)
    outpath = os.path.join(folder, 'frames.png')
    fig.savefig(outpath)


def _preprocess_frames(folder, name):
    path = os.path.join(folder, 'frames.npy')
    frames = np.load(path)

    frames = preprocessing.apply_wavelet_filter(frames)
    outpath = os.path.join(folder, 'frames_preprocessed.npy')
    np.save(outpath, frames)

    fig = plotting.plot_frames_from_movie(frames, name)
    outpath = os.path.join(folder, 'frames_preprocessed.png')
    fig.savefig(outpath)


def _extract_tracks(folder, name):
    print('Extracting tracks from frames')
    path = os.path.join(folder, 'frames_preprocessed.npy')
    frames = np.load(path)

    tracks = extract.extract_tracks_from_frames(frames)
    tracks['movie'] = name
    outpath = os.path.join(folder, 'tracks.csv')
    files.save_dataframe(tracks, outpath)

    fig = plotting.plot_tracks_infos(tracks, name, frames[0])
    outpath = os.path.join(folder, 'tracks.png')
    fig.savefig(outpath)


def _filter_tracks(folder, name):
    print('Keeping only long tracks')
    path = os.path.join(folder, 'tracks.csv')
    tracks = files.load_dataframe(path)

    filtered = filter.remove_short_tracks(tracks)
    outpath = os.path.join(folder, 'tracks_filtered.csv')
    files.save_dataframe(filtered, outpath)

    fig = plotting.plot_tracks_infos(filtered, name)
    outpath = os.path.join(folder, 'tracks_filtered.png')
    fig.savefig(outpath)


def _rotate_tracks(folder, name):
    print('Rotating tracks')
    path = os.path.join(folder, 'tracks_filtered.csv')
    tracks = files.load_dataframe(path)

    rotated = postprocessing.add_rotated_coordinates(tracks)
    outpath = os.path.join(folder, 'tracks_rotated.csv')
    files.save_dataframe(rotated, outpath)

    fig = plotting.plot_particles_coordinates(rotated, 'x_rotated', 'y_rotated', name)
    outpath = os.path.join(folder, 'tracks_rotated.png')
    fig.savefig(outpath)


if __name__ == "__main__":
    run()
