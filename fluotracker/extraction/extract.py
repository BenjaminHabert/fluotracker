import pandas as pd
import filter
import trackpy as tp

number = 411

filep = "Diamants-"+str(number)+"_crop.tif"
filecsv = "TrajectoirePyW-Diam"+str(number)+"_crop_minmass150.csv"

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
    # PB avec le choix des paramètres de memory. Certaines trajectoires sont mal interprétées
    # exemple du film 411 : avec memory = 7, on a une traj qui commence sur un stop bordélique
    # avec memory = 2, la trajectoire passe au dessus du stop en question : c'est ce qui se passe
    # en réalité si on regarde le film. Le pb (je crois) est lié au fait que link_df ne prédit pas
    # la prochaine position en fonction de la vitesse. Ca doit être possible mais comment ?

    # t_neurons will contain the trajectories of interest
    t_neurons = pd.DataFrame()

    Ntraj = 0
    for item in set(tracks.particle):
        #print(item)
        sub = tracks[tracks.particle==item] # selection of the item-th particle trajectory
        distance = tp.motion.diagonal_size(sub)
        # distance is an estimation of the particle displacement if the displacement
        # is roughly linear

        if distance>7:
            Ntraj += 1
            t_neurons = t_neurons.append(sub)

            print('\n',Ntraj,'trajectoires retenues\n')

    # plt.figure()
    # plt.imshow(frames[0])
    # tp.plot_traj(t_neurons)
    t_neurons.to_csv(filecsv, sep = '\t')

    return tracks
