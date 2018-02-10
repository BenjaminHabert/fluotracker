from fluotracker.io import files

import extract


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


def extract_tracks(movie_to_extract, output_folder):
    # Loading
    print("Loading movie: ")
    print(movie_to_extract)
    frames, movie_name = files.load_movie_frames_and_name(movie_to_extract)

    # Extracting
    tracks = extract.extract_tracks_from_frames(frames)
    tracks['movie'] = movie_name
    print('Done extracting from movie. tracks is like this:')
    print(tracks.head())

    # Saving result
    output_filename = movie_name + "_extracted.csv"
    print("Saving tracks to file: ")
    print(output_filename)
    files.save_dataframe(tracks, output_filename, folder=output_folder)


if __name__ == "__main__":
    print('Lauching main script to extract particles tracks from movies.')

    movie_to_extract = "raw/movie8.tif"
    output_folder = "extracted"
    extract_tracks(movie_to_extract, output_folder)

    print('Main extraction script completed')

    # run()
