# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from math import ceil
import os
folder_path = os.getcwd()
font_type = ImageFont.truetype(r'{}\assets\verdana.ttf'.format(folder_path ), 25)

images=[]
cl=open('setting.txt','r')
cl=cl.readlines()
bkclr=cl[0].strip()
if bkclr=='black':
    cl1=(24,25,26)
    cl2=(211,233,233)
else:
    cl1=(211,233,233)
    cl2=(24,25,26)

# def drawImage(x, author, comments_parts ,y_location):
#     for i in range(len(comments_parts)):
#         if i==0:
#             image = Image.new('RGB', (1280,720), color =cl1)
#             draw = ImageDraw.Draw(image)
#             draw.text(xy=(100,y_location - 40), text=author, fill =(89,161,210), font=font_type)
#             draw.text(xy=(100,y_location + 40*i), text=comments_parts[i], fill =cl2, font=font_type)
#             image.save(r'{}\generated\part'.format(folder_path ) + str(x) + '-' + str(i) +'.jpg')
#         elif i>0:
#             image = Image.open(r'{}\generated\part'.format(folder_path)+ str(x) + '-' + str(i-1) +'.jpg')
#             draw = ImageDraw.Draw(image)
#             draw.text(xy=(100,y_location + 40*i), text=comments_parts[i], fill =cl2, font=font_type)
#             image.save(r'{}\generated\part'.format(folder_path ) + str(x) + '-' + str(i) +'.jpg')

def drawImage(x, author, post_titles ,y_location,j):
    i=int(0)
    image = Image.new('RGB', (1280, 720), color=cl1)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, y_location - 40), text=author, fill=(89, 161, 210), font=font_type)
    for i in range(len(post_titles)):
        draw.text(xy=(100,y_location + 40*i), text=post_titles[i], fill =cl2, font=font_type)
    image.save(r'{}\generated\part'.format(folder_path ) + str(x) +'.jpg')

def drawImage1(x, author, post_titles ,y_location,j):
    i=int(0)
    image = Image.new('RGB', (1280, 720), color=cl1)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, y_location - 40), text=author, fill=(89, 161, 210), font=font_type)
    for i in range(len(post_titles)):
        draw.text(xy=(100,y_location + 40*i), text=post_titles[i], fill =cl2, font=font_type)
    image.save(r'{}\generated\part'.format(folder_path ) + str(x) + '-' + str(j) +'.jpg')


def drawImage2(x, author, post_bodies ,y_location,j):
    i=int(0)
    image = Image.new('RGB', (1280, 720), color=cl1)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(100, y_location - 40), text=author, fill=(89, 161, 210), font=font_type)
    for i in range(len(post_bodies)):
        draw.text(xy=(100,y_location + 40*i), text=post_bodies[i], fill =cl2, font=font_type)
    image.save(r'{}\generated\part'.format(folder_path ) + str(x) + '-' + str(j) +'.jpg')
            

