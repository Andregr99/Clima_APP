import requests
import os
from django.http import JsonResponse
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import ClimaSerializer

load_dotenv()

def obter_dados_clima(cidade):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return {"erro": "Chave de API não configurada. Entre em contato com o suporte."}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  # Lança exceção para erros HTTP (4xx e 5xx)
        dados = resposta.json()

        return {
            "cidade": dados.get("name"),
            "temperatura": f"{dados['main']['temp']}°C",
            "sensacao_termica": f"{dados['main']['feels_like']}°C",
            "umidade": f"{dados['main']['humidity']}%",
            "descricao": dados['weather'][0]['description'].capitalize()
        }

    except requests.exceptions.Timeout:
        return {"erro": "Tempo de resposta excedido. Tente novamente mais tarde."}

    except requests.exceptions.ConnectionError:
        return {"erro": "Falha de conexão. Verifique sua internet e tente novamente."}

    except requests.exceptions.HTTPError as e:
        if resposta.status_code == 404:
            return {"erro": f"Cidade '{cidade}' não encontrada. Verifique o nome e tente novamente."}
        return {"erro": f"Erro ao acessar a API: {e}"}

    except Exception as e:
        return {"erro": f"Ocorreu um erro inesperado: {e}"}

def buscar_clima(request, cidade):
    clima = obter_dados_clima(cidade)
    if "erro" in clima:
        return JsonResponse(clima, status=400)
    return JsonResponse(clima)

@api_view(['GET'])
def clima_api(request, cidade):
    clima = obter_dados_clima(cidade)
    if "erro" in clima:
        return Response(clima, status=400)
    serializer = ClimaSerializer(clima)
    return Response(serializer.data)

def index(request):
    cidade = request.GET.get('cidade', "Ribeirão Preto")
    clima = obter_dados_clima(cidade)
    return render(request, 'clima_app/index.html', {"clima": clima})
