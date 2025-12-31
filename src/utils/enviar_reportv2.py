import pyautogui
import pyperclip
import time
import webbrowser
import os

# ===============================
# CONFIGURAÇÕES
# ===============================
CONTATO = "link conteudo"
MENSAGEM = """
Bom dia!

Segue o relatório atualizado.

"""
IMAGEM = r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data-viz\report_diario.png"

# ===============================
# VALIDAÇÕES
# ===============================
if not os.path.exists(IMAGEM):
    raise FileNotFoundError("Imagem não encontrada")

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5

# ===============================
# 1. Abrir WhatsApp Web
# ===============================
webbrowser.open("https://web.whatsapp.com")
time.sleep(15)  # tempo para carregar/login

#===============================
# 2. Buscar contato/grupo (SEM BARRA)
# ===============================
pyautogui.click(188, 204)  # 🔍 campo de busca (AJUSTE)
time.sleep(1)

pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")

pyautogui.write(CONTATO)
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)


# ===============================
# 3. Abrir menu de anexo
# ===============================
pyautogui.click(702, 981)  # 📎 (AJUSTE ESSA POSIÇÃO)
time.sleep(1)

# ===============================
# 4. Clicar em "Fotos e vídeos"
# ===============================
pyautogui.click(714, 582)  # (AJUSTE)
time.sleep(2)

# ===============================
# 5. Colar caminho da imagem
# ===============================
pyperclip.copy(IMAGEM)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)  # MUITO IMPORTANTE: esperar preview

# ===============================
# 6. Digitar mensagem
# ===============================
pyperclip.copy(MENSAGEM)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# ===============================
# 7. Enviar
# ===============================
pyautogui.press("enter")

print(" Mensagem e imagem enviadas com sucesso")

