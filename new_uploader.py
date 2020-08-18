from tkinter import filedialog

from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from tkinter import *
import tkinter as tk


def quit():
    window.destroy()


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

def send_details():
    # loggin into the channel
    des=open(description_file,'r')
    des_list=[]
    des=des.readlines()
    for l in des:
        des_list.append(l)

    descr=listToString(des_list)
    tit=video_file.split('/')[-1]
    title=tit.split('.')[0]
    tags=tit.split(' ')

    channel = Channel()
    channel.login("client_secrets.json", "credentials.storage")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=video_file)

    # setting snippet
    video.set_title(title)
    video.set_description(descr)
    video.set_tags(tags)
    video.set_category("Entertainment")
    # video.set_default_language("english")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    video.set_thumbnail_path(thumbnail_file)

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.get_video_id())
    print(video)

    # liking video
    video.like()


def video__file(event=None):
    global video_file
    video_file = filedialog.askopenfile()
    video_file=video_file.name

    print(video_file)


def thumbnail__file(event=None):
    global thumbnail_file
    thumbnail_file = filedialog.askopenfile()
    thumbnail_file = thumbnail_file.name

    print(thumbnail_file)

def description__file(event=None):
    global description_file
    description_file = filedialog.askopenfile()
    description_file = description_file.name

    print(description_file)

def main_screen():
    global window
    window = tk.Tk()
    window.geometry("400x400")
    window.title("Youtube upload BOT")


    label1 = tk.Label(text="Youtube Bot", font=('ariel', 20, 'bold'))
    label1.place(x=80, y=10)

    usrlabel = tk.Label(text="Select File", font=("Times new roman", 16))
    usrlabel.place(x=100, y=150)
    button = tk.Button(text='Select', bg="yellow", command=video__file)
    button.place(x=300, y=150)

    usrlabel = tk.Label(text="Select File", font=("Times new roman", 16))
    usrlabel.place(x=100, y=150)
    button = tk.Button(text='Select', bg="yellow", command=thumbnail__file)
    button.place(x=300, y=150)

    usrlabel = tk.Label(text="Select File", font=("Times new roman", 16))
    usrlabel.place(x=100, y=150)
    button = tk.Button(text='Select', bg="yellow", command=description_file)
    button.place(x=300, y=150)

    button1 = tk.Button(window, text="Start", bg="green", command=send_details)
    button1.place(x=240, y=350)
    button2 = tk.Button(window, text="Stop", bg="Red", command=quit)
    button2.place(x=280, y=350)

    window.mainloop()


main_screen()
