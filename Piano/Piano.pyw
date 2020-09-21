from tkinter import *
import winsound

musica = []
d = 500
mfr = 2
def C():
    winsound.Beep(132*mfr, d)
def Cs():
    winsound.Beep(137*mfr, d)
def D():
    winsound.Beep(148*mfr, d)
def Ds():
    winsound.Beep(154*mfr, d)
def E():
    winsound.Beep(165*mfr, d)
def F():
    winsound.Beep(171*mfr, d)
def Fs():
    winsound.Beep(183*mfr, d)
def G():
    winsound.Beep(198*mfr, d)
def Gs():
    winsound.Beep(206*mfr, d)
def A():
    winsound.Beep(220*mfr, d)
def As():
    winsound.Beep(229*mfr, d)
def B():
    winsound.Beep(247*mfr, d)


jan = Tk()
jan.title('Piano Notas Musicais')
jan['bg'] = '#523F38'
jan.geometry('337x320+500+300')
jan.resizable(width=False, height=False)

lb2 = Label(jan, text='Github.com/EuCarlos/', fg='white', bg='#523F38').place(x=100, y=50)

btnDo = Button(jan, width='5', height=10, text='C', fg='black', bg='white',command=C).place(x=5, y=130)
btnRe = Button(jan, width='5', height=10, text='D', fg='black', bg='white',command=D).place(x=52, y=130)
btnMi = Button(jan, width='5', height=10, text='E', fg='black', bg='white',command=E).place(x=99, y=130)
btnFa = Button(jan, width='5', height=10, text='F', fg='black', bg='white',command=F).place(x=146, y=130)
btnSol = Button(jan, width='5', height=10, text='G', fg='black', bg='white',command=G).place(x=193, y=130)
btnLa = Button(jan, width='5', height=10, text='A', fg='black', bg='white',command=A).place(x=240, y=130)
btnSi = Button(jan, width='5', height=10, text='B', fg='black', bg='white',command=B).place(x=287, y=130)
btnDoS = Button(jan, width='2', height=5, text='C#', fg='white', bg='black',command=Cs).place(x=37, y=130)
btnRes = Button(jan, width='2', height=5, text='D#', fg='white', bg='black',command=Ds).place(x=85, y=130)
btnFaS = Button(jan, width='2', height=5, text='F#', fg='white', bg='black',command=Fs).place(x=181, y=130)
btnSolS = Button(jan, width='2', height=5, text='G#', fg='white', bg='black',command=Gs).place(x=229, y=130)
btnLaS = Button(jan, width='2', height=5, text='A#', fg='white', bg='black',command=As).place(x=277, y=130)

jan.mainloop()
