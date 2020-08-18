from tkinter import *
import tkinter as tk




def textfilegenerator():
    window.destroy()
    slba = slbk.get()
    slw =slbkw.get()
    fntba=fntbk.get()
    fntw =fntwh.get()
    voim =voimal.get()
    voif =voifem.get()
    scpa =scpaut.get()
    scpm =scpman.get()
    cm   = cmnts.get()
    ytb =yt.get()
    print(ytb)
    set =open('setting.txt','w+')
    if slba ==1:
        set.write('black\n')
    else:
        set.write('white\n')
    if fntba==1:
        set.write('black\n')
    else:
        set.write('white\n')
    if voim==1:
        set.write('male\n')
    else:
        set.write('female\n')
    if scpa==1:
        set.write('auto\n')
    else:
        set.write('manual\n')
        fil=open('format_script.txt','w+')
        fil.write("""post_authors::
post_titles::
post_bodies::
authors::
comments::""")
    set.write(cm+'\n')
    # if ytb ==1:
    #     set.write('yes\n')
    # else:
    #     set.write('no\n')

    set.close()
    # messagebox.showinfo('Complete','Setting saved')
    root = tk.Tk()
    root.title("Complete")
    label = tk.Label(root, text="Setting Saved")
    label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    button = tk.Button(root, text="OK", command=lambda: root.destroy())
    button.pack(side="bottom", fill="none", expand=True)
    root.mainloop()




def main_screen():
    global window
    window = tk.Tk()
    window.geometry("600x600")
    window.title("Reddit Vedio Generator BOT")
    global username
    global slbk,slbkw,fntbk,fntwh,voimal,voifem,scpaut,scpman,cmnts,yt

    slbk= IntVar()
    slbkw = IntVar()
    fntbk =IntVar()
    fntwh   =IntVar()
    voimal =IntVar()
    voifem =IntVar()
    scpaut =IntVar()
    scpman =IntVar()
    cmnts= StringVar()
    yt =IntVar()


    label1 = tk.Label(text="Reddit Video Generator Bot", font=('ariel', 20, 'bold'))
    label1.place(x=80, y=10)

    label1 = tk.Label(text="Slide Background Color ", font=("Times new roman", 16))
    label1.place(x=100, y=100)
    entryusr = Checkbutton(text="Black", variable=slbk)
    entryusr.place(x=350, y=100)
    entryusr = Checkbutton(text="White", variable=slbkw)
    entryusr.place(x=420, y=100)
    label2 = tk.Label(text="Fonts Color", font=("Times new roman", 16))
    label2.place(x=100, y=160)
    entrypass = Checkbutton(text="Black", variable=fntbk)
    entrypass.place(x=350, y=160)
    entrypass = Checkbutton(text="White", variable=fntwh)
    entrypass.place(x=420, y=160)
    label3 = tk.Label(text="Voice ", font=("Times new roman", 16))
    label3.place(x=100, y=220)
    entrypass = Checkbutton(text="Female", variable=voifem)
    entrypass.place(x=350, y=220)
    entrypass = Checkbutton(text="Male", variable=voimal)
    entrypass.place(x=420, y=220)
    label4 = tk.Label(text="Script", font=("Times new roman", 16))
    label4.place(x=100, y=280)
    entrypass = Checkbutton(text="Auto", variable=scpaut)
    entrypass.place(x=350, y=280)
    entrypass = Checkbutton(text="Manual", variable=scpman)
    entrypass.place(x=420, y=280)

    subjectlabel = tk.Label(text="Total Comments :", font=("Times new roman", 16))
    subjectlabel.place(x=100, y=340)
    entrysub = tk.Entry(window, font=('ariel', 12, 'bold'), bd=6, insertwidth=6, bg="yellow",
                        justify='left', textvariable=cmnts)
    entrysub.place(x=350, y=340)
    # entrypass = Checkbutton(text="upload on youtube", variable=yt)
    # entrypass.place(x=100, y=400)



    button1 = tk.Button(window, text="Start", bg="green", command=textfilegenerator)
    button1.place(x=240, y=500)
    button2 = tk.Button(window, text="Stop", bg="Red", command=quit)
    button2.place(x=280, y=500)

    window.mainloop()


main_screen()
