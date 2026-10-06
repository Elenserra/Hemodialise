import json
import matplotlib.pyplot as plt

def carregar_resultado(caminho):
    with open(caminho, "r") as f:
        return json.load(f)


def plotar_alocacoes(resultado, titulo):
    alocacoes = resultado["alocacoes"]

    # Ordena as distâncias em ordem decrescente
    distancias = sorted(
        [a["distancia"] for a in alocacoes],
        reverse=True
    )

    plt.figure(figsize=(8,4))
    plt.bar(range(len(distancias)), distancias)

    plt.ylabel("Distância")
    plt.xlabel("Alocações")
    plt.title(titulo)

    # Remove os rótulos do eixo X
    plt.xticks([])

    plt.tight_layout()
    plt.show()


# Carregar resultados
resultado_PLI = carregar_resultado("resultado_PLI.json")
resultado_PLIM_equidade = carregar_resultado("resultado_PLIM_equidade.json")

# Plotar

plotar_alocacoes(
    resultado_PLI,
    "Modelo PLI – Distância por Alocação"
)

plotar_alocacoes(
    resultado_PLIM_equidade,
    "Modelo PLIM com Equidade – Distância por Alocação"
)

