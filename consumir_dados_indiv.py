import requests
import pprint
import lista

key_open = 'f1496ebe85ac1452998e7e43b65e6ac1'
key_netclima= '89e0c9d38f0b4b6c0354770cfaaca166'
#Previsão para 5 dias de 3h em 3h
#api.openweathermap.org/data/2.5/forecast?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric

#Previsão Atual
#api.openweathermap.org/data/2.5/weather?lat={{lat_jari}}&lon={{long_jari}}&appid={{key_openweather}}&lang=pt_br&units=metric
lat= '-9.72332'
lon= '-48.2773131'
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric&cnt=3'
url_2 = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&appid={key_open}&lang=pt_br&units=metric&cnt=3'
url_diario = f'https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&mode=json&cnt=3&lang=pt_br&units=metric&apikey={key_netclima}'
url_hora = f'https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&mode=json&appid={key_netclima}&units=metric&lang=pt_br&cnt=9&_=1672315205140'
#&_=1672315205146


def requisicao(url):
    requisicao = requests.get(url,verify=False, timeout=200)
    requisicao_json = requisicao.json()
    return requisicao_json
    


req_json = requisicao(url_hora)
#rain = req_json['list'][0]['rain']
#pop = req_json['list'][0]['pop']
pprint.pprint(req_json)

    