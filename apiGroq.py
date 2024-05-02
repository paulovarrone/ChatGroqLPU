from groq import Groq
import PyPDF2



api_key = "chave api"

client = Groq(api_key="chave api")

# def extract_text_from_pdf(pdf_file):
#   pdf_text = ""
#   pdf_reader = PyPDF2.PdfReader(pdf_file)
#   for page in pdf_reader.pages:
#     pdf_text += page.extract_text()
#   return pdf_text


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Me de uma receita de pão",
        }
    ],
    model="llama3-70b-8192",
    temperature=0,
)

print(chat_completion.choices[0].message.content)