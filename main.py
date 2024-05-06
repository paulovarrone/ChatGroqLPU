import os
from chat_ia import arquivo_texto 


def main():
  caminho_pdf = r'C:\Users\3470622\Desktop\Workspace\pgm testes\APIGroq\pdf'

  camininho_contestacao = r'C:\Users\3470622\Desktop\Workspace\pgm testes\APIGroq\contestacao'

  conteudo_pasta = os.listdir(caminho_pdf)

  pasta_contestacao = os.path.exists(camininho_contestacao)

  arquivo_texto(caminho_pdf, camininho_contestacao, conteudo_pasta,pasta_contestacao)


if __name__ == "__main__":
  main() 