# Projeto de pipeline de dados financeiros

Um pipeline de dados para coletar, armazenar e analisar preços e vendas de ativos financeiros, incluindo Bitcoin e commodities.

## Estrutura do Projeto

```
.env_sample # Variáveis ​​de ambiente de exemplo para conexão com o banco de dados
ExtractLoad/ # Scripts Python para extração e carregamento de dados
getBitcoin.py # Coleta dados de preços de Bitcoin
getComm.py # Coleta dados de preços de commodities (ouro, petróleo, prata)
getPrices_loop_db.py # Loop ETL principal: busca preços e carrega no banco de dados
Tables/ # Scripts SQL para esquema e transformações do banco de dados
Bronze/ # Tabelas de dados brutos
create_table.sql
Silver/ # Tabelas de vendas normalizadas e enriquecidas
silver_sales_normalized.sql
silver_sales_enriched.sql
Gold/ # Visualizações analíticas
gold_kpi_by_customer.sql
gold_last_7_assets_sales.sql
```

## Como Funciona

1. **Extrair e Carregar**
- Scripts Python em `ExtractLoad/` buscam dados de preços de APIs (Coinbase para BTC, Yahoo Finance para commodities).
- Os dados são carregados no banco de dados PostgreSQL.

2. **Camada Bronze**
- Tabelas brutas para preços, clientes e vendas (`create_table.sql`).

3. **Camada Prata**
- Normaliza e enriquece os dados de vendas com informações de preço (`silver_sales_normalized.sql`, `silver_sales_enriched.sql`).

4. **Camada Ouro**
- Visualizações analíticas para KPIs e vendas recentes (`gold_kpi_by_customer.sql`, `gold_last_7_assets_sales.sql`).

## Configuração

1. **Instalar dependências**
- Python: `pandas`, `sqlalchemy`, `yfinance`, `python-dotenv`, `requests`
- Banco de dados: PostgreSQL

2. **Configurar ambiente**
- Copiar `.env_sample` para `.env` e preencher as credenciais do seu banco de dados.

3. **Criar tabelas**
- Executar scripts SQL em `Tables/Bronze/` para configurar o banco de dados.

4. **Executar ETL**
- Executar `ExtractLoad/getPrices_loop_db.py` para iniciar a coleta e o carregamento de dados.

## Uso

- **Coleta de Dados:**
Executar o script ETL para buscar e armazenar continuamente os preços dos ativos.

- **Análise:**
Usar os scripts SQL em `Tables/Silver/` e `Tables/Gold/` para transformar e analisar dados de vendas e preços.

## Objetivo

Este projeto será utilizado para automatizar o monitoramento de preços e vendas de ativos financeiros, facilitando análises históricas, geração de relatórios e dashboards e suporte à tomada de decisão em investimentos.

