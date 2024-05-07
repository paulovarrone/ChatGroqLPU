from groq import Groq
from fpdf import FPDF
import os
from extrair_texto import extract_text_from_pdf
from conteudo import conteudo, pergunta
from dotenv import dotenv_values

config = dotenv_values(".env")

GROQ_API_KEY = config["GROQ_API_KEY"]

client = Groq(api_key = GROQ_API_KEY)

def arquivo_texto(caminho_pdf, camininho_contestacao, conteudo_pasta,pasta_contestacao):
  try: 
    if not pasta_contestacao:
      os.makedirs(camininho_contestacao)
      print("Pasta criada com sucesso.")
    else:
      print("Pasta já existe.")

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
                model="llama3-8b-8192",
                temperature=0,
                max_tokens=1024,
                top_p=1,
                stop=None,
        )

        texto_da_contestacao = chat_completion.choices[0].message.content

        nome_arquivo_pdf = "Contestação_" + os.path.splitext(arquivo)[0] + ".pdf"
        
        caminho_texto = os.path.join(camininho_contestacao, nome_arquivo_pdf)


        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Dividir o texto em parágrafos e adicionar recuo
        centralizar = False
        paragrafos = texto_da_contestacao.split('\n')

        for paragrafo in paragrafos:
          paragrafo_original = paragrafo  # Guardar o parágrafo original para verificar a centralização
          paragrafo = paragrafo.replace("Advogado:", "").replace("Data:", "").strip()

          if "Informações do advogado:" in paragrafo_original:
              paragrafo = paragrafo.replace("Informações do advogado:", "").strip()
              centralizar = True

          if centralizar:
              pdf.set_font("Arial", 'B', size=12)
              pdf.cell(0, 10, '    ' + paragrafo, ln=True, align='C')
          else:
              # Parágrafos antes de "Advogado:" são adicionados normalmente
              pdf.multi_cell(0, 10, paragrafo)

        pdf.output(caminho_texto)

        print("Contestação criada com sucesso!")

  except Exception as e:
    print(f"ERRO {arquivo}: {str(e)}")