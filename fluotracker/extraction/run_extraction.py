from fluotracker.io import files

import extract
import filter


def run():
    """Run extraction of nanoparticle tracks from movies."""
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


def extract_tracks():
    movie_to_extract = "raw/movie8.tif"

    # Loading
    print("Loading movie: " + movie_to_extract)
    frames = files.load_movie_frames(movie_to_extract)
    print("Movie loaded")
    #print(frames)

    # Extracting
    tracks = extract.extract_tracks_from_frames(frames)
    tracks['movie'] = 'movie8'
    print('Done extracting from movie. tracks is like this:')
    print(tracks.head())

    # Saving result
    output_filename = "extracted/movie8.csv"
    print("Saving tracks to file: " + output_filename)
    files.save_dataframe(tracks, output_filename)

    # Applying filters
    # Le fait de sauvegarder puis charger les données peut paraître un peu idiot
    # mais l'intérêt c'est qu'ensuite on peut ne réaliser qu'une seule étape sans
    # redémarrer le projet depuis le début.
    extracted = files.load_dataframe(output_filename)
    filtered = filter.remove_short_tracks(extracted, threshold_length=20)
    files.save_dataframe(filtered, 'filtered/movie8.csv')


if __name__ == "__main__":
    print('Lauching main script to extract particles tracks from movies.')
    extract_tracks()
    print('Main extraction script completed')
    print('Content of data/ is now like this:')
    files.inventory()
