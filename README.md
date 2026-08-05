# Pipeline de Detecção de Fraude — PaySim

Pipeline de ETL em Python que processa dados simulados de transações bancárias e sinaliza transações potencialmente fraudulentas com base em uma regra de comportamento de conta.

## Objetivo do projeto

Instituições financeiras lidam com um altíssimo volume de transações diariamente, o que torna inviável identificar movimentações suspeitas manualmente. O objetivo foi construir um pipeline de ETL capaz de extrair, tratar e carregar dados de transações financeiras, aplicando uma regra de negócio própria para sinalizar automaticamente transações com padrão suspeito, simulando um cenário real de prevenção à fraude no setor financeiro.

## Sobre o dataset

O [PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1) simula transações financeiras (pagamentos, transferências, saques) ao longo de 30 dias, com base em dados reais de um provedor de serviços financeiros móveis. Contém 6.362.620 transações, das quais 8.213 (0,13%) são fraudes confirmadas.

## O que o pipeline faz

**1. Extract** (`extract.py`) — leitura do CSV bruto e inspeção inicial dos dados.

**2. Transform** (`transform.py`) — remove colunas não usadas, verifica nulos e cria a coluna `flag_suspeita`, sinalizando contas que ficaram com saldo zero após transação igual ao saldo anterior (padrão de conta "esvaziada").

**3. Load** (`load.py`) — carrega os dados na tabela `transacoes` de um banco SQLite (`pipeline.db`).

**4. Consulta** (`consulta.py`) — consultas SQL comparando a regra própria (`flag_suspeita`) com a coluna oficial de fraude (`isFraud`).

## Resultado

A regra `flag_suspeita` identificou 8.008 transações suspeitas, contra 8.213 fraudes reais no dataset — alta sobreposição para uma regra baseada em uma única condição, sem machine learning.

## Tecnologias utilizadas

- Python (pandas, sqlite3)
- SQLite
- Git/GitHub

## Como rodar

O CSV do PaySim não está no repositório (~470MB). Baixe em [kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1), coloque em uma pasta `dados/`, instale `pandas` e rode na ordem: `extract.py` → `transform.py` → `load.py` → `consulta.py`.

## Aprendizados

Minha primeira experiência construindo um pipeline de ETL completo, do zero:

- Consolidei o fluxo extract → transform → load, incluindo decisões sobre quais colunas manter e como validar dados nulos
- Criei uma regra de negócio própria e a comparei ao resultado real do dataset, entendendo os limites de uma regra simples frente a fraudes mais sofisticadas
- Ganhei familiaridade com SQLite como camada de persistência para consultas analíticas

## Próximos passos

Conectar `pipeline.db` a um dashboard no Power BI para visualização das transações sinalizadas.

---

Projeto desenvolvido na minha transição para a área de dados, com foco em Risco e Prevenção à Fraude no setor financeiro.
