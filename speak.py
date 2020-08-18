from gtts import gTTS


def speakk(myText,language):
    print(myText)
    output = gTTS(text=myText, lang = language, slow=False)
    return output

