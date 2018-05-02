import pandas as pd
import filter
import trackpy as tp

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
    Nbframe = frames.shape[0]
    print('[extract.py] Running extraction from tracks')

    print('First Step: Apply the "à trous" Wavelet transform to the frames')
    NewFrames = filter.Filtering_frames(frames)

    print('Second Step: Localizaton of the nanoparticles in each frame')
    f = tp.batch(NewFrames[:Nbframe], 7, minmass=150,preprocess=False);

    print('Third Step: Computation of the trajectories')
    tracks = tp.link_df(f, search_range=5, memory=7)

    return tracks
