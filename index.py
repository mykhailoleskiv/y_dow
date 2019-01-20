import os
import subprocess

import requests
from bs4 import BeautifulSoup


def get_play_list_links(url):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    domain = 'https://www.youtube.com'
    urls = []
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        href = href[:href.find('&')]
        if href.startswith('/watch?'):
            urls.append(domain + href)
    return urls


def download_by_url(url, path=None):
    os.chdir(path)
    subprocess.call(['youtube-dl', '-w',
                     '--extract-audio',
                     '--audio-format', 'mp3',
                     '--extract-audio',
                     '--prefer-ffmpeg',
                     url])


# Enter valid link and absolute path
PLAYLIST_LINK = ''
OUTPUT_PATH = ''

if __name__ == '__main__':
    urls = get_play_list_links(PLAYLIST_LINK)
    for url in urls:
        name = download_by_url(url, OUTPUT_PATH)
