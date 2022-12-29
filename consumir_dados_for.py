import requests
import pprint
import lista

key_open = 'f1496ebe85ac1452998e7e43b65e6ac1'
#Previsão para 5 dias de 3h em 3h
#api.openweathermap.org/data/2.5/forecast?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric

#Previsão Atual
#api.openweathermap.org/data/2.5/weather?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric
#lat= '-9.72332'
#lon= '-48.2773131'
#url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric'


def requisicao(url):
    requisicao = requests.get(url,verify=False, timeout=200)
    requisicao_json = requisicao.json()
    return requisicao_json
    

for i in lista.lista_2:
    #req_json = requisicao(url)
    #pprint.pprint(req_json)   
    lat = i['Latitude']
    lon = i['Longitude']
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric'
    req_json = requisicao(url)
    rain = req_json['list'][0]['rain']
    print(i['Ponto'],rain)
    