import requests
import warnings

key_open = 'f1496ebe85ac1452998e7e43b65e6ac1'
key_netclima= '89e0c9d38f0b4b6c0354770cfaaca166'
#Previsão para 5 dias de 3h em 3h
#api.openweathermap.org/data/2.5/forecast?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric

#Previsão Atual
#api.openweathermap.org/data/2.5/weather?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric
#lat= '-9.72332'
#lon= '-48.2773131'
#url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric'

array_de_pontos = []
#array_de_pontos_unico = [800,804]
#{'id': 503, 'main': 'Rain', 'description': 'chuva muito forte', 'icon': '10d'}
#{'id': 602, 'main': 'Snow', 'description': 'nevasca', 'icon': '13n'}
#{'id': 504, 'main': 'Rain', 'description': 'chuva extrema', 'icon': '10d'}
#{'id': 504, 'main': 'Rain', 'description': 'chuva extrema', 'icon': '10n'}
array_de_pontos_unico = [804, 803, 801, 800, 802, 500, 501,502,504, 601, 600,503,602 ]
meu_set = set()

def requisicao(url):
    requisicao = requests.get(url, verify=False, timeout=200)
    warnings.simplefilter('ignore')
    requisicao_json = requisicao.json()
    return requisicao_json
    

def listar_description(dados):
       
    for d in dados:
        linha_filtrada = d['weather'][0]
        id_linha = linha_filtrada['id']
        if id_linha not in array_de_pontos_unico:
            array_de_pontos.append(linha_filtrada)

        #array_de_pontos.append(linha_filtrada)
    return array_de_pontos

  

def filtro_1(latitude, longitude):         
    lat = latitude
    lon = longitude
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric'
    req_json = requisicao(url)
    dados = req_json['list'] 

    return dados

#filtro_1(lista.lista_4)
'''
    for i in array_de_pontos:
        id_linha = i['id']
        if id_linha not in array_de_pontos_unico:
            array_de_pontos_unico.append(id_linha)
            print(i)
'''


