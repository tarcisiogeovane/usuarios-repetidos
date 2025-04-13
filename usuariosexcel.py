import pandas as pd
import re

# Função para ler e processar o arquivo txt
def parse_influencers_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Lista para armazenar os dados
    data = []
    current_arroba = None
    current_linhas = None
    quem_enviou_list = []

    # Divide o conteúdo em linhas
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Identifica o arroba
        if line.startswith("Arroba:"):
            if current_arroba and current_linhas and quem_enviou_list:
                # Salva o registro anterior
                data.append({
                    "Arroba": current_arroba,
                    "Linhas": current_linhas,
                    "Quem Enviou": ", ".join(quem_enviou_list)
                })
            current_arroba = line.replace("Arroba:", "").strip()
            quem_enviou_list = []
            i += 1
            continue

        # Identifica as linhas
        if line.startswith("Linhas:"):
            current_linhas = line.replace("Linhas:", "").strip()
            i += 1
            continue

        # Ignora a linha de cabeçalho da tabela
        if line.startswith("arroba") and "Quem enviou" in line:
            i += 1
            continue

        # Coleta "Quem enviou" (linhas com arroba e nome)
        if current_arroba and line and not line.startswith("Duplicatas encontradas"):
            # Usa regex para capturar o nome após o arroba
            match = re.match(rf"{re.escape(current_arroba)}\s+(.+)", line.strip())
            if match:
                quem_enviou = match.group(1).strip()
                if quem_enviou not in quem_enviou_list:  # Evita duplicatas
                    quem_enviou_list.append(quem_enviou)
            i += 1
            continue

        i += 1

    # Adiciona o último registro
    if current_arroba and current_linhas and quem_enviou_list:
        data.append({
            "Arroba": current_arroba,
            "Linhas": current_linhas,
            "Quem Enviou": ", ".join(quem_enviou_list)
        })

    return data

# Caminho do arquivo txt
file_path = 'c:\\Users\\tarci\\OneDrive\\Desktop\\usuarios repetidos\\influencers repetidos.txt'

# Processa o arquivo
data = parse_influencers_txt(file_path)

# Cria um DataFrame com os dados
df = pd.DataFrame(data, columns=["Arroba", "Linhas", "Quem Enviou"])

# Salva o DataFrame como Excel
output_path = 'c:\\Users\\tarci\\OneDrive\\Desktop\\usuarios repetidos\\duplicatas.xlsx'
df.to_excel(output_path, index=False)

print(f"Planilha salva em '{output_path}'.")