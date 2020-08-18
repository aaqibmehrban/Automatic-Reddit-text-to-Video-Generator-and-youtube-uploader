import os
import random
import time

from moviepy.audio.fx import volumex
from moviepy.editor import *


# import moviepy.audio.fx.all as af
def start_combine():


    time.sleep(5)
    print('----------- Adding Background Music ---------------')
    path=os.getcwd()
    m=os.listdir("music")
    mu=random.choice(m)
    print(mu)
    videoclip = VideoFileClip("final.mp4")
    audioclip = AudioFileClip(r"{}\music\{}".format(path,mu))
    audio = afx.audio_loop(audioclip, duration=videoclip.duration)
    # newaudio = (audio.afx(vfx.volumex, 0.5))
    newaudio = audio.fx(afx.volumex, 0.2)
    # newaudio = audio.fx(volumex, 0.5)

    new_audioclip = CompositeAudioClip([videoclip.audio, newaudio])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("video_with_bk_music.mp4")


