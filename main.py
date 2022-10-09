from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import acoes as act

USUARIO = 'Edson'

# CONFIGURA GLOBAIS E INICIA OS SERVIÇOS
model = Model(r'F:\Programacao\Voskmodels\vosk-model-small-pt-0.3')
voz = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
falar = pyttsx3.init()

# LOOP PARA MANTER O ASSISTENTE "SEMPRE OUVINDO"
while True:
    data = stream.read(4096, exception_on_overflow=False)
    if voz.AcceptWaveform(data):
        texto = voz.Result()
        texto = texto[14:-3].lower()
        if texto != '':
            texto = texto.replace(' assis', '')
            print(f'Texto sem o assis: {texto}')
            saudacao = ['bom dia', 'boa tarde', 'olá', 'oi', 'boa noite']
            clima = ['temperatura', 'previsão do tempo', 'clima']
            errado = ['veado', 'puta', 'caralho', 'cú', 'filha da puta', 'viado']
            if texto in saudacao:
                falar.say(act.saudacao(texto, USUARIO))
                falar.runAndWait()
            elif texto in clima:
                falar.say(act.clima(USUARIO))
                falar.runAndWait()
            elif texto in errado:
                falar.say(act.xingamento(USUARIO))
                falar.runAndWait()
            elif texto == 'música':
                falar.say(f"Abrindo player de música,  {USUARIO}")
                falar.runAndWait()
                act.musica()
            elif texto == 'fechar música':
                act.fechar_musica()
                falar.say(f"Pronto,  {USUARIO}, sem música!")
                falar.runAndWait()
            elif texto == 'desligar':
                falar.say(f"Até mais, {USUARIO}, estou indo dormir!")
                falar.runAndWait()
                break
