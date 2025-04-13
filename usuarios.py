import pandas as pd

# Carrega o arquivo Excel
file_path = 'c:\\Users\\tarci\\OneDrive\\Desktop\\usuarios repetidos\\repetidos.xlsx'
df = pd.read_excel(file_path, sheet_name=0)

# Normaliza a coluna 'Quem enviou' para ignorar maiúsculas/minúsculas
df['Quem enviou_normalized'] = df['Quem enviou'].str.lower()

try:
    # Verifica duplicatas na coluna 'arroba' com diferentes 'Quem enviou' (normalizado)
    duplicatas = df.groupby('arroba')['Quem enviou_normalized'].nunique().reset_index()
    duplicatas = duplicatas[duplicatas['Quem enviou_normalized'] > 1]

    # Abre o arquivo resultado.txt para escrita
    with open('resultado.txt', 'w', encoding='utf-8') as f:
        if not duplicatas.empty:
            f.write("Duplicatas encontradas (mesmo 'arroba' com diferentes 'Quem enviou'):\n")
            for arroba in duplicatas['arroba']:
                # Filtra as linhas com o 'arroba' duplicado
                linhas_duplicadas = df[df['arroba'] == arroba][['arroba', 'Quem enviou']]
                # Obtém os índices (números das linhas) das duplicatas e adiciona 4
                indices = [i + 4 for i in df[df['arroba'] == arroba].index.tolist()]
                f.write(f"\nArroba: {arroba}\n")
                f.write(f"Linhas: {', '.join(map(str, indices))}\n")
                # Escreve as linhas duplicadas
                f.write(linhas_duplicadas.to_string(index=False))
                f.write("\n")
            print("Resultados salvos em 'resultado.txt'.")
        else:
            f.write("Nenhuma duplicata encontrada (mesmo 'arroba' com diferentes 'Quem enviou').\n")
            print("Nenhuma duplicata encontrada. Resultado salvo em 'resultado.txt'.")

except KeyError as e:
    with open('resultado.txt', 'w', encoding='utf-8') as f:
        f.write(f"Erro: A coluna {e} não foi encontrada. Verifique os nomes das colunas na planilha.\n")
    print(f"Erro: Coluna {e} não encontrada. Mensagem salva em 'resultado.txt'.")

# Remove a coluna temporária usada para normalização
df = df.drop(columns=['Quem enviou_normalized'], errors='ignore')