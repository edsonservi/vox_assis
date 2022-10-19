import pygetwindow as gw
import datetime
import os
from random import choice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


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

    frase = f'{usuario}, em {local[1]}, a temperatura é de {temperatura} graus, ' \
            f'há {chuva} de chance de chover, o ar esta com ' \
            f'{umidade} de umidade e o vento está soprando a {vento}.'
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
