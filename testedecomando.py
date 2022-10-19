# ARQUIVO DE TESTE DE IMPLEMENTAÇÃO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


def clima(usuario):
    options = Options()
    options.add_argument('--headless')
    nav = webdriver.Chrome(options=options)
    nav.get('http:www.google.com')
    caminho = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
    nav.find_element('xpath', caminho).send_keys('clima São José - SC', Keys.ENTER)
    temperatura = nav.find_element('xpath', '//*[@id="wob_tm"]').text
    vento = nav.find_element('xpath', '//*[@id="wob_ws"]').text
    umidade = nav.find_element('xpath', '//*[@id="wob_hm"]').text
    chuva = nav.find_element('xpath', '//*[@id="wob_pp"]').text
    local = nav.find_element('xpath', '//*[@id="wob_loc"]').text
    local = local.split(',')
    nav.close()

    frase = f'{usuario}, em {local[1]} A temperatura é de {temperatura} graus, ' \
            f'há {chuva} de chance de chover, o ar esta com ' \
            f'{umidade} de umidade e o vento esta soprando a {vento}.'
    return frase


print(clima('Edson'))
"""
temperatura = nav.find_element('xpath', '//*[@id="OverviewCurrentTemperature"]/a').text
temperatura = temperatura.replace("°C", "")
temperatura = temperatura.replace(" ", "")
temperatura = temperatura.replace("\n", "")
temperatura = int(temperatura)
estado = nav.find_element('xpath', '//*[@id="OverviewCurrentTemperature"]/div/div[1]').text
chuva = nav.find_element('xpath', '//*[@id="ForecastDays"]/div/ul/li[1]/button/span/'
                                  'div/div/div[2]/div[2]/div[2]/div/span[2]').text
chuva = int(chuva.replace("%", ""))
nav.quit()
frase = f'{usuario}, A temperatura é de {temperatura} graus, está {estado} e há {chuva} ' \
        f'porcento de chances de chover.'
return frase
"""
