def abrir_whatsapp(page):
    page.goto("https://web.whatsapp.com/")

    # Aguarda WhatsApp pronto (login ou já logado)
    page.wait_for_selector(
        "div[contenteditable='true'][data-tab='3'], canvas",
        timeout=60000
    )


def enviar_imagem_whatsapp(page, contato, imagem, mensagem):

    # 🔍 Buscar contato
    search = page.get_by_role("textbox", name="Caixa de texto de pesquisa")
    search.fill(contato)
    page.wait_for_timeout(1500)
    page.keyboard.press("Enter")

    # 🟢 Aguarda conversa abrir
    campo_msg = page.locator("footer div[contenteditable='true']")
    campo_msg.wait_for(state="visible", timeout=30000)

    # ➕ Abrir menu anexar
    anexar = page.locator("button[aria-label='Anexar'], span[data-icon='plus']")
    anexar.first.click()

# 📷 Clicar explicitamente em "Fotos e vídeos"
    fotos_videos = page.get_by_role("menuitem", name="Fotos e vídeos")
    fotos_videos.wait_for(state="visible", timeout=10000)
    fotos_videos.click()

# 📎 Input correto
    file_input = page.locator("input[type='file']").first
    file_input.set_input_files(imagem)


    # 🖼️ Aguarda preview da imagem (ESTE É O PONTO-CHAVE)
    preview_img = page.locator("img[src^='blob:']")
    preview_img.wait_for(state="visible", timeout=30000)

    # ✍️ Campo de legenda (mensagem junto da imagem)
    legenda = page.locator(
        "div[contenteditable='true'][data-tab][aria-label]"
    ).last
    legenda.wait_for(state="visible", timeout=10000)
    legenda.fill(mensagem)

    # 🚀 Botão enviar (pai do ícone)
    botao_enviar = page.locator(
        "button:has(span[data-icon='wds-ic-send-filled'])"
    )

    botao_enviar.wait_for(state="visible", timeout=30000)

    # 🔥 CLIQUE FORÇADO (prática aceita para WhatsApp Web)
    botao_enviar.click(force=True)

    # ✅ Confirma envio (preview desaparece)
    preview_img.wait_for(state="detached", timeout=30000)






