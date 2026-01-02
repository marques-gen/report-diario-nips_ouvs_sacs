import requests

url = "https://prod-00.brazilsouth.logic.azure.com/..."  # URL do fluxo

payload = {
    "processo": "atualizacao_sharepoint",
    "usuario": "genelson",
    "data": "2026-01-01"
}

response = requests.post(url, json=payload, timeout=30)

if response.status_code == 200:
    print("Fluxo executado com sucesso")
else:
    print("Erro ao executar fluxo:", response.text)
