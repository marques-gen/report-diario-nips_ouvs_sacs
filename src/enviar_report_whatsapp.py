import os
import time
import webbrowser
import pyautogui
import pyperclip


# ===============================
# CONFIGURAÇÕES PADRÃO
# ===============================
WHATSAPP_URL = "https://web.whatsapp.com"

DEFAULT_WAIT_LOGIN = 15
DEFAULT_PAUSE = 0.5


# ===============================
# CONFIGURAÇÕES DE COORDENADAS

# ===============================
COORD_SEARCH = (207, 254)
COORD_ATTACH = (925, 1070)
COORD_PHOTO_VIDEO = (910, 682)


# ===============================
# SETUP INICIAL
# ===============================
def setup_pyautogui(pause: float = DEFAULT_PAUSE):
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = pause


# ===============================
# VALIDAÇÕES
# ===============================
def validar_imagem(caminho_imagem: str):
    if not os.path.exists(caminho_imagem):
        raise FileNotFoundError(f"Imagem não encontrada: {caminho_imagem}")


# ===============================
# AÇÕES
# ===============================
def abrir_whatsapp_web(tempo_espera: int = DEFAULT_WAIT_LOGIN):
    webbrowser.open(WHATSAPP_URL)
    time.sleep(tempo_espera)


def buscar_contato(nome_contato: str):
    pyautogui.click(*COORD_SEARCH)
    time.sleep(1)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    pyautogui.write(nome_contato)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)


def abrir_menu_anexo():
    pyautogui.click(*COORD_ATTACH)
    time.sleep(1)


def selecionar_foto_video():
    pyautogui.click(*COORD_PHOTO_VIDEO)
    time.sleep(2)


def anexar_imagem(caminho_imagem: str):
    pyperclip.copy(caminho_imagem)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(3)


def digitar_mensagem(mensagem: str):
    pyperclip.copy(mensagem)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)


def enviar():
    pyautogui.press("enter")


# ===============================
# FUNÇÃO ORQUESTRADORA
# ===============================
def enviar_mensagem_com_imagem(
    contato: str,
    mensagem: str,
    imagem: str,
    tempo_login: int = DEFAULT_WAIT_LOGIN
):
    validar_imagem(imagem)
    setup_pyautogui()

    abrir_whatsapp_web(tempo_login)
    buscar_contato(contato)

    abrir_menu_anexo()
    selecionar_foto_video()
    anexar_imagem(imagem)

    digitar_mensagem(mensagem)
    enviar()

    print("Mensagem e imagem enviadas com sucesso")

