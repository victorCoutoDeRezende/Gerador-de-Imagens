import openai
from requests import get
import urllib.request
import sys

openai.api_key = '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'

def msg_abertura():
    print("-=" * 50)
    print('Você deseja gerar ou criar variações de uma imagem?'.upper().center(100))
    print("[1]GERAR - [2]MODIFICAR".center(100))
    print("-=" * 50)
msg_abertura()

def cria_imagem(descricao_imagem):
    response = openai.Image.create(
        prompt= descricao_imagem,
        n=1,
        size=resolucao
    )
    image_url = response['data'][0]['url']
    print(f'URL da imagem gerada: {image_url}')

    try:
        urllib.request.urlretrieve(image_url, f"generated-images/{imagem}.jpg")
        print("Imagem salva! =)")
    except:
        erro = sys.exc_info()
        print("Ocorreu um erro:", erro)

def modifica_imagem(modificacao_imagem):
    response = openai.Image.create_variation(
        image=open(modificacao_imagem, "rb"),
        n=1,
        size=resolucao
    )
    image_url = response['data'][0]['url']
    print(f'URL da imagem gerada: {image_url}')

    try:
        indice_barra = imagem.find("/")
        nome_imagem_gerada = imagem[indice_barra+1:]
        urllib.request.urlretrieve(image_url, f"modified-images/{nome_imagem_gerada}")
        print("Imagem salva! =)")
    except:
        erro = sys.exc_info()
        print("Ocorreu um erro:", erro)

def verifica(mensagem):
    global imagem, resolucao
    imagem = input(mensagem)
    tamanho = int(input("Escolha um tamanho de resolução\n [1]256x256 - [2]512x512 - [3]1024x1024\n-> "))
    if tamanho == 1:
        resolucao = "256x256"
    elif tamanho == 2:
        resolucao = "512x512"
    else:
        resolucao = "1024x1024"
    return imagem, tamanho

escolha = int(input("-> "))

if escolha == 1:
    verifica('Digite o que deseja que seja gerado-> ')
    cria_imagem(imagem)
elif escolha == 2:
    verifica("Cole aqui o nome da imagem, cole também o caminho caso não esteja na pasta atual->")
    modifica_imagem(imagem)
else:
    print("Digite uma opção válida")
