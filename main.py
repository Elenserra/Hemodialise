import json
from modelo_2 import problema_transporte_equidade
from modelo_PLI import carregar_dados, carregar_jsons, problema_transporte_classico

def salvar_resultado_json(resultado, nome_arquivo):
    """
    Salvar o resultado do modelo em um arquivo JSON.
    """
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=4)
        print(f"\nArquivo salvo com sucesso: {nome_arquivo} \n")
    except Exception as e:
        print(f"\nErro ao salvar arquivo JSON: {e}\n")


def main():
    # Carregar os arquivos JSON
    caminho_demanda = "JSON/demanda.json"
    caminho_oferta = "JSON/oferta.json"
    caminho_distancias = "JSON/distancia.json"

    json_origens_data, json_destinos_data, json_distancias_data = carregar_jsons(
        caminho_demanda,
        caminho_oferta,
        caminho_distancias
    )

    # Processar dados
    origens, destinos, demanda, oferta, distancia = carregar_dados(
        json_origens_data,
        json_destinos_data,
        json_distancias_data
    )

      # Modelo 1 – PLI Clássico
    resultado_classico = problema_transporte_classico(
        origens, destinos, demanda, oferta, distancia
    )
    # Salvar o resultado 1
    salvar_resultado_json(resultado_classico, "resultado_PLI.json")

    # Modelo 2 – Equidade
    resultado_equidade = problema_transporte_equidade(
        origens, destinos, demanda, oferta, distancia
    )
    # Salvar o resultado 2
    salvar_resultado_json(resultado_equidade, "resultado_PLIM_equidade.json")



if __name__ == "__main__":
    main()
