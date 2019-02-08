import os
import re

import eyed3
from PyLyrics import PyLyrics

from index import OUTPUT_PATH


def parse_song_name(song_name):
    end = song_name.find('-')
    if end == -1:
        end = song_name.find('—')
    artist = song_name[:end]
    artist = re.sub("[\(\[].*?[\)\]]", "", artist)
    song = re.sub("[\(\[].*?[\)\]]", "", song_name[end+1:-4])
    return [artist.strip(), song.strip()]


for filename in os.listdir(OUTPUT_PATH):
    data = parse_song_name(filename)
    # try:
    #     lyrics = PyLyrics.getLyrics(data[0], data[1])
    # except ValueError:
    #     print('Song or Singer does not exist or the API does not have Lyrics')
    track = eyed3.load(OUTPUT_PATH + filename)
    track.tag.artist = data[0]
    track.tag.title = data[1]
    # TODO: change set audio lyrics
    track.tag.save()
