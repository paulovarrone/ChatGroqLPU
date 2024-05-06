from groq import Groq
import fitz
import os
import datetime

api_key = "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"

client = Groq(api_key = api_key)


data_atual = datetime.datetime.now()
numero_mes = data_atual.month

mes_str = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Abril",
            5: "Maio",
            6: "Junho",
            7: "Julho",
            8: "Agosto",
            9: "Setembro",
            10: "Outubro",
            11: "Novembro",
            12: "Dezembro"
        }[numero_mes]

data_formatada = data_atual.strftime(f"%d de {mes_str} de %Y.") 

pergunta = f"""Faça uma contestação.
        Certifique-se de incluir:
        AGRAVO DE INSTRUMENTO
        Número do Processo: 
        Agravante: 
        Agravados: 
        Breve resumo do agravo de instrumento.
        Análise da Tempestividade: Confirme se a contestação está sendo feita dentro do prazo legal.
        Impugnação Específica dos Fatos: Indique como negar, admitir ou declarar desconhecimento dos fatos alegados pela parte autora.
        Fundamentação Legal: Apresente as leis, jurisprudências e doutrinas que suportam a defesa.
        Apresentação de Provas: Especifique as provas que serão usadas para contestar as alegações da parte autora, como documentos, testemunhos, entre outros.
        Questões Preliminares e Processuais: Argumente sobre eventuais questões processuais que possam desqualificar a petição inicial ou exigir sua completa reformulação.
        Formulação do Mérito e do Pedido: Desenvolva os argumentos de mérito contra os pedidos da parte autora e formule os pedidos específicos na contestação.
        Endereçamento Correto e Evitar a Preclusão: Garanta que a contestação esteja corretamente endereçada e discuta estratégias para evitar a preclusão de defesas e argumentos. 
        No final do documento, deve ser incluido no final da resposta com apenas uma quebra de linha:
            as informações do advogado ou procurador, nome do advogado ou procurador e seu registro de OAB. 
            {data_formatada} no documento.
        """

conteudo = "Você é um procurador com mais de 20 anos de experiência no município do estado do rio de janeiro. Você irá analisar minuciosamente o documento enviado e responder com base neste documento citado. Evite erros de ortografia na linguagem Português Brasil"


def extract_text_from_pdf(pdf_path):
  try:

    text = ""

    with fitz.open(pdf_path) as pdf_file:
      for page in pdf_file: 
        text += page.get_text()

    return text
  
  except Exception:
    print("ERRO AO TENTAR EXTRAIR TEXTO")


def main():

  caminho_pdf = r'C:\Users\3470622\Desktop\Workspace\pgm testes\APIGroq\pdf'

  camininho_contestacao = r'C:\Users\3470622\Desktop\Workspace\pgm testes\APIGroq\contestacao'

  conteudo_pasta = os.listdir(caminho_pdf)

  pasta_contestacao = os.path.exists(camininho_contestacao)

  try: 

    if not pasta_contestacao:
      os.makedirs(camininho_contestacao)

    for arquivo in conteudo_pasta:

      if arquivo.endswith('.pdf'):
        pdf_file = os.path.join(caminho_pdf, arquivo)
        text = extract_text_from_pdf(pdf_file)

        
        chat_completion = client.chat.completions.create(
            messages=[
                    {"role": "system", "content": conteudo},
                    {"role": "user", "content": pergunta},
                    {"role": "assistant", "content": text}
                  ],
                model="llama3-70b-8192",
                temperature=0,
                max_tokens=1024,
                top_p=1,
                stop=None,
        )

        texto_da_contestacao = chat_completion.choices[0].message.content

        nome_arquivo_texto = "Contestação_" + os.path.splitext(arquivo)[0] + ".txt"

        caminho_texto = os.path.join(camininho_contestacao, nome_arquivo_texto)

        with open(caminho_texto, 'w', encoding='utf-8') as texto:
          texto.write(texto_da_contestacao)

        print("Sucesso")

  except Exception as e:
    print(f"ERRO {arquivo}: {str(e)}")

if __name__ == "__main__":
  main()  