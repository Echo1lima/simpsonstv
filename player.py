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
        # mpv command line arguments:
        # -no-window: prevent opening for audio tracs
        # -vo=drm: drop the drm master when doing VT switch
        # -hwdec=auto: enables hardware acceleration
        playProcess = Popen([
            'mpv',
            'no-window',
            'vo=drm',
            'hwdec=auto',
            video
        ])
        playProcess.wait()

def main():
    while True:
        playVideos()

if __name__ == "__main__":
    main()
