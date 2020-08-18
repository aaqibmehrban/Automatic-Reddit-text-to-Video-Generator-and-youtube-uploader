from moviepy.editor import *

def processSound(audio):
    print('begin duration', audio.duration)
    begin_cut = audio.duration
    
    if audio.duration > 1.5:
        for i in range(6): #0 to 5
            frame_volume = audio.get_frame( (audio.duration -.51) + (.1*i))
            if frame_volume[0] == 0:
                begin_cut = (audio.duration -.51) + (.1*i)
                break
    
        if begin_cut + .1 < audio.duration:
            audio = audio.set_end(begin_cut + .1)
    
    print('end duration', audio.duration)    
    return audio

               
                

