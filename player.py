import os
import random
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')
videos = []

def getVideos():
    global videos
    videos = []
    for file in os.listdir(directory):
        if file.lower().endswith('.mp4'):
            videos.append(os.path.join(directory, file))

def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)
        return
    
    random.shuffle(videos)
    for video in videos:
        # MPlayer command line arguments:
        # -fs: Fullscreen mode
        # -nolirc: Disable LIRC interface
        # -really-quiet: Minimal console output
        # -noborder: No window decoration
        playProcess = Popen([
            'mplayer',
            '-fs',
            '-nolirc',
            '-really-quiet',
            '-noborder',
            video
        ])
        playProcess.wait()

def main():
    while True:
        playVideos()

if __name__ == "__main__":
    main()
