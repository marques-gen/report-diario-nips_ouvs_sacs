import win32com.client as win32
import time


CAMINHO_ARQUIVO = r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data\Report_Diário.xlsx"
DESTINO_IMAGEM=r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data-viz\report_diario.png"

def fechar_excel_com_segurança(wb, excel):
    wb.Save()
    wb.Close(SaveChanges=True)
    time.sleep(2)
    excel.Quit()
    del wb
    del excel


excel = win32.Dispatch("Excel.Application")
excel.Visible = False
excel.DisplayAlerts = False

wb = excel.Workbooks.Open(CAMINHO_ARQUIVO)

# Atualizar tudo
wb.RefreshAll()

# Aguarda atualização terminar
while excel.CalculationState != 0:
    time.sleep(2)

print("Atualização concluída")

#Capturar intevalo e gerar imagem
from PIL import ImageGrab

sheet = wb.Sheets("Report1")
rng = sheet.Range("B2:N7")

rng.CopyPicture(Appearance=1, Format=2)
time.sleep(1)

img = ImageGrab.grabclipboard()
img.save(DESTINO_IMAGEM)

# Fechar excel
fechar_excel_com_segurança(wb,excel)
