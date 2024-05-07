from fpdf import FPDF


def texto_para_pdf(caminho_texto,texto_da_contestacao):   
    try:     
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

            
        centralizar = False
        paragrafos = texto_da_contestacao.split('\n')

        for paragrafo in paragrafos:
            paragrafo_original = paragrafo  
            paragrafo = paragrafo.replace("Advogado:", "").replace("Data:", "").strip()

            if "Informações do advogado:" in paragrafo_original:
                paragrafo = paragrafo.replace("Informações do advogado:", "").strip()
                centralizar = True

            if centralizar:
                pdf.set_font("Arial", 'B', size=12)
                pdf.cell(0, 10, '    ' + paragrafo, ln=True, align='C')
            else:
                pdf.multi_cell(0, 10, paragrafo)

        pdf.output(caminho_texto)
    
    except Exception as e:
        print(f"ERRO {pdf}: {str(e)}")
