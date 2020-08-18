import os
from moviepy.editor import *

import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def finalizing(filename):
    path=os.getcwd()
    print(path)
    clips=['./intro_outros/intro.mp4','./video_with_bk_music.mp4','./intro_outros/outro.mp4']
    clip1 = VideoFileClip(r"{}\intro_outros\intro.mp4".format(path))
    clip2 = VideoFileClip(r"{}\video_with_bk_music.mp4".format(path))
    clip3 = VideoFileClip(r"{}\intro_outros\outro.mp4".format(path))
    final_clip = concatenate_videoclips([clip1,clip2,clip3])

    final_clip.write_videofile(filename+'.mp4')


# finalizing('videokaksossc')
