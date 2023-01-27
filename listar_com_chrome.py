from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time, listar_descrip, pprint

#browser = webdriver.Chrome()

opts = Options()
opts.add_argument('--headless')
browser = Chrome(options=opts)
browser.get('https://theonegenerator.com/pt/geradores/endereco/gerador-de-coordenadas/')
time.sleep(3)
gerar = browser.find_element(By.CSS_SELECTOR, "#app-content > section > div.container > div > div.col > div.generator-container > div > div > div > div.generator > form > button")

for f in range(50):    
    gerar.click()
    time.sleep(0.2)
    campo = browser.find_element(By.ID, "copyToClipboard-coord")
    time.sleep(0.1)
    #print(campo.get_attribute("value"))
    lat_lon = campo.get_attribute("value")
    stop_caract = ","
    stop_index = lat_lon.index(stop_caract)
    lat_bruto = lat_lon[0:stop_index]
    lon_bruto = lat_lon[9:]
    lat = lat_bruto.strip()
    lon = lon_bruto.strip()
    #print(f'Latitude={lat} e Longitude={lon}')
    result_api = listar_descrip.filtro_1(lat,lon)
    #linha_filt=listar_descrip.listar_description(result_api)
    retorno_filt = listar_descrip.listar_description(result_api)
    #for i in retorno_filt:
    #    print(i)
    
    time.sleep(1)
    print(f)
for i in retorno_filt:
    print(i)

browser.quit()