import os
import subprocess

from lyrics import get_songs_data

PLAYLIST_LINK = 'https://www.youtube.com/playlist?list=PLQzNb__3Hyqq_gqsnUOUvGLSSgw2IgQ7y'
OUTPUT_PATH = '/home/mykhailo/repos/ydow/music/'
# youtube-dl names files with weird symbols in the beginning
END_OF_SONG_NAME = -16


def download_by_url(url, path=None):
    os.chdir(path)
    subprocess.call(
        ['youtube-dl', '-w', '--extract-audio', '--audio-format', 'mp3', '--extract-audio', '--prefer-ffmpeg', url])


def rename_files(end_of_song_name, path=None):
    for filename in os.listdir(path):
        new_filename = filename[:end_of_song_name] + '.mp3'
        os.rename(path + filename, path + new_filename)


if __name__ == '__main__':
    download_by_url(PLAYLIST_LINK, OUTPUT_PATH)
    rename_files(END_OF_SONG_NAME, OUTPUT_PATH)
    get_songs_data(OUTPUT_PATH)
