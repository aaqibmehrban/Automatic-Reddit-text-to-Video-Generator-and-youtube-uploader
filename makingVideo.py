from moviepy.editor import *
import os

def makingVideo(comments,post_titles,post_bodies):
    videos=[]
    folder_path = os.getcwd()
    flash = VideoFileClip('flash.mp4')
    flash.fps = 30
    # new_audio = r'C:\Users\rajaa\Downloads\Compressed\Reddit-video-generation-master\Reddit-video-generation-master\funny34.mp3'
    # i=int(1)
    print('combine function')
    print(post_titles)
    for i in range(len(post_titles)):
        print('this is the making video :{}'.format(i))
        audio = AudioFileClip(r'{}\voices\part98'.format(folder_path)+ '-' + str(i)+'.mp3')
        intro = ImageClip(r'{}\generated\part98'.format(folder_path) + '-' + str(i)+'.jpg', duration = audio.duration )
        intro.fps = 30
        intro = intro.set_audio(audio)
        intro = intro.set_end(intro.duration-.3)
        videos.append(intro)
        videos.append(flash)

    for i in range(len(post_bodies)):
        print('this is the making video :{}'.format(i))
        audio = AudioFileClip(r'{}\voices\part97'.format(folder_path) + '-' + str(i) + '.mp3')
        intro = ImageClip(r'{}\generated\part97'.format(folder_path) + '-' + str(i) + '.jpg', duration=audio.duration)
        intro.fps = 30
        intro = intro.set_audio(audio)
        intro = intro.set_end(intro.duration - .3)
        videos.append(intro)
        videos.append(flash)

    # for x in range(len(comments)):
    #
    #     for i in range(len(comments[x])):
    #         audio = AudioFileClip(r'{}\voices\part'.format(folder_path) + str(x) + str(i) + '.mp3')
    #         clip = ImageClip(r'{}\generated\part'.format(folder_path)+str(x) + '-' + str(i)+'.jpg', duration = audio.duration )
    #         clip.fps = 30
    #         clip = clip.set_audio(audio)
    #         clip = clip.set_end(clip.duration)
    #         videos.append(clip)
    #
    #     videos.append(flash)
    for x in range(len(comments)):

        # for i in range(len(comments[x])):
        audio = AudioFileClip(r'{}\voices\part'.format(folder_path) + str(x) + '.mp3')
        clip = ImageClip(r'{}\generated\part'.format(folder_path) + str(x) + '.jpg',
                         duration=audio.duration)
        clip.fps = 30
        clip = clip.set_audio(audio)
        clip = clip.set_end(clip.duration)
        videos.append(clip)

        videos.append(flash)

        audio = AudioFileClip(r'{}\voices\part100'.format(folder_path)+'-' + str(x) + '.mp3')
        clip = ImageClip(r'{}\generated\part100'.format(folder_path) + '-' + str(x) + '.jpg',
                         duration=audio.duration)
        clip.fps = 30
        clip = clip.set_audio(audio)
        clip = clip.set_end(clip.duration)
        videos.append(clip)

        videos.append(flash)

    final_clip = concatenate(videos)


    final_clip.write_videofile("final.mp4")



