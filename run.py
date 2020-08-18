from time import time
from time import sleep
import pyttsx3
import comtypes.client

import shutil

start = time()
from combine import *
from drawImage import drawImage, drawImage1, drawImage2
from speak import *
from makingVideo import makingVideo
from processSound import processSound
from reddit_scrapper_new import *
from finalizing_video import *
from thumbnail_generator import *
# from youtube_video_uploader import *

import random
import string

end = time.time()


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += " " + ele

        # return string
    return str1


def get_script():
    if script == 'auto':
        vidf = open('links.txt', 'r')
        vidf = vidf.readlines()
        for i in vidf:
            shutil.rmtree('generated')
            shutil.rmtree('voices')
            os.mkdir('generated')
            os.mkdir('voices')
            print('Video Started')
            urls = i.split(',')
            (post_titles, post_authors, comments, authors, y_locations, post_y_locations,
             title_for_thumbnail,post_bodies,post_bod_y_locations,replies_author,replies,replies_y_locations) = new_scrapr(urls, total_cmnts)
            print('')
            print('-----------start')
            print(post_titles)
            print('----------------')
            start = time.time()
            for x in range(len(comments)):
                drawImage(x, authors[x], comments[+x], y_locations[x],x)
            # draw image (for post title)
            # x=0
            # print(talent_)
            for i in range(len(post_titles)):
                print('now going to draw:')
                print(post_titles[i])
                drawImage1(98, post_authors[i], post_titles[i], post_y_locations[i],i)
                # input('')
            for j in range(len(post_bodies)):
                print('now going to draw:')

                drawImage2(97, post_authors[j], post_bodies[j], post_bod_y_locations[j],j )

            for j in range(len(replies_author)):
                print('now going to draw:')

                drawImage2(100, replies_author[j], replies[j], replies_y_locations[j], j)
                # input('')
            end = time.time()
            print('*********draw: ', end - start)

    else:
        form = open('format_script.txt', 'r')
        form = form.readlines()
        pst_ath=form[0].strip().split('::')[1]
        pst_ti = form[1].strip().split('::')[1]
        title_for_thumbnail = pst_ti


        # pst_ath = form[0].strip().split('::')[1]
        # pst_ti = form[1].strip().split('::')[1]
        #
        # pst_bodies = form[2].strip().split('::')[1]
        # pst_bodies = pst_bodies.split('|')
        # at = form[3].strip().split('::')[1]
        # cm = form[4].strip().split('::')[1]
        # pst_ath = pst_ath.split('|')
        # pst_ti = pst_ti.split('|')
        # at = at.split('|')
        # cm = cm.split('|')
        post_bodies = []
        post_bod_y_locations = []
        y_locations = []
        comments = []
        authors = at
        post_titles = []
        post_authors = pst_ath
        post_y_locations = []

        for i in cm:
            (comment, y_location) = divideComment(i)
            comments.append(comment)
            y_locations.append(y_location)

        for i in pst_bodies:
            (post_body, post_bod_y_location) = divideComment(i)
            post_bodies.append(post_body)
            post_bod_y_locations.append(post_bod_y_location)

        for i in pst_ti:
            (post_title, post_y_location) = divideComment(i)
            post_titles.append(post_title)
            post_y_locations.append(post_y_location)

        start = time.time()
        for x in range(len(comments)):
            drawImage(x, authors[x], comments[x], y_locations[x],x)
        # draw image (for post title)

        for x in range(len(post_titles)):
            drawImage1(98, post_authors[x], post_titles[x], post_y_locations[x],x)

        for j in range(len(post_bodies)):
            drawImage2(97, post_authors[j], post_bodies[j], post_bod_y_locations[j], j)

        end = time.time()
        print('*********draw: ', end - start)

    start = time.time()
    language = 'en'
    for x in range(len(comments)):
        # for i in range(len(comments[x])):
        #     path = r'{}\voices\part'.format(folder_path) + str(x) + '-' + str(i) + '.mp3'
            path = r'{}\voices\part'.format(folder_path) + str(x)+ '.mp3'
            myText = comments[x]
            if voic == 'male':
                engine = pyttsx3.init()
                engine.setProperty('rate', 180)
                print(myText)
                engine.save_to_file(listToString(myText), path)
                engine.runAndWait()
                time.sleep(3)


            else:
                engine = pyttsx3.init()
                voices = engine.getProperty('voices')  # getting details of current voice
                # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
                engine.setProperty('voice', voices[1].id)
                engine.setProperty('rate', 170)
                print(myText)
                engine.save_to_file(listToString(myText), path)
                engine.runAndWait()
                time.sleep(3)
                # output = speakk(myText, language)
                # output.save(path)

    # Chat for intro
    print('------------end=---------')
    print(post_titles)
    print('-------------------------')
    # counter=int(0)
    for x in range(len(post_titles)):
        # for i in range(len(post_titles[x])):
        myText = post_titles[x]
        path = r'{}\voices\part98'.format(folder_path) + '-' + str(x) + '.mp3'
        if voic.strip() == 'male':
            engine = pyttsx3.init()
            engine.setProperty('rate', 180)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)

        else:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 170)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)
            # output = speakk(listToString(myText), language)
            # output.save(path)
            # script.write(myText + '\n')
        # counter+=1
    for x in range(len(post_bodies)):
        # for i in range(len(post_titles[x])):
        myText = post_bodies[x]
        path = r'{}\voices\part97'.format(folder_path) + '-' + str(x) + '.mp3'
        if voic.strip() == 'male':
            engine = pyttsx3.init()
            engine.setProperty('rate', 180)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)

        else:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 180)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)

    for x in range(len(replies)):
        # for i in range(len(post_titles[x])):
        myText = replies[x]
        path = r'{}\voices\part100'.format(folder_path) + '-' + str(x) + '.mp3'
        if voic.strip() == 'male':
            engine = pyttsx3.init()
            engine.setProperty('rate', 180)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)

        else:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')  # getting details of current voice
            # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
            engine.setProperty('voice', voices[1].id)
            engine.setProperty('rate', 170)
            print(listToString(myText))
            engine.save_to_file(listToString(myText), path)
            engine.runAndWait()
            time.sleep(3)


    end = time.time()
    print('*********chat: ', end - start)
    #########################################################################
    #########################################################################
    # Processing the pauses in the soundclips
    start = time.time()

    end = time.time()
    print('*********pause: ', end - start)
    start = time.time()
    makingVideo(comments, post_titles,post_bodies)
    end = time.time()
    print('*********stitch: ', end - start)
    #########################################################################
    #########################################################################
    # this version of code creates videos w/o background music, if desired use the following code to overlay music
    # clip.audio = CompositeAudioClip([clip.audio, new_audio])
    # time.sleep(10)
    filename = "final_video{}".format(randomString())
    os.mkdir(filename)
    print('---------- Start Generating Script --------')
    fil=open(filename+'.txt','w+')
    for i in range(len(post_titles)):
        fil.write(post_authors[i] + ':' + listToString(post_titles[i]) + '\n')

    for i in range(len(post_bodies)):
        fil.write(post_authors[i] + ':' + listToString(post_bodies[i]) + '\n')

    for i in range(len(comments)):
        fil.write(authors[i] + ':' + listToString(comments[i]) + '\n')

    print('------------ completed --------------------------')

    start_combine()
    print('--------- Finalizing Video -----------------------------')

    finalizing(filename)
    sleep(5)
    print('''
    Video has been created check the main directory
    ''')
    print(title_for_thumbnail)
    thumbnail(title_for_thumbnail, filename)
    print('Thumbnail_generated ---- Successfully')
    sleep(5)
    fil.close()
    sleep(5)

    shutil.move('{}\{}.mp4'.format(os.getcwd(), filename),filename)
    shutil.move('{}\{}.txt'.format(os.getcwd(), filename), filename)
    shutil.move('{}\{}.png'.format(os.getcwd(), filename), filename)



def fol_check():
    try:
        shutil.rmtree('generated')
        shutil.rmtree('voices')
    except:
        pass
    global set, total_cmnts, script, voic, yt
    set = open('setting.txt', 'r')
    set = set.readlines()
    voic = set[2].strip()
    script = set[3].strip()
    total_cmnts = set[4].strip()
    # yt = set[5].strip()
    # print(total_cmnts)

    dirName = 'generated'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory Generated :", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    dirName = 'voices'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory Generated :", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


if __name__ == '__main__':
    fol_check()
    get_script()
