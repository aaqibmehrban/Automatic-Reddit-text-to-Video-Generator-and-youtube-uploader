from PIL import Image, ImageDraw, ImageFont
from math import ceil
import os
folder_path =os.getcwd()
font_type = ImageFont.truetype(r'{}\assets\verdana.ttf'.format(folder_path ), 25)

def divideComment(word):
    comments_parts= []   
    begin = 0
    end   = 80
    i     = 0
    y_location = 350 - (ceil(len(word)/80)-1)*(20)
    
    if end > len(word):
        comments_parts.append(word[begin:len(word)])
    while end <= len(word):
        if end > len(word)-1:
            end = len(word)-1
        if word[end-i]==' ':
            comments_parts.append(word[begin:end - i])
            begin = end - i + 1
            end = begin + 80
            i=0
            if end > len(word)-1:
                comments_parts.append(word[begin:len(word)])
        else:
            i+=1
    return (comments_parts,y_location)