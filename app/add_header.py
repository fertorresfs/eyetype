import os
from datetime import date

# === Configurações personalizáveis ===
autor = "Fernando Torres Ferreira da Silva"
projeto = "VoxRecomNLP - Comunicação Aumentativa com IA"
versao = "v2.0"
data_hoje = date.today().strftime("%d/%m/%Y")
link1 = "https://wandb.ai/fernandotfs-usp-universidade-de-s-o-paulo"
link2 = "https://github.com/fertorresfs/vox_recom_nlp"
extensao = ".py"

# === Cabeçalho que será inserido ===
def gerar_cabecalho(nome_arquivo):
    return f"""# ============================================
# Autor: {autor}
# Projeto: {projeto}
# Versão: {versao}
# Arquivo: {nome_arquivo}
# Wandb: {link1}
# Github: {link2}
# Data: {data_hoje}
# ============================================\n"""

# === Inserção do cabeçalho ===
def inserir_cabecalho_em_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Evita inserir múltiplas vezes
    if "Autor: Fernando Torres" in conteudo:
        return

    nome_arquivo = os.path.basename(caminho_arquivo)
    cabecalho = gerar_cabecalho(nome_arquivo)
    novo_conteudo = cabecalho + conteudo

    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(novo_conteudo)
    print(f"[✔] Cabeçalho adicionado: {caminho_arquivo}")

# === Percorrer diretórios recursivamente ===
def processar_pasta(pasta_raiz):
    for raiz, _, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if arquivo.endswith(extensao):
                caminho_completo = os.path.join(raiz, arquivo)
                inserir_cabecalho_em_arquivo(caminho_completo)

# === Executar ===
if __name__ == "__main__":
    pasta_projeto = "."  # Caminho da raiz do projeto (atual)
    processar_pasta(pasta_projeto)
