# classificador/views.py

#imports
from django.shortcuts import render
import PyPDF2
import io
from .ai_service import analyze_email_with_openai


def index(request):
    context = {}

    if request.method == 'POST':
        email_content = ""
        
        text_from_textarea = request.POST.get('email_text')
        uploaded_file = request.FILES.get('email_file')

        if uploaded_file:
            if uploaded_file.name.endswith('.pdf'):
                try:
                    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
                    for page in pdf_reader.pages:
                        email_content += page.extract_text() or ""
                except Exception as e:
                    email_content = f"Erro ao ler o arquivo PDF: {e}"

            elif uploaded_file.name.endswith('.txt'):
                try:
                    email_content = uploaded_file.read().decode('utf-8')
                except Exception as e:
                    email_content = f"Erro ao ler o arquivo TXT: {e}"
            else:
                email_content = "Formato de arquivo não suportado."

        elif text_from_textarea:
            email_content = text_from_textarea
        
        if email_content and not email_content.startswith("Erro"):
            classification, suggested_response = analyze_email_with_openai(email_content)
            context['classification'] = classification
            context['suggested_response'] = suggested_response.strip()
            context['scroll_to_result'] = True
        
        # Se o formulário foi enviado (POST) mas não conseguimos um conteúdo...
        else:
            context['classification'] = "Erro"
            context['suggested_response'] = email_content or "Formulário enviado vazio. Por favor, cole um texto ou envie um arquivo."
            context['scroll_to_result'] = True 

    return render(request, 'classificador/index.html', context)