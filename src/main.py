from atualizar_report import gerar_imagem_do_relatorio
from enviar_report_whatsapp import enviar_mensagem_com_imagem

CAMINHO_ARQUIVO = r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data\Report_Diário-Nips_Ouvs_Sacs.xlsx"
DESTINO_IMAGEM=r"C:\projects-soluctions\report-diario-nips_ouvs_sacs\data-viz\report_diario.png"

CONTATO = "MCP - Melhoria e Controle de Processos"

MENSAGEM = """
*Report TESTE - validar números/Regras*

Dr. Jorge, segue reporte diário de SAC, NIPs e Ouvidoria.


"""

IMAGEM = DESTINO_IMAGEM


if __name__ == "__main__":
    
    gerar_imagem_do_relatorio(
        caminho_arquivo=CAMINHO_ARQUIVO,
        nome_aba="Report1",
        intervalo="A2:O9",
        destino_imagem=DESTINO_IMAGEM,
        excel_visivel=False
    )

    enviar_mensagem_com_imagem(
        contato=CONTATO,
        mensagem=MENSAGEM,
        imagem=IMAGEM
    )


