import os
from chat_ia import arquivo_texto 

def main():
  try:
    caminho_pdf = "SEU CAMINHO DA PASTA PDF"

    camininho_contestacao = "CAMINHO PARA ONDE VOCE QUER CRIAR A PASTA COM A CONTESTACAO"

    conteudo_pasta = os.listdir(caminho_pdf)

    pasta_contestacao = os.path.exists(camininho_contestacao)

    arquivo_texto(caminho_pdf, camininho_contestacao, conteudo_pasta,pasta_contestacao)
  except Exception as e:
    print(f"Erro  {arquivo_texto}: {str(e)}")

if __name__ == "__main__":
  main() 