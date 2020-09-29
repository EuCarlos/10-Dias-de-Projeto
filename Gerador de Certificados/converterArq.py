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
        print("Failed to convert in PDF format.Please confirm environment meets all the requirements  and try again")
        print(str(e))
    finally:
        Workbook.Close()
def apagaArq(input_file):
    os.remove(input_file)
