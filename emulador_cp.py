def copiar_arquivo(origem, destino):
    try:
        # Abre o arquivo de origem para leitura
        with open(origem, 'r', encoding='utf-8') as arquivo_origem:
            conteudo = arquivo_origem.read()

        # Abre ou cria o arquivo de destino para escrita
        with open(destino, 'w', encoding='utf-8') as arquivo_destino:
            arquivo_destino.write(conteudo)

        print(f"Arquivo '{origem}' copiado com sucesso para '{destino}'.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{origem}' não foi encontrado.")
    except IOError as e:
        print(f"Erro de E/S: {e}")

if __name__ == "__main__":
    origem = "arquivo.txt"          
    destino = "arquivo_copia.txt"  

    copiar_arquivo(origem, destino)
