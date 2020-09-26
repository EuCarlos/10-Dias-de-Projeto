from __future__ import unicode_literals
import youtube_dl
import urllib
import shutil
from tkinter import *

ydl_opts = {}
corBG = '#e63946'
cor1 = '#1d3557'

def baixar_Video():
    Url = str(FQuantC.get())
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([Url])

jan = Tk()

jan.title('DOWNLOAD DE VIDEOS DO YOUTUBE')
jan['bg'] = corBG
jan.geometry('300x320+500+300')
jan.resizable(width=False, height=False)

txt1 = Label(jan, text='BAIXAR VIDEO DO YOUTUBE', bg=cor1, foreground='white').pack(side=TOP, fill=X)
txt2 = Label(jan, text='Informe a URL do video \npara poder baixar', bg=corBG).place(x=70, y=100)
Link = Entry(jan)
Link.place(x=70, y=140)
btnBaixaVideo = Button(jan, width='15', text='BAIXAR VIDEO', fg='white', bg=cor1, command=baixar_Video).place(x=80, y=180)

jan.mainloop()
