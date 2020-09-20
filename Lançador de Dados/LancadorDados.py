from tkinter import *
import random

Dados = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
def btn_LancarDados():
    dancaDados1 = random.choice(Dados)
    dancaDados2 = random.choice(Dados)
    image1['file'] = dancaDados1
    image2['file'] = dancaDados2

jan = Tk()

jan.title('Lança Dados')
jan.resizable(width=False, height=False)
jan.geometry('300x120+500+300')


image1 = PhotoImage(file="dice1.png")
image2 = PhotoImage(file="dice6.png")
img1 = Label(jan, image=image1).place(x=100, y=20)
img2 = Label(jan, image=image2).place(x=160, y=20)

btnLancarDados = Button(jan, width='15', text='LANÇAR DADOS', fg='white', bg='black', command=btn_LancarDados).place(x=100, y=80)

jan.mainloop()
