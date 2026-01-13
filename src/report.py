import pandas as pd

df = pd.DataFrame({
    "Vendedor": [
        "Sofia Oliveira", "Lucas Santos", "Amanda Pereira", "Pedro Almeida",
        "Isabela Lima", "Gabriel Costa", "Juliana Oliveira", "Mateus Silva"
    ],
    "Filial": ["SP", "RJ", "MG", "ES", "SP", "RJ", "MG", "ES"],
    "Valor": [
        30500.90, 22800.75, 39100.30, 37300.20,
        28300.60, 34900.60, 25000.50, 48000.80
    ]
})
print(df.head())

#================================================================================
import matplotlib.pyplot as plt
from matplotlib.table import Table

def gerar_imagem_tabela(df, caminho_saida):
    total = df["Valor"].sum()
    df_plot = df.copy()

    fig, ax = plt.subplots(figsize=(8, len(df_plot) * 0.35 + 2))
    ax.axis("off")

    # Títulos
    ax.text(
        0.5, 1.05,
        "FATURAMENTO TOTAL\n(01/JAN - 15/JAN)",
        ha="center", va="center",
        fontsize=14, fontweight="bold",
        color="white",
        transform=ax.transAxes,
        bbox=dict(facecolor="#0B7A6E", edgecolor="none", pad=10)
    )

    tabela = Table(ax, bbox=[0, 0, 1, 0.95])

    colunas = ["VENDEDORES", "FILIAL", "VALOR"]
    larguras = [0.55, 0.15, 0.30]
    altura = 1 / (len(df_plot) + 2)

    # Cabeçalho
    for i, col in enumerate(colunas):
        tabela.add_cell(
            0, i, larguras[i], altura,
            text=col,
            loc="center",
            facecolor="#00A38C",
            edgecolor="white"
        )

    max_val = df_plot["Valor"].max()

    # Linhas
    for i, row in enumerate(df_plot.itertuples(), start=1):
        tabela.add_cell(i, 0, larguras[0], altura,
                         text=row.Vendedor, loc="left",
                         facecolor="#E6E6E6")

        tabela.add_cell(i, 1, larguras[1], altura,
                         text=row.Filial, loc="center",
                         facecolor="#F2F2F2")

        cor_valor = "#C6EFCE" if row.Valor >= max_val * 0.7 else "white"

        tabela.add_cell(
            i, 2, larguras[2], altura,
            text=f"R$ {row.Valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            loc="right",
            facecolor=cor_valor
        )

    # Linha total
    i_total = len(df_plot) + 1
    tabela.add_cell(i_total, 0, larguras[0] + larguras[1], altura,
                     text="Total", loc="left",
                     facecolor="#00A38C")

    tabela.add_cell(
        i_total, 2, larguras[2], altura,
        text=f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
        loc="right",
        facecolor="#00A38C"
    )

    ax.add_table(tabela)

    plt.savefig(caminho_saida, dpi=200, bbox_inches="tight")
    plt.close()

#===================================================================

gerar_imagem_tabela(
    df,
    "faturamento_total.png"
)


