from playwright.sync_api import Page

def atualizar_consultas_excel(page: Page):
    frame = page.frame(name="WacFrame_Excel_0")

    if not frame:
        raise Exception("Iframe do Excel não encontrado")

    # Aguarda Ribbon
    aba_dados = frame.get_by_role("tab", name="Dados", exact=True)
    aba_dados.wait_for(state="visible", timeout=60000)
    aba_dados.click()

    frame.wait_for_timeout(1500)

    # Botão Atualizar Tudo (layout novo)
    btn_refresh_all = frame.get_by_role("button", name="Atualizar Tudo")
    btn_refresh_all.wait_for(state="visible", timeout=30000)
    btn_refresh_all.click()
