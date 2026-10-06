# Projeto Hemodiálise

Projeto desenvolvido para apoiar a **ampliação do acesso de pacientes ao tratamento de hemodiálise no estado do Maranhão**, utilizando modelos computacionais de **Programação Linear Inteira (PLI)** e técnicas de otimização.

O projeto busca utilizar modelos matemáticos para auxiliar na tomada de decisões relacionadas à alocação e ao atendimento de pacientes que necessitam de tratamento de hemodiálise, contribuindo para uma melhor utilização dos recursos disponíveis.

## Objetivo

O objetivo do projeto é utilizar modelos de otimização para auxiliar no **planejamento do acesso de pacientes ao tratamento de hemodiálise**, considerando os recursos disponíveis, a demanda por atendimento, a oferta das unidades de tratamento e as distâncias entre os municípios.

Os modelos implementados permitem analisar diferentes possibilidades de alocação dos pacientes às unidades de tratamento e buscar soluções que contribuam para um atendimento mais adequado.

## Dados de entrada

Os dados utilizados pelos modelos estão armazenados em arquivos no formato **JSON**, localizados na pasta `JSON/`. Esses arquivos contêm as informações necessárias para representar as características do problema de distribuição e alocação dos pacientes.

### `demanda.json`

O arquivo [`demanda.json`](https://github.com/Elenserra/Hemodialise/blob/main/JSON/demanda.json) contém os dados referentes à quantidade de pacientes que necessitam de atendimento nos diferentes municípios considerados no estudo. Os dados de demanda são utilizados pelos modelos para identificar as necessidades de atendimento e determinar a alocação dos pacientes às unidades de tratamento.

### `oferta.json`

O arquivo [`oferta.json`](https://github.com/Elenserra/Hemodialise/blob/main/JSON/oferta.json) contém informações relacionadas à capacidade de atendimento disponível em cada unidade, sendo utilizados pelos modelos de otimização para estabelecer os limites de pacientes que podem ser encaminhados para cada unidade de tratamento.

### `distancia.json`

O arquivo [`distancia.json`](https://github.com/Elenserra/Hemodialise/blob/main/JSON/distancia.json) contém as informações referentes ao deslocamento dos pacientes até as unidades de atendimento. Dessa forma, as distâncias podem influenciar a definição da alocação dos pacientes, permitindo que o modelo busque soluções que considerem a proximidade entre o local de residência dos pacientes e as unidades de tratamento.

### Relação entre os arquivos

Os três arquivos de dados são utilizados de forma integrada pelos modelos de otimização:

* **`demanda.json`** → representa a necessidade de atendimento dos pacientes;
* **`oferta.json`** → representa a capacidade disponível nas unidades de tratamento;
* **`distancia.json`** → representa as distâncias entre os locais de demanda e as unidades de tratamento.

A utilização conjunta dessas informações permite que os modelos avaliem a relação entre **demanda, capacidade de atendimento e deslocamento**, buscando uma solução para a distribuição dos pacientes entre as unidades de tratamento de hemodiálise.

## Requisitos

Para executar o projeto, é necessário ter instalado:

* **Python 3**
* **PuLP 3.3.1**
* **CBC (COIN-OR Branch and Cut)** — solver utilizado pelo PuLP para resolver os modelos de otimização.

## Como executar

Acesse a pasta do projeto e execute o arquivo `main.py` para realizar a execução dos modelos e obter a solução do problema:

```bash
python3 main.py
```

O arquivo `main.py` é responsável pela execução dos modelos de otimização implementados, bem como pela apresentação dos resultados obtidos.

Esses resultados permitem analisar a **distribuição dos pacientes entre as unidades de tratamento de hemodiálise do estado do Maranhão**, contribuindo para a avaliação e o planejamento do acesso dos pacientes ao tratamento.

## Visualização dos resultados

Para visualizar graficamente os resultados obtidos pelos modelos, execute:

```bash
python3 gráfico.py
```

O arquivo `gráfico.py` é responsável pela geração dos gráficos utilizados para auxiliar na análise e interpretação dos resultados obtidos a partir dos modelos de otimização.

## Considerações

O projeto utiliza **modelos matemáticos e técnicas de otimização** como ferramentas de apoio ao planejamento do acesso de pacientes ao tratamento de hemodiálise.

A integração dos dados de **demanda, oferta e distância** permite representar diferentes aspectos do problema de alocação dos pacientes, fornecendo informações que podem auxiliar na análise da distribuição dos atendimentos entre as unidades de tratamento.

Os resultados obtidos pelos modelos devem ser interpretados como **apoio à tomada de decisão**, considerando as características, restrições e recursos definidos no problema.

---

**Projeto Hemodiálise**
*Modelos computacionais para apoio ao planejamento e ao acesso de pacientes ao tratamento de hemodiálise no estado do Maranhão.*
