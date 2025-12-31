
#bibliotecas necessarias, caso nao tenha instalada em sua maquina basta executar os comandos (pip instal....)
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time

#Abre o Chrome


#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
midia = r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data-viz\report_diario.png"

def aguardar_whatsapp_pronto(driver, timeout=60):
    wait = WebDriverWait(driver, timeout)

    # Sidebar de conversas (elemento mais estável do WhatsApp)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@aria-label="Lista de conversas"] | //div[@role="grid"]')
        )
    )

# Atualiza o ChromeDriver para a versão mais recente compatível
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://web.whatsapp.com/")
    print("Escaneie o QR Code...")
    time.sleep(20)

    aguardar_whatsapp_pronto(driver)
    print("WhatsApp carregado com sucesso")

except Exception as e:
    print(f"Erro ao carregar o WhatsApp Web: {e}")
    driver.quit()
    raise

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    wait = WebDriverWait(driver, 30)

    campo_pesquisa = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@contenteditable="true"][@role="textbox"]')
        )
    )

    campo_pesquisa.click()
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


# Adicionar logs detalhados na função de envio de imagem

def enviar_imagem_com_mensagem(caminho_imagem, mensagem):
    try:
        print("Verificando se a conversa está aberta...")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//footer')
            )
        )
        print("Conversa aberta com sucesso.")

        print("Procurando input para envio de arquivo...")
        file_inputs = driver.find_elements(By.XPATH, '//input[@type="file"]')
        if not file_inputs:
            raise Exception("input[type=file] não encontrado. Verifique se o seletor está correto.")

        print("Input encontrado. Enviando arquivo...")
        file_inputs[-1].send_keys(caminho_imagem)

        print("Aguardando preview da mídia...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[contains(@class, "_1JpRT")]')  # Classe do preview da mídia
            )
        )
        print("Preview carregado com sucesso.")

        print("Inserindo legenda...")
        driver.execute_script("""
            const el = document.activeElement;
            el.innerText = arguments[0];
            el.dispatchEvent(new InputEvent('input', { bubbles: true }));
        """, mensagem)

        time.sleep(1)

        print("Clicando no botão de enviar...")
        driver.execute_script("""
            const footer = document.querySelector('footer');
            if (!footer) return;

            const buttons = footer.querySelectorAll('button');
            for (const btn of buttons) {
                const svg = btn.querySelector('svg');
                if (!svg) continue;

                const paths = svg.querySelectorAll('path');
                for (const p of paths) {
                    const d = p.getAttribute('d') || '';
                    if (d.length > 100) { // ícone de enviar costuma ter path grande
                        btn.click();
                        return;
                    }
                }
            }
        """)

        print(f"Mensagem enviada com sucesso para o contato com a imagem: {caminho_imagem}")

    except Exception as e:
        print(f"Erro ao enviar mensagem com imagem: {e}")
        raise


#Percorre todos os contatos/Grupos e envia as mensagens
contatos = ["link conteudo"]

mensagem = "Bom dia grupo, que o dia de vocês seja iluminado"
imagem = r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data-viz\report_diario.png"

for contato in contatos:
    buscar_contato(contato)
    enviar_imagem_com_mensagem(imagem, mensagem)
    time.sleep(50)
