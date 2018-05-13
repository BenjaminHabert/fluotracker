import pandas as pd
import trackpy as tp


def remove_short_tracks(tracks, threshold_length=7):
    """Filter les tracks qui font plus de X pixels.

    Parameters
    ----------
    tracks: pd.DataFrame
        contient les traces brutes des nanoparticle
    threshold_length: float
        le nombre de pixels minimum pour avoir une trace valide

    Returns
    -------
    t_neurons: pd.DataFrame
        seulement une partie des traces obtenues en entréee.

    """
    print("[filter.py] Je filtre les tracks qui sont trop courtes")

    # t_neurons will contain the trajectories of interest
    t_neurons = pd.DataFrame()

    Ntraj = 0
    for item in set(tracks.particle):
        sub = tracks[tracks.particle == item]  # selection of the item-th particle trajectory
        distance = tp.motion.diagonal_size(sub)
        # distance is an estimation of the particle displacement if the displacement
        # is roughly linear

        if distance > threshold_length:
            Ntraj += 1
            t_neurons = t_neurons.append(sub)
            print('\n', Ntraj, 'trajectoires retenues\n')

    # plt.figure()
    # plt.imshow(frames[0])
    # tp.plot_traj(t_neurons)
    # t_neurons.to_csv(filecsv, sep='\t')
    return t_neurons
