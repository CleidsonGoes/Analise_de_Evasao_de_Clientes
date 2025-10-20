<h1 align="center">📊 Análise de Evasão de Clientes Bancários</h1> <p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas&logoColor=white" /> <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-9cf?logo=plotly&logoColor=white" /> <img src="https://img.shields.io/badge/Status-Em%20Desenvolvimento-success" /> </p>
🧠 Sobre o Projeto

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) com foco em identificar os fatores que influenciam o cancelamento de contas de clientes bancários.

Através do Python, o script lê e processa uma base de dados em CSV, realiza limpeza e tratamento, gera estatísticas descritivas e visualizações interativas com Plotly Express, permitindo descobrir padrões e comportamentos relevantes entre clientes ativos e cancelados.

🧩 Tecnologias Utilizadas

🐍 Python 3.10+

🧮 Pandas — Manipulação e análise de dados

📊 Plotly Express — Criação de gráficos interativos

💻 VS Code / Jupyter Notebook (recomendado para execução)

⚙️ Etapas da Análise

Leitura dos Dados

Importação do arquivo ClientesBanco.csv com pandas.read_csv().

Configuração de exibição completa de colunas e linhas.

Limpeza e Preparação

Remoção da coluna desnecessária CLIENTNUM.

Exclusão de registros com valores ausentes (NaN).

Análise Estatística

Geração de estatísticas descritivas com describe().

Contagem e percentual de clientes por categoria (ativos x cancelados).

Visualização Gráfica

Criação automática de histogramas interativos para todas as colunas do dataset, permitindo comparar clientes ativos e cancelados em cada variável.

💡 Principais Insights

🔹 Clientes com mais produtos contratados tendem a não cancelar suas contas.

🔹 Maior volume e frequência de transações estão associados à menor taxa de cancelamento.

🔹 Mais contatos com o suporte estão relacionados a maior probabilidade de cancelamento, possivelmente indicando insatisfação.

Essas descobertas podem auxiliar a instituição a desenvolver estratégias de retenção e melhorar o relacionamento com os clientes.

▶️ Como Executar o Projeto
1️⃣ Instale as dependências:
pip install pandas plotly

2️⃣ Execute o script:
python index.py

3️⃣ Visualize os resultados:

Estatísticas e informações gerais serão exibidas no terminal.

Gráficos interativos serão abertos automaticamente no navegador.

📁 Estrutura do Projeto

> ```
> 📦 Analise_de_Evasao_de_Clientes  
> ├── 📄 index.py  
> ├── 📊 ClientesBanco.csv  
> └── 📘 README.md  
> ```

✨ Autor

Cleidson Goes
📍 Salvador, BA
💻 Analista de BI e Analista de Dados em formação
<p align="center">
  <a href="https://github.com/cleidsongoes">
    <img src="https://img.shields.io/badge/GitHub-cleidsongoes-black?logo=github" alt="GitHub Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/cleidson-goes/">
    <img src="https://img.shields.io/badge/LinkedIn-Cleidson%20Goes-blue?logo=linkedin" alt="LinkedIn Badge"/>
  </a>
</p>
