# Pipeline de Detecção de Fraude — PaySim

Pipeline de ETL em Python que processa dados simulados de transações bancárias e sinaliza transações potencialmente fraudulentas com base em uma regra de comportamento de conta.

## Objetivo do projeto

Instituições financeiras lidam diariamente com um altíssimo volume de transações, o que torna inviável identificar movimentações suspeitas de forma manual. O objetivo deste projeto foi construir um pipeline de ETL capaz de extrair, tratar e carregar dados de transações financeiras, aplicando uma regra de negócio própria para sinalizar automaticamente transações com padrão de comportamento suspeito, simulando um cenário real de prevenção à fraude no setor financeiro.

## Sobre o dataset

O [PaySim](https://www.kaggle.com/datasets/ealaxi/paysim1) é um dataset público que simula transações financeiras (pagamentos, transferências, saques) ao longo de 30 dias, com base em dados reais de um provedor de serviços financeiros móveis. Contém 6.362.620 transações, das quais 8.213 (0,13%) são fraudes confirmadas.

## O que o pipeline faz

**1. Extract** (`extract.py`)
Lê o CSV bruto e faz uma inspeção inicial: formato dos dados, colunas disponíveis, amostra das primeiras linhas.

**2. Transform** (`transform.py`)

- Remove colunas de identificação não usadas na análise (`nameOrig`, `nameDest`, `isFlaggedFraud`)
- Verifica valores nulos
- Cria uma coluna própria, `flag_suspeita`, sinalizando transações onde a conta de origem tinha saldo positivo, ficou com saldo zero após a transação, e o valor transacionado é igual ao saldo anterior — um padrão comum de conta "esvaziada"

**3. Load** (`load.py`)
Carrega os dados transformados em um banco SQLite (`pipeline.db`), na tabela `transacoes`, pronta para consulta via SQL ou conexão com ferramentas de BI.

**4. Consulta** (`consulta.py`)
Exemplos de consultas SQL sobre o banco gerado, incluindo comparação entre a regra própria (`flag_suspeita`) e a coluna oficial de fraude do dataset (`isFraud`).

## Resultado da regra criada

A regra `flag_suspeita` identificou 8.008 transações suspeitas, contra 8.213 fraudes reais no dataset (`isFraud = 1`) — uma sobreposição alta para uma regra baseada em uma única condição de comportamento, sem uso de machine learning.

## Tecnologias utilizadas

- Python (pandas, sqlite3)
- SQLite
- Git/GitHub

## Como rodar

O CSV do PaySim não está incluído no repositório por causa do tamanho (~470MB). Para reproduzir:

1. Baixe o dataset em [kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/ealaxi/paysim1)
2. Coloque o arquivo `.csv` em uma pasta `dados/`
3. Instale as dependências: `pip install pandas`
4. Rode na ordem: `extract.py` → `transform.py` → `load.py` → `consulta.py`

## Aprendizados

Este projeto foi minha primeira experiência construindo um pipeline de ETL completo, do zero. Os principais aprendizados foram:

- Consolidar na prática o fluxo extract → transform → load, incluindo decisões de quais colunas manter e como validar dados nulos
- Criar uma regra de negócio própria e compará-la contra o resultado real do dataset, entendendo os limites de uma regra simples frente a fraudes mais sofisticadas
- Ganhar familiaridade com SQLite como camada de persistência para consultas analíticas
- Perceber, na prática, a importância da documentação técnica para tornar um projeto compreensível para terceiros

## Próximos passos

Conectar `pipeline.db` a um dashboard no Power BI para visualização das transações sinalizadas.

---

Projeto desenvolvido como parte da minha transição para a área de dados, com foco em Risco e Prevenção à Fraude no setor financeiro.
