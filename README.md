# Influencers Duplicados - Conversor TXT para Excel

Este projeto contém um script Python que converte um arquivo de texto (`influencers repetidos.txt`) com informações de duplicatas de influenciadores (arrobas do Instagram e quem os contatou) em uma planilha Excel estruturada (`duplicatas.xlsx`).

## Funcionalidade

O script:
- Lê o arquivo `influencers repetidos.txt`, que lista arrobas do Instagram duplicados, os números das linhas correspondentes na planilha original, e as pessoas que os contataram ("Quem enviou").
- Extrai e organiza os dados em três colunas:
  - **Arroba**: O Instagram duplicado.
  - **Linhas**: Números das linhas onde o arroba aparece, separados por vírgula.
  - **Quem Enviou**: Nomes das pessoas que contataram o arroba, separados por vírgula.
- Gera uma planilha Excel (`duplicatas.xlsx`) com os dados organizados.

## Pré-requisitos

- **Python 3.x** instalado.
- Bibliotecas Python necessárias:
  - `pandas`
  - `openpyxl`

Instale as dependências com:
```bash
pip install pandas openpyxl
