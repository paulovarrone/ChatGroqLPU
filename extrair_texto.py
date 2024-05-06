import fitz

def extract_text_from_pdf(pdf_path):
  try:

    text = ""

    with fitz.open(pdf_path) as pdf_file:
      for page in pdf_file: 
        text += page.get_text()

    return text
  
  except Exception:
    print("ERRO AO TENTAR EXTRAIR TEXTO")