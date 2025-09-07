# Visão de Negócio – Camada GOLD

## 1) `gold_last7_assets`

**O que é:** visão diária, por ativo, dos **últimos 7 dias** de operação. Mostra volume financeiro, fluxo líquido e número de transações por ativo, mesmo quando um dia não teve movimento (fica 0).

**Para que serve:**

* Acompanhar desempenho **recente** por ativo (BTC-USD, GC=F, CL=F, SI=F).
* Medir **tendência semanal** e apoiar decisões táticas (rebalanceamentos, campanhas, limites).
* Base simples para card de “**como fechou o dia**” no dashboard.

**Grão (grain):** 1 linha por **(data, ativo)**.
**Período coberto:** últimos 7 dias (rolling).
**Fonte:** `silver_sales_enriched` (transações já normalizadas e precificadas).
**Atualização:** recomendada diária (D+0) ou intradiária conforme a coleta de cotações.

**Colunas (definições de negócio):**

* `data` (DATE): dia calendário.
* `ativo` (TEXT): símbolo normalizado (ex.: `BTC-USD`, `GC=F`, `CL=F`, `SI=F`).
* `volume_gross_usd` (NUMERIC): **somatório do notional absoluto** do dia (VENDA e COMPRA entram como positivos).
* `fluxo_liquido_usd` (NUMERIC): **VENDA – COMPRA** em US\$ (Compras entram negativas, Vendas positivas).
* `transacoes` (INTEGER): quantidade de ordens no dia para o ativo.

**Exemplos de uso:**

* “Qual ativo mais movimentou nos últimos 7 dias?”
* “O fluxo líquido do BTC na semana está positivo ou negativo?”
* “Houve queda de atividade (nº de transações) em algum dia?”

**Exemplos de perguntas respondidas:**

* Top 1 ativo por **volume** ontem.
* Evolução do **fluxo líquido** do CL=F ao longo da semana.
* **Heatmap** de transações por ativo × dia.

**Regras/limitações importantes:**

* Considera só dias do calendário; se quiser **dias úteis**, ajustar a geração de datas.
* Preços vêm da camada silver com join “as-of/backward” (último preço ≤ hora), evitando uso de preço futuro.
* Se não houver transação no dia/ativo, os valores ficam **0** (linha existe por consistência de grade).

---

## 2) `gold_kpi_by_customer`

**O que é:** KPIs **consolidados por cliente** no período completo disponível (baseada na enriched).

**Para que serve:**

* Identificar **clientes chave** por **volume** e por **resultado líquido**.
* Suporte a **CRM/CS/Vendas** (priorização de atendimento, ofertas por comportamento).
* Base para ranking de clientes e análise de concentração.

**Grão (grain):** 1 linha por **cliente**.
**Período coberto:** todo o histórico carregado na `silver_sales_enriched` (pode ser filtrado por data no consumo).
**Fonte:** `silver_sales_enriched` (join com `bronze_customers` pelo `customer_id`).
**Atualização:** diária (D+0) após enrichment.

**Colunas (definições de negócio):**

* `customer_id` (TEXT): identificador do cliente.
* `customer_name` (TEXT): nome de exibição do cliente.
* `volume_gross_usd` (NUMERIC): **somatório do notional absoluto** no período (intensidade de relacionamento).
* `fluxo_liquido_usd` (NUMERIC): **VENDA – COMPRA** ao longo do período (proxy de “resultado” operacional da carteira do cliente).
* `transacoes` (INTEGER): quantidade total de ordens do cliente.

**Exemplos de uso:**

* “Top 10 clientes por **volume** no mês.”
* “Quem mais **ganhou/perdeu** (fluxo líquido) no trimestre?”
* “Distribuição de **nº de transações** por cliente (cauda longa).”

**Exemplos de perguntas respondidas:**

* **Quem mais ganhou** e **quem mais perdeu**: ordenar por `fluxo_liquido_usd` desc/asc.
* Qual cliente tem **maior engajamento** (transações) vs **maior volume**.
* **Concentração** de receita/volume (ex.: % Top 5).

**Regras/limitações importantes:**

* `fluxo_liquido_usd` depende do sentido da operação: VENDA (+), COMPRA (−).
* Para análises sazonais, **filtrar por `data_dia`** na `silver_sales_enriched` antes de agregar (ex.: mês corrente).
* Clientes sem transação não aparecem (podem ser incluídos via outer join com `bronze_customers` se necessário).