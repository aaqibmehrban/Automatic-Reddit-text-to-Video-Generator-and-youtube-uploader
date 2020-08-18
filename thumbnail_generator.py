from character_generator import *
from PIL import Image, ImageDraw, ImageFont
# get an image

def thumbnail(word,name):
    base = Image.open('thumbnail.jpg').convert('RGBA')

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # get a font
    fnt = ImageFont.truetype(r"/assets/verdanab.ttf", 200)
    # get a drawing context
    d = ImageDraw.Draw(txt)



    (comments_parts, y_location) = divideComment1(word)

    print(comments_parts)
    print(y_location)
    bc=350
    s=850
    for i in comments_parts:
        print(i)
        d.text((bc,s), i, font=fnt, fill=(255, 255, 255, 255))
        s+=160


    out = Image.alpha_composite(base, txt)

    out.save(fp='{}.png'.format(name))
