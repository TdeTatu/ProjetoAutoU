# ProjetoAutoU

# IA-Mail

Analisador de Emails é uma aplicação web desenvolvida em Django que utiliza a API da OpenAI para classificar emails em "Produtivo" ou "Improdutivo" e sugerir respostas automáticas, otimizando o fluxo de trabalho e a comunicação.

**[>> Acesse a Demonstração Online <<](http://Jonatas12.pythonanywhere.com/)**

---

## 📖 Sobre o Projeto

Em ambientes corporativos com alto volume de emails, a triagem manual consome um tempo precioso. Muitos emails são mensagens que não exigem ação imediata (como agradecimentos ou felicitações), enquanto outros são solicitações críticas que precisam de atenção.

Esta aplicação resolve esse problema ao automatizar a leitura e classificação, liberando a equipe para focar em tarefas de maior valor.

### ✨ Funcionalidades Principais

* **Classificação com IA:** Analisa o conteúdo do email e o classifica como **Produtivo** ou **Improdutivo** .
* **Sugestão de Respostas:** Gera automaticamente uma resposta profissional e contextualizada em português, adequada à classificação do email.
* **Múltiplos Formatos de Entrada:** Permite ao usuário colar o texto do email diretamente ou fazer o upload de arquivos nos formatos `.txt` e `.pdf`.
* **Interface Moderna:** Possui uma interface limpa, responsiva e com tema escuro para uma melhor experiência do usuário.
* **Auto-Scroll Inteligente:** Após a análise, a página rola suavemente para exibir o resultado, melhorando a usabilidade.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Inteligência Artificial:** OpenAI API (GPT-4o)
* **Processamento de Arquivos:** PyPDF2
* **Banco de Dados (Local):** SQLite
* **Hospedagem (Deploy):** PythonAnywhere

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para configurar e executar o projeto no seu ambiente local.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO_AQUI]
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd ProjetoAutoU
    ```

3.  **Crie e ative um ambiente virtual:**

    * No Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Instale as dependências do projeto:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto (na mesma pasta que `manage.py`).
    * Adicione as seguintes variáveis a ele, substituindo pelos seus valores:
        ```
        # Gere uma nova chave secreta para o Django. Não use a de produção.
        SECRET_KEY="sua-secret-key-aleatoria-aqui"

        # Sua chave da API da OpenAI
        OPENAI_API_KEY="sk-..."
        ```

6.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

7.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8.  **Acesse a aplicação:**
    Abra seu navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Pronto!

---

## ☁️ Deploy

A aplicação está hospedada na plataforma PythonAnywhere e pode ser acessada através do link:
[http://Jonatas12.pythonanywhere.com](http://Jonatas12.pythonanywhere.com)

---

## 👨‍💻 Autor

**Jonatas Luiz Gomes dos Santos**

* **LinkedIn:** [www.linkedin.com/in/jônatas-luiz-gomes-dos-santos-a39b09377](www.linkedin.com/in/jônatas-luiz-gomes-dos-santos-a39b09377)
* **GitHub:** [https://github.com/TdeTatu](https://github.com/TdeTatu)