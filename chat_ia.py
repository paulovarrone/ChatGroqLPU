from groq import Groq
import os
from extrair_texto import extract_text_from_pdf
from conteudo import conteudo, pergunta
from text_to_pdf import texto_para_pdf
from dotenv import load_dotenv

load_dotenv()

client = Groq()

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

        texto_para_pdf(caminho_texto,texto_da_contestacao)
      
        print("Contestação criada com sucesso!")

  except Exception as e:
    print(f"ERRO {arquivo}: {str(e)}")