import os
import re

import eyed3
from PyLyrics import PyLyrics


def parse_song_name(song_name):
    end = song_name.find('-')
    if end == -1:
        end = song_name.find('—')
    artist = song_name[:end]
    artist = re.sub("[\(\[].*?[\)\]]", "", artist)
    song = re.sub("[\(\[].*?[\)\]]", "", song_name[end + 1:-4])
    return [artist.strip(), song.strip()]


def get_songs_data(OUTPUT_PATH):
    for filename in os.listdir(OUTPUT_PATH):
        data = parse_song_name(filename)
        track = eyed3.load(OUTPUT_PATH + filename)
        track.tag.artist = data[0]
        track.tag.title = data[1]
        try:
            lyrics = PyLyrics.getLyrics(data[0].title(), data[1].title())
        except ValueError:
            print('{}\'s lyrics do not exists'.format(data[0].title() + ' - ' + data[1].title()))
        else:
            track.tag.lyrics.set(lyrics)
        track.tag.save()
