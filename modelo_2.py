import pulp
import json
import unicodedata

# Padronizar os nomes
def normalizar(nome):
    if nome is None:
        return ""
    nome = nome.strip().upper()
    nome = unicodedata.normalize('NFD', nome)
    nome = "".join(c for c in nome if unicodedata.category(c) != 'Mn')
    return nome

def carregar_jsons(arquivo_demanda, arquivo_oferta, arquivo_distancias):
    """
    Carregar os três arquivos JSON do modelo.

    Parâmetros:
        arquivo_demanda : caminho do JSON com origens
        arquivo_oferta : caminho do JSON com destinos
        arquivo_distancias : caminho do JSON com matriz de distâncias

    Retorna:
        dict: (json_origem, json_destino, json_distancias)
    """
    try:
        with open(arquivo_demanda, "r", encoding="utf-8") as f1:
            json_origem = json.load(f1)

        with open(arquivo_oferta, "r", encoding="utf-8") as f2:
            json_destino = json.load(f2)

        with open(arquivo_distancias, "r", encoding="utf-8") as f3:
            json_distancias = json.load(f3)

        return json_origem, json_destino, json_distancias

    except FileNotFoundError as e:
        print("Arquivo não encontrado:", e.filename)
        raise e
    except json.JSONDecodeError:
        print("Erro ao ler um dos JSONs — arquivo com formatação inválida.")
        raise

def carregar_dados(json_origens, json_destinos, json_distancias):

    # 1. Ler origens
    origens = [ normalizar (o["nome"]) for o in json_origens["origem"]]

    demanda = {
        normalizar (o["nome"]): o["demanda"]
        for o in json_origens["origem"]
    }

    # 2. Ler destinos
    destinos = [ normalizar (d["nome"]) for d in json_destinos["destinos"]]

    oferta = {
        normalizar (d["nome"]): d["oferta"]
        for d in json_destinos["destinos"]
    }

    # 3. Ler distâncias
    distancia = {}

    for item in json_distancias["custos_distancias"]:
        origem = normalizar (item["origem"])
        destino = normalizar (item["destino"])
        dist = float(item["distancia"]) if item["distancia"] not in [None, ""] else 0.0

        distancia[(origem, destino)] = dist

    return origens, destinos, demanda, oferta, distancia

def problema_transporte_equidade(origens, destinos, demanda, oferta, distancia):

    # Criar o modelo de minimização
    modelo = pulp.LpProblem(
        "Modelo_Transporte_Hemodialise_Equidade",
        pulp.LpMinimize
    )

    # Variáveis x[i,j] – fluxo de pacientes
    x = pulp.LpVariable.dicts(
        "x",
        [(i, j) for i in origens for j in destinos],
        lowBound=0,
        cat="Integer"
    )

    # Variáveis y[i,j] – indica se a rota é usada
    y = pulp.LpVariable.dicts(
        "y",
        [(i, j) for i in origens for j in destinos],
        cat="Binary"
    )

    # Variável lambda – maior distância individual
    lambda_var = pulp.LpVariable(
        "lambda",
        lowBound=0,
        cat="Continuous"
    )

    # Big-M (total de pacientes)
    M = sum(demanda.values())

    # Função Objetivo
    # Minimize a maior distância individual
    # Min λ
    modelo += lambda_var

    # Restrições do modelo:
    # 1. Atendimento total da demanda
    # ∑​ Xij ​= Demi​
    for i in origens:
        modelo += (
            pulp.lpSum(x[(i, j)] for j in destinos) == demanda[i]
        )

    # 2. Capacidade das clínicas
    # ∑​ Xij ​≤ Capj​
    for j in destinos:
        modelo += (
            pulp.lpSum(x[(i, j)] for i in origens) <= oferta[j]
        )

    # 3. Ligação X -> Y (Big-M)
    # Xij ​≤ M ⋅ Yij​
    for i in origens:
        for j in destinos:
            modelo += x[(i, j)] <= M * y[(i, j)]

    # 4. Restrição de equidade (Min–Max)
    # λ ≥ Cij ​⋅ Yij​
    for i in origens:
        for j in destinos:
            dij = distancia.get((i, j), 9999999)
            modelo += lambda_var >= dij * y[(i, j)]

    # Resolver
    modelo.solve()

    # Retornar resultados em formato JSON
    resultado_json = {
        "status": pulp.LpStatus[modelo.status],
        "lambda": round(pulp.value(lambda_var), 2),
        "custo_total": 0.0,
        "alocacoes": []
    }

    custo_total = 0.0
    
    for i in origens:
        for j in destinos:
            valor = x[(i, j)].value()
            if valor is None:
                continue
            valor = int(valor)

            if valor > 0:
                dij = distancia.get((i, j), 0)

                custo_total += valor * dij

                resultado_json["alocacoes"].append({
                    "origem": i,
                    "destino": j,
                    "demanda": valor,
                    "distancia": dij
                })
                
    resultado_json["custo_total"] = round(custo_total, 2)

    return resultado_json
