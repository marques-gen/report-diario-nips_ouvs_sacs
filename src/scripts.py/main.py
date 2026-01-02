import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from atualiza_consulta import atualizar_consultas_excel
from captura_imagem import selecionar_intervalo_nomeado, capturar_intervalo,converter_para_jpg
from envia_mensagem_whats import abrir_whatsapp,enviar_imagem_whatsapp

load_dotenv()

EXCEL_URL = os.getenv("EXCEL_URL")
AUTH_FILE = "auth_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=50
    )

    # Usa sessão persistida (SEM LOGIN)
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()

    # 1 Abre direto o Excel Online
    page.goto(EXCEL_URL)

    # 2 Caso esteja em modo leitura → Editar
    try:
        editar = page.get_by_role("button", name="Editar")
        if editar.count() > 0:
            editar.click()
            page.wait_for_timeout(3000)
    except:
        pass

    # 3 Aguarda iframe do Excel
    page.wait_for_selector("iframe[name^='WacFrame_Excel']", timeout=60000)
    page.wait_for_timeout(5000)

    # Debug visual
    page.screenshot(path="excel_carregado.png", full_page=True)

    # 4 Atualiza consultas
    print("Atualizando consultas no Excel Online...")
    atualizar_consultas_excel(page)

    # 5 Aguarda finalizar (Excel é assíncrono)
    print("Aguardando Excel finalizar atualização...")
    page.wait_for_timeout(30000)  # ajuste conforme tempo real

    print("Planilha atualizada com sucesso")
#===============================================================================

    MENSAGEM = """
                *Relatório Diário*

                Segue abaixo o status atualizado.

                """


    # Excel
    selecionar_intervalo_nomeado(page, "report1")
    capturar_intervalo(page, "relatorio.png")

    # WhatsApp
    abrir_whatsapp(page)
    converter_para_jpg("relatorio.png", "relatorio.jpg")
    enviar_imagem_whatsapp(
    page,
    contato="Link conteudo",
    imagem="relatorio.jpg",
    mensagem=MENSAGEM
)
    #page.wait_for_timeout(5000)
    input("Mensagem enviada. Pressione ENTER para fechar.")
    browser.close()
