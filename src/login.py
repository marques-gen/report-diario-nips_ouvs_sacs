from playwright.sync_api import sync_playwright
import os

AUTH_FILE = "auth_state.json"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://login.microsoftonline.com/")

    print("Faça login MANUALMENTE e finalize a autenticação.")
    page.wait_for_timeout(60000)  # tempo para você logar

    # Salva cookies + localStorage
    context.storage_state(path=AUTH_FILE)

    print("Login salvo com sucesso")

    browser.close()
