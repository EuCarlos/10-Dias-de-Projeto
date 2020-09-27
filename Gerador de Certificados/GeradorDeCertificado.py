from tkinter import *
from openpyxl import load_workbook
from datetime import date
#Criar um Entry para o "Nome do Curso"
#Criar uma def para salvar como PDF
'''
# Fazer o programa ler o arquivo .txt(com nomes do anulos)
# salvar o arquivo em um mainloop
    for i in range(len('nome_da_variavel_dos_Aqruivo))
        pegar nomes[i]
        planilha.cell(row=linhaQueONomeVaiFicar, column=ColunadoDoNome, value=pegar nome[i])
        salvaOArquivo('Certificado{}.txt'.format(i))
'''

def getValores():
    nome = FNome.get()
    prof = FProf.get()
    planilha1.cell(row=7,column=5, value=nome)
    planilha1.cell(row=26, column=2, value=date)
    planilha1.cell(row=26, column=11, value=prof)
    arquivo_excel.save("Certificado.xlsx")

date_today = date.today()
date = '{}/{}/{}'.format(date_today.day, date_today.month, date_today.year)
corBG = '#f2cc8f'
cor1 = '#81b29a'

caminho = 'Modelo.xlsx'
arquivo_excel = load_workbook(caminho)
planilha1 = arquivo_excel.active

jan = Tk()
jan.title('Gerar Certificado')
jan['bg'] = corBG
jan.geometry('300x200+500+300')
jan.resizable(width=False, height=False)

txt1 = Label(jan, text='GERAR CERTIFICADO', bg=cor1, fg='black').pack(side=TOP, fill=X)
txt2 = Label(jan, text='NOME COMPLETO:', bg=corBG, fg='black').place(x=20, y=50)
FNome = Entry(jan)
FNome.place(x=155, y=50)
txt3 = Label(jan, text='NOME DO PROFESSOR:', bg=corBG, fg='black').place(x=20, y=85)
FProf = Entry(jan)
FProf.place(x=155, y=85)
btnGerar = Button(jan, width='20', text='GERAR CERTIFICADO', fg='white', bg=cor1, command=getValores).place(x=85, y=120)

jan.mainloop()
