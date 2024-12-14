import os
import shutil

# Caminho da pasta Downloads (alterar conforme necessário)
pasta_downloads = os.path.expanduser("~/Downloads")

# Dicionário para organizar os arquivos por tipo
tipos_arquivos = {
    "Documentos": [".pdf", ".doc", ".docx", ".txt"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Músicas": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "Outros": []
}

# Função para mover arquivos
def organizar_downloads():
    for arquivo in os.listdir(pasta_downloads):
        caminho_arquivo = os.path.join(pasta_downloads, arquivo)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(arquivo)
            encontrado = False
            
            # Verifica em qual categoria o arquivo se encaixa
            for pasta, extensoes in tipos_arquivos.items():
                if extensao.lower() in extensoes:
                    mover_para_pasta(arquivo, pasta)
                    encontrado = True
                    break
            
            # Caso o tipo não esteja mapeado, move para a pasta "Outros"
            if not encontrado:
                mover_para_pasta(arquivo, "Outros")

# Função para mover o arquivo para a pasta correta
def mover_para_pasta(arquivo, pasta_destino):
    pasta_destino_completa = os.path.join(pasta_downloads, pasta_destino)
    
    # Cria a pasta caso não exista
    if not os.path.exists(pasta_destino_completa):
        os.makedirs(pasta_destino_completa)
    
    # Move o arquivo
    shutil.move(os.path.join(pasta_downloads, arquivo), os.path.join(pasta_destino_completa, arquivo))
    print(f"{arquivo} movido para {pasta_destino}/")

# main
if __name__ == "__main__":
    organizar_downloads()
    print("Organização concluída!")
