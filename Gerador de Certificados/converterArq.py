from win32com import client
import win32api
import os

def Excel2Pdf(input_file, output_file):
    app = client.DispatchEx("Excel.Application")
    app.Interactive = False
    app.Visible = False
    Workbook = app.Workbooks.Open(input_file)
    try:
        Workbook.ActiveSheet.ExportAsFixedFormat(0, output_file)
    except Exception as e:
        print("Falha ao converter em formato PDF. Confirme se o ambiente atende a todos os requisitos e tente novamente")
        print(str(e))
    finally:
        Workbook.Close()
def apagaArq(input_file):
    os.remove(input_file)
