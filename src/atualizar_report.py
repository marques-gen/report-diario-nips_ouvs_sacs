import time
import win32com.client as win32
from PIL import ImageGrab


def iniciar_excel(visible: bool = False):
    excel = win32.Dispatch("Excel.Application")
    excel.Visible = visible
    excel.DisplayAlerts = False
    return excel


def abrir_workbook(excel, caminho_arquivo: str):
    return excel.Workbooks.Open(caminho_arquivo)


def atualizar_workbook(wb, excel, intervalo_checagem: int = 2):
    wb.RefreshAll()

    # Aguarda queries assíncronas (Power Query / ODBC / Web)
    excel.CalculateUntilAsyncQueriesDone()

    # Garante que os cálculos finalizaram
    while excel.CalculationState != 0:
        time.sleep(intervalo_checagem)

    print("Atualização concluída")

    while excel.CalculationState != 0:
        time.sleep(intervalo_checagem)

    print("Atualização concluída")


def capturar_intervalo_como_imagem(
    wb,
    nome_aba: str,
    intervalo: str,
    destino_imagem: str,
    espera_clipboard: int = 1
):
    sheet = wb.Sheets(nome_aba)
    rng = sheet.Range(intervalo)

    rng.CopyPicture(Appearance=1, Format=2)
    time.sleep(espera_clipboard)

    img = ImageGrab.grabclipboard()
    if img is None:
        raise RuntimeError("Não foi possível capturar a imagem do intervalo.")

    img.save(destino_imagem)


def fechar_excel_com_segurança(wb, excel, espera_fechamento: int = 2):
    try:
        wb.Save()
        wb.Close(SaveChanges=True)
        time.sleep(espera_fechamento)
    finally:
        excel.Quit()
        del wb
        del excel


def gerar_imagem_do_relatorio(
    caminho_arquivo: str,
    nome_aba: str,
    intervalo: str,
    destino_imagem: str,
    excel_visivel: bool = False
    ):
    excel = iniciar_excel(visible=excel_visivel)

    try:
        wb = abrir_workbook(excel, caminho_arquivo)
        atualizar_workbook(wb, excel)
        capturar_intervalo_como_imagem(
            wb,
            nome_aba=nome_aba,
            intervalo=intervalo,
            destino_imagem=destino_imagem
        )
    finally:
        fechar_excel_com_segurança(wb, excel)

