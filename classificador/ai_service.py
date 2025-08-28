# classificador/ai_service.py
    
import openai
from django.conf import settings
import json

def analyze_email_with_openai(content):
    try:
        openai.api_key = settings.OPENAI_API_KEY

        # --- PROMPT PARA IA(gpt-4o) ---
        prompt = f"""
        **Sua Identidade e Objetivo:**
        Você é um assistente de IA especialista em comunicação empresarial e produtividade, integrado a um sistema de gerenciamento de emails. Sua tarefa é analisar o conteúdo de um email e retornar uma análise estruturada em formato JSON.

        **Formato de Saída Obrigatório:**
        A sua resposta DEVE ser um objeto JSON válido com três chaves:
        1. "classification": (string) A classificação do email.
        2. "reasoning": (string) Uma frase curta e clara explicando o porquê da classificação.
        3. "suggested_response": (string) A sugestão de resposta em português.

        **Definições das Categorias de Classificação:**
        - "Produtivo": Emails que requerem uma ação direta, decisão ou fornecimento de informação pela equipe.
          - Exemplos: Perguntas sobre produtos/serviços, solicitações de suporte técnico, agendamento de reuniões, envio de documentos importantes para revisão, pedidos de orçamento.
        - "Improdutivo": Emails que são puramente informacionais, sociais, automatizados ou de marketing, e não necessitam de uma ação direta da equipe.
          - Exemplos: Agradecimentos ("Obrigado!"), mensagens de feriado ("Feliz Natal"), newsletters, notificações automáticas de sistema (ex: 'backup concluído'), spam.

        **Regras para a Geração da Resposta Sugerida:**
        - Se a classificação for "Produtivo", a resposta deve ser em português, profissional, concisa e proativa. Ela deve acusar o recebimento, demonstrar que o email foi compreendido e, se possível, indicar o próximo passo (ex: "Nossa equipe irá analisar sua solicitação...").
        - Se a classificação for "Improdutivo", a resposta deve ser um reconhecimento curto e educado (ex: "Recebido, obrigado!", "Obrigado pelo contato!", ou simplesmente não sugerir resposta se for um spam/newsletter).

        **Email a ser Analisado:**
        ---
        {content}
        ---

        **Objeto JSON de Resposta:**
        """

        response = openai.chat.completions.create(
            model="gpt-4o",  
            messages=[
                {"role": "system", "content": "Você é um assistente especialista em análise de emails que responde estritamente em formato JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.3, 
            max_tokens=500
        )

        result_text = response.choices[0].message.content
        result_json = json.loads(result_text)

        # Extraindo os valores do JSON. 
        classification = result_json.get('classification', 'Erro')
        suggested_response = result_json.get('suggested_response', 'Não foi possível gerar uma resposta.').strip()
        
        # Possibilidade de exibir a "razão" da classificação:
        # reasoning = result_json.get('reasoning', '') 
        # print(f"Razão da IA: {reasoning}")

        return classification, suggested_response

    except openai.APIStatusError as e:
        print(f"Erro na API da OpenAI: {e}")
        error_message = e.response.json().get("error", {}).get("message", "Erro desconhecido.")
        return "Erro de API", f"Ocorreu um erro ao processar sua solicitação: {error_message}"
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return "Erro de Código", f"Ocorreu um erro inesperado: {e}"