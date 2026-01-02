
from time import sleep
from PIL import Image

def get_excel_frame(page):
    for frame in page.frames:
        if "excel" in (frame.url or "").lower():
            return frame
    return None

#=================================================================================
# captura_imagem.py
def selecionar_intervalo_nomeado(page, nome_intervalo):
    # Fecha overlays / ribbon
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)

    # Ir para intervalo nomeado
    page.keyboard.press("Control+g")
    page.wait_for_timeout(800)

    page.keyboard.type(nome_intervalo)
    page.wait_for_timeout(300)

    page.keyboard.press("Enter")
    page.wait_for_timeout(1500)
#=================================================================================
def ajustar_zoom(frame, nivel=200):
    frame.keyboard.press("Control+Alt+=")
    frame.wait_for_timeout(300)



#=================================================================================
def capturar_intervalo(page, path_img):
    frame = get_excel_frame(page)
    if not frame:
        raise Exception("❌ Frame do Excel não encontrado")

    # Aguarda QUALQUER canvas aparecer
    frame.wait_for_selector("canvas", timeout=60000)

    # Aguarda estabilização do render
    frame.wait_for_timeout(3000)

    canvases = frame.locator("canvas")
    total = canvases.count()

    if total == 0:
        raise Exception("❌ Nenhum canvas encontrado")

    # 🔥 Heurística usada pela comunidade:
    # pega o MAIOR canvas visível (área da planilha)
    maior = None
    maior_area = 0

    for i in range(total):
        c = canvases.nth(i)
        box = c.bounding_box()
        if box:
            area = box["width"] * box["height"]
            if area > maior_area:
                maior_area = area
                maior = c

    if not maior:
        raise Exception("❌ Canvas principal não identificado")

    maior.screenshot(path=path_img)
#=============================================================================

def converter_para_jpg(png, jpg):
    img = Image.open(png).convert("RGB")
    img.save(jpg, "JPEG", quality=95)




