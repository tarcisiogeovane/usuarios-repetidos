# Influencers Duplicados - Identificador e Conversor

Este projeto contém dois scripts Python para identificar duplicatas de influenciadores em uma planilha Excel e convertê-las em formatos úteis:
1. **Identificação de duplicatas**: Lê uma planilha Excel, encontra arrobas do Instagram duplicados (mesmo arroba contatado por pessoas diferentes), e gera um arquivo de texto (`resultado.txt`).
2. **Conversão para Excel**: Transforma o `resultado.txt` em uma planilha Excel estruturada (`duplicatas.xlsx`) com as duplicatas organizadas.

O projeto é útil para equipes que gerenciam contatos de influenciadores, permitindo identificar e organizar casos em que o mesmo arroba foi contatado por múltiplas pessoas.

## Funcionalidades

### 1. Identificador de Duplicatas (`identificar_duplicatas.py`)
- **Entrada**: Planilha Excel (ex.: `Influencers_que_já_enviamos_email.xlsx`) com colunas "arroba" e "Quem enviou".
- **Processo**:
  - Identifica arrobas duplicados que foram contatados por pessoas diferentes (ignorando variações de maiúsculas/minúsculas, como "Felipe Costa" e "FELIPE COSTA").
  - Ajusta os números das linhas (adiciona +4 para alinhar com linhas do Excel).
- **Saída**: Arquivo `resultado.txt` contendo:
  - Cada arroba duplicado.
  - Números das linhas onde aparece (ajustados).
  - Nomes das pessoas que contataram o arroba.

### 2. Conversor TXT para Excel (`txt_to_excel.py`)
- **Entrada**: Arquivo `resultado.txt` gerado pelo script anterior.
- **Processo**:
  - Lê o texto e extrai arrobas, linhas, e nomes de "Quem enviou".
  - Organiza os dados em uma estrutura tabular.
- **Saída**: Planilha `duplicatas.xlsx` com colunas:
  - **Arroba**: O Instagram duplicado.
  - **Linhas**: Números das linhas, separados por vírgula.
  - **Quem Enviou**: Nomes das pessoas, separados por vírgula.

## Pré-requisitos

- **Python 3.x** instalado.
- Bibliotecas Python necessárias:
  - `pandas`
  - `openpyxl`
- Instale as dependências com:
  ```bash
  pip install pandas openpyxl
