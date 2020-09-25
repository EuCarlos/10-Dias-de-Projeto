from tkinter import *
from tkinter import messagebox
from random import choice
import win32clipboard


corBG = '#ff6b6b'#Rosa
cor1 = '#1a535c'#AzulEscuro
cor2 = '#f7fff7'#Branco
cor3 = '#ffe66d'#Amarelo


def gera_senha():
    def btn_Copiar():
        copiado = str(senha)
        print('\033[1;33;41m TEXTO COPIADO \033[0;0m')
        # set clipboard data
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(copiado)
        win32clipboard.CloseClipboard()
    NumChar = 0
    try:
        NumChar = int(FQuantC.get())
    except ValueError or UnboundLocalError:
        messagebox.showerror(title="ERRO", message="Informe um valor valido.")

    caracters = '!@#$%&*/*-+0123456789abcdefghijlmnopqrstuwvxzABCDEFGHIJKLMNOPQRSTUVWXZ'
    senha = ''
    for char in range(NumChar):
        senha += choice(caracters)
    lb3['text'] = senha
    btnCopiar = Button(janela, width='15', text='COPIAR SENHA', fg=cor2, bg='gray', command=btn_Copiar).place(x=200, y=200)
    lb3.pack(side=BOTTOM, fill=X)

janela = Tk()
janela.title('Gerador de Senhas')
janela['bg'] = cor3
janela.geometry('500x320+500+300')
janela.resizable(width=False, height=False)

lb1 = Label(janela, text='Gerador de Senhas', bg=cor1, foreground=cor2).pack(side=TOP, fill=X)
lb2 = Label(janela, text='Quantidade de Caracteres:', bg=cor3).place(x=177, y=50)
try:
    FQuantC = Entry(janela)
except ValueError or UnboundLocalError:
    print('Valor Incorreto')

FQuantC.place(x=189, y=75)
btnGera_Senha = Button(janela, width='15', text='GERAR SENHA', fg=cor2, bg=cor1, command=gera_senha).place(x=200, y=150)

lb3 = Label(janela, text=' ', bg=cor1, foreground=cor2)


janela.mainloop()
