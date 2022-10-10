import pygetwindow as gw
import datetime
import os
from random import choice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


def clima(usuario):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--start-maximized')
    nav = webdriver.Chrome(options=options)
    nav.get('https://www.msn.com/pt-br/clima/forecast/in-S%C3%A3o-Jos%C3%A9,Santa-Catarina')
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


def saudacao(texto, usuario):
    frase = f"{texto} {usuario}, agora é {datetime.datetime.now().strftime('%H:%M')}, " \
            f"hoje é dia, {datetime.datetime.now().strftime('%d/%m')}."
    return frase


def xingamento(usuario):
    frase = f"Não use termos de baixo calão comigo {usuario}, seu filha de uma puta do caralho!"
    return frase


def musica():
    caminho = os.walk(r'F:\Musica')
    musicas = []
    for arquivo in caminho:
        for itens in arquivo:
            for x in itens:
                if 'mp3' in x:
                    musicas.append(x)

    escolha = f'F:\\Musica\\{choice(musicas)}'
    janela = gw.getActiveWindow()
    sleep(2)
    os.startfile(escolha)
    sleep(2)
    janela.activate()


def fechar_musica():
    janela = gw.getWindowsWithTitle('Reprodutor de Mídias VLC')[0]
    janela.close()
