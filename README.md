# Projeto Hemodiálise

Projeto desenvolvido para apoiar a **ampliação do acesso de pacientes ao tratamento de hemodiálise do estado do Maranhão**, utilizando modelos computacionais de **Programação Linear Inteira (PLI)** e técnicas de otimização.

O projeto busca utilizar modelos matemáticos para auxiliar na tomada de decisões relacionadas à alocação e ao atendimento de pacientes que necessitam de tratamento de hemodiálise, contribuindo para uma melhor utilização dos recursos disponíveis.

## Objetivo

O objetivo do projeto é utilizar modelos de otimização para auxiliar no **planejamento do acesso de pacientes ao tratamento de hemodiálise**, considerando os recursos disponíveis e as necessidades de atendimento.

Os modelos implementados permitem analisar diferentes possibilidades de alocação e buscar soluções que contribuam para um atendimento mais adequado aos pacientes.

## Requisitos

Para executar o projeto, é necessário ter instalado:

* **Python 3**
* **PuLP 3.3.1**
* **CBC (COIN-OR Branch and Cut)** — solver utilizado pelo PuLP para resolver os modelos de otimização.

## Como executar

Entre na pasta do projeto:

```bash
cd projetoHemo
```

Para executar os modelos e realizar a resolução do problema:

```bash
python3 main.py
```

O arquivo `main.py` é responsável pela execução dos modelos de otimização implementados, bem como pela apresentação dos resultados obtidos. Esses resultados permitem analisar a distribuição dos pacientes entre as unidades de tratamento de hemodiálise do estado do Maranhão, contribuindo para a avaliação e o planejamento do acesso dos pacientes ao tratamento.

## Visualização dos resultados

Para visualizar graficamente os resultados obtidos pelos modelos:

```bash
python3 gráfico.py
```

O arquivo `gráfico.py` é responsável pela geração dos gráficos para análise dos resultados.


## Considerações

O projeto utiliza **modelos matemáticos e técnicas de otimização** como ferramenta de apoio ao planejamento do acesso de pacientes ao tratamento de hemodiálise.

Os resultados obtidos pelos modelos devem ser interpretados como **apoio à tomada de decisão**, considerando as características, restrições e recursos definidos no problema.

---

**Projeto Hemodiálise**
*Modelos computacionais para apoio ao planejamento e ao acesso de pacientes ao tratamento de hemodiálise.*
