from tkinter import *
from tkinter.scrolledtext import ScrolledText
import win32clipboard
import webbrowser

corBG = '#D8F3DC'
cor1 = '#40916c'
cor2 = '#6c757d'

def callback(Link):
    webbrowser.open_new(Link)

def Gerador_Link():
    def btn_Copiar():
        copiado = str(Link)
        print('\033[1;33;41m TEXTO COPIADO \033[0;0m')
        # set clipboard data
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(copiado)
        win32clipboard.CloseClipboard()
    Form_NTel = str(NTel.get())
    Form_cx_msg = str(cx_msg.get())
    print('Gerando Link...')
    Link = str('https://api.whatsapp.com/send?phone=55{}&text={}'.format(Form_NTel, Form_cx_msg))
    lb4['text'] = Link
    lb4.bind("<Button-1>", lambda e: callback(Link))
    btnCopiar = Button(janela, width='15', text='COPIAR LINK', fg='white', bg=cor2, command=btn_Copiar).place(x=200, y=230)
    lb5 = Label(janela, text='**Clique no Link abaixo para abrir no navegador', fg='red', bg=corBG).place(x=125, y=150)

def btn_Sair():
    janela.destroy()

def btn_Enviar():
    print('ABRINDO NAVEGADOR...')

janela = Tk()
janela.title('WhatsApp Mensagem')
janela["bg"] = corBG
janela.geometry('500x320+500+300')
janela.resizable(width=False, height=False)

lb1 = Label(janela, text='WhatsApp API', bg=cor1, foreground='white').pack(side=TOP, fill=X)
lb2 = Label(janela, text='N° Telefone:', bg=corBG).place(x=100, y=50)
lb3 = Label(janela, text='Mensagem:', bg=corBG).place(x=100, y=100)
NTel = Entry(janela)
NTel.place(x=200, y=50)
cx_msg = Entry(janela)#ScrolledText(janela, width=15, height=5)
cx_msg.place(x=200, y=100)
lb4 = Label(janela, text='AQUI FICARARÁ SEU LINK', bg=cor1, foreground='white')
lb4.pack(side=BOTTOM, fill=X)

btnGerarLink = Button(janela, width='15', text='GERAR LINK', fg='white', bg=cor1, command=Gerador_Link).place(x=200, y=200)
btnSair = Button(janela, width='15', text='SAIR', fg='white', bg=cor1, command=btn_Sair).place(x=200, y=260)

janela.mainloop()
