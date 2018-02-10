def run():
    """Run extraction of nanoparticle tracks from movies"""
    pass
    # List movies in data folder

    # For each movie
    #   - load the images
    #   - extract particles positions as arrays
    #   - save tracks as csv files
    #   - (optional): save image with tracks overlay

    # For each extracted tracks file
    #   - load the tracks
    #   - filter valid and invalid tracks
    #   - save all valid tracks as one csv. columns: original file / partile ID / x (px) / y (px)
    #   - (optional): save image with tracks overlay indicating valid / invalid choice (green / red)

if __name__ == "__main__":
    print('Lauching main script to extract particles tracks from movies.')
    run()
