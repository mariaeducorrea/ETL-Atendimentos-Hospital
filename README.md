# Análise de Dados de Atendimentos do Hospital

Este projeto tem como objetivo realizar a análise de dados dos atendimentos hospitalares, utilizando informações extraídas de um banco de dados PostgreSQL. A partir dessa extração, os dados foram manipulados com o Pandas, exportados para um arquivo CSV e posteriormente transformados para um formato Excel (.xlsx). Esses dados processados foram, então, importados para o Power BI, permitindo a criação de um dashboard interativo para visualização e análise.

## Fluxo de Trabalho

O fluxo de trabalho realizado para a análise dos dados é o seguinte:

### 1. Conexão com o Banco de Dados PostgreSQL

Primeiro, fiz a conexão com o banco de dados PostgreSQL, onde as informações dos atendimentos hospitalares estavam armazenadas. Para isso, utilizei a biblioteca **`psycopg2`** em Python, que facilita a comunicação entre o Python e o PostgreSQL.

### 2. Exportação dos Dados para CSV

Após obter os dados do banco de dados PostgreSQL, os exportei para um arquivo CSV, que serve como formato de transferência para facilitar a manipulação posterior.

### 3. Manipulação de Dados com Pandas

Depois de exportar os dados para o arquivo CSV, usei a biblioteca Pandas para carregar e manipular os dados. Com o Pandas, realizei várias operações de transformação, como conversão de tipos de dados, categorização de idades e arredondamento de horários, entre outras manipulações necessárias.

### 4. Exportação para Excel (.xlsx)

Após manipular os dados com Pandas, exportei os resultados para um arquivo Excel (.xlsx), que serve como formato final para visualização e análise no Power BI.

---

#### Tecnologias Utilizadas

- PostgreSQL: Banco de dados relacional para armazenar as informações de - atendimentos.
- psycopg2: Biblioteca Python para realizar a conexão e consulta no PostgreSQL.
- Pandas: Biblioteca Python para manipulação e transformação de dados.
- Excel (XLSX): Formato de arquivo para armazenar os dados manipulados.
- Power BI: Ferramenta de BI para visualização e análise interativa dos dados.
