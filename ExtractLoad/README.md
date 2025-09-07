# Coleta de Cotações

Tem como objetivo coletar, consolidar e salvar cotações em tempo real de **Bitcoin** e de **commodities** selecionadas, utilizando APIs públicas e a biblioteca `yfinance`.

---

## Estrutura do Projeto

### **GetBitcoin.py**

* Script responsável por coletar a **cotação atual do Bitcoin** em USD.
* Fonte: API pública da **Coinbase**.
* Retorna um **DataFrame padronizado** com as colunas:

  * `ativo` — símbolo do ativo (`BTC-USD`)
  * `preco` — preço atual
  * `moeda` — moeda de cotação (USD)
  * `horario_coleta` — horário local da coleta
* Pode ser executado de forma independente (`python GetBitcoin.py`) para teste.

---

### **GetComm.py**

* Script responsável por coletar a **última cotação** de commodities em USD, no intervalo de 1 minuto.
* Fonte: **Yahoo Finance** via biblioteca `yfinance`.
* Lista de ativos incluídos por padrão:

  * `GC=F` — Ouro
  * `CL=F` — Petróleo WTI
  * `SI=F` — Prata
* Retorna um **DataFrame padronizado** com as colunas:

  * `ativo` — símbolo do ativo
  * `preco` — preço atual
  * `moeda` — moeda de cotação (USD)
  * `horario_coleta` — horário local da coleta
* Pode ser executado de forma independente (`python GetComm.py`) para teste.

---

### **GetPrices.py**

* Script orquestrador que combina os resultados de **GetBitcoin** e **GetCommodities**.
* **Loop infinito com salvamento** — coleta a cada 60 segundos e **salva** no banco de dados.

---

## Como Executar

1. **Instalar dependências:**

   ```bash
   pip install pandas yfinance requests
   ```

2. **Rodar a coleta de Bitcoin:**

   ```bash
   python GetBitcoin.py
   ```

3. **Rodar a coleta de Commodities:**

   ```bash
   python GetCommodities.py
   ```

4. **Rodar a coleta consolidada (exemplo com salvamento a cada 60s):**

   ```bash
   python GetPrices_loop_save.py
   ```

---

## Objetivo Futuro

Os dados coletados serão utilizados para:

* Calcular **KPIs diários** como lucro/prejuízo.
* Avaliar variação de preços.