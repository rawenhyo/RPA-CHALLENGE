import os
import requests


def baixarDesafioRPA(caminho: str, nome: str):
    url_api = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
    # Caminho onde o arquivo será salvo
    download_path = caminho+nome
    if (os.path.exists(caminho+nome)):
        print((f"Arquivo já existe em: {
              download_path} e não foi baixado novamente"))
        return download_path
    # Fazer a solicitação GET para a URL da API
    response = requests.get(url_api)

    # Verificar se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Salvar o conteúdo da resposta em um arquivo
        with open(download_path, 'wb') as file:
            file.write(response.content)
        print(f"Arquivo baixado e salvo em: {download_path}")
        return download_path
    else:
        print(f"Erro ao baixar o arquivo: {response.status_code}")
