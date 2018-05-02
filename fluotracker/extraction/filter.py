from scipy import signal


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

def LowPass1():
    """ First lowpass filter used in the wavelet decomposition

    Returns
    -------
    Array with which the frames will be convoluted
    from Izeddin et al. Opt. Expr. 20, 2081 (2012)
    """
    H0 = 3./8
    H1 = 1./4
    H2 = 1./16
    LowPass = np.array([H2,H1,H0,H1,H2])
    LowPassV = LowPass.reshape(-1,1)
    LowPassH = LowPass.reshape(1,-1)
    Array1 = np.dot(LowPassV,LowPassH)
    return Array1

def LowPass2():
    """ Second lowpass filter used in the wavelet decomposition

    Returns
    -------
    Array with which the frames will be convoluted
    from Izeddin et al. Opt. Expr. 20, 2081 (2012)
    """
    H0 = 3./8
    H1 = 1./4
    H2 = 1./16
    LowPass = np.array([H2,0,H1,0,H0,0,H1,0,H2])
    LowPassV = LowPass.reshape(-1,1)
    LowPassH = LowPass.reshape(1,-1)
    Array2 = np.dot(LowPassV,LowPassH)
    return Array2

def Wavelet2(Array,Array1,Array2):
    """
    Wavelet image of Array. Consist in the convolution of Array with Array1 then with Array2

    Parameters
    ----------
    Array, Array1 and Array2 are numpy arrays

    Returns
    -------
    NewArray is a numpy array which has the same size than Array
    """
    LC1 = signal.convolve2d(Array,Array1,mode='same')
    LC2 = signal.convolve2d(LC1,Array2,mode='same')
    NewArray = LC1 - LC2
    return NewArray

def Filtering_frames(frames):
    """
    filtering of the movie to get images filtered using the "à trous" wavelet transform

    Parameters
    ----------
    frames is a stack of numpy arrays

    Returns
    -------
    Newframes which is the stack filtered using the wavelet transformation. Same size as frames
    """

    Nbframe = frames.shape[0]
    NbRows = frames.shape[1]
    NbColumns = frames.shape[2]
    #initialization (useful ?)
    Newframes = np.zeros((Nbframe,NbRows,NbColumns))

    LP1 = LowPass1() # low pass matrix
    LP2 = LowPass2() # low pass matrix

    for i in range(Nbframe):
        print(i+"th frame filtered")
        Newframes[i] = Wavelet2(frames[i],LP1,LP2)

    return Newframes
