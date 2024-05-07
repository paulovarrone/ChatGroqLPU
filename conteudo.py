import datetime

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
            {data_formatada} no documento você deve ser rígido a colocar a data correta da variável data_formatada.
            Rio de Janeiro.
        """

conteudo = "Você é um procurador com mais de 20 anos de experiência no município do estado do rio de janeiro. Você irá analisar minuciosamente o documento enviado e responder com base neste documento citado. Evite erros de ortografia na linguagem Português Brasil"