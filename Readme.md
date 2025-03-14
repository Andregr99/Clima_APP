# 🌤️ **ClimaApp - Django** 🤩

Aplicação desenvolvida com **Django** e **Django REST Framework** para consumir a API do OpenWeatherMap, exibir informações meteorológicas em uma interface web e fornecer um **webservice REST** com os dados tratados.  


## ⚙️ **Funcionalidades**  

✅ Buscar clima de uma cidade através da API do OpenWeatherMap  
✅ Exibir informações meteorológicas na interface web  
✅ Criar um **endpoint REST** para fornecer os dados formatados  


## 🚀 **Tecnologias Utilizadas**  

- **Python 3.10+**  
- **Django** - Framework web  
- **Django REST Framework(DRF)** - Criação da API REST  
- **Requests** - Consumo da API externa  
- **CSS** - Estilização da interface  


## ⚙️ **Instalação e Execução**  

1️⃣ Clone este repositório:

git clone https://github.com/Andregr99/Clima_APP.git

No seu terminal Digite:
cd clima_project

2️⃣ Crie e ative um ambiente virtual:

Editar
python -m venv venv

Ativação:

(CMD): venv\Scripts\activate
(PowerShell): venv\Scripts\Activate.ps1

3️⃣ Instale as dependências:

pip install -r requirements.txt

4️⃣ Configure a chave da API OpenWeatherMap:
Crie um arquivo .envna raiz do projeto e adicione:

OPENWEATHER_API_KEY=SUA_CHAVE_AQUI

🔹 Obs: Você pode obter uma chave gratuita em **https://openweathermap.org/api** 😉


5️⃣ Migrações do banco de dados:

python manage.py migrate

6️⃣ Execute o servidor:

python manage.py runserver

Acesse no navegador:
🔹 Clique no link "http://127.0.0.1:8000/" no seu terminal enquanto segura a tecla Ctrl 🤩🚀🚀🚀

**Iniciando com Django REST Framework. Como estou iniciando minha jornada neste framework, feedbacks e sugestões são muito bem-vindos guys. Para dúvidas ou colaborações, entre em contato comigo pelo LinkedIn 🤩🤝**