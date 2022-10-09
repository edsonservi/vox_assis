from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

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
            if "assis" in texto:
                testar = texto.split(' ')
                clima = ['temperatura', 'previsão do tempo', 'clima']
                errado = ['veado', 'puta', 'caralho', 'cú', 'filha da puta', 'viado']
                if 'música' in testar and 'tocar' in testar:
                    falar.say(texto)
                    falar.runAndWait()
                elif 'música' in testar and 'fechar' in testar:
                    falar.say(texto)
                    falar.runAndWait()
                elif 'bom' in testar and 'dia' in testar \
                        or 'boa' in testar and 'tarde' in testar \
                        or 'boa' in testar and 'noite' in testar \
                        or 'olá' in testar\
                        or 'oi' in testar:
                    falar.say('Deu certo!!')
                    falar.runAndWait()
                    falar.say(texto)
                    falar.runAndWait()
