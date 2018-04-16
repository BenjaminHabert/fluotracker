def remove_short_tracks(tracks, threshold_seconds=3):
    """Filter les tracks qui font plus de X seconds.

    Parameters
    ----------
    tracks: pd.DataFrame
        contient les traces brutes des nanoparticle
    threshold_seconds: float
        le nombre de secondes minimum pour avoir une trace valide

    Returns
    -------
    long_tracks: pd.DataFrame
        seulement une partie des traces obtenues en entréee.

    """
    print("[filter.py] Je filtre les tracks qui sont trop courtes")
    # TODO: implémenter vraiment cette fonction!
    long_tracks = tracks
    return long_tracks
