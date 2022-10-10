from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import acoes as act

# CONFIGURAÇÕES DE PERSONALIZAÇÃO
USUARIO = 'Edson'

# CONFIGURA GLOBAIS E INICIO OS SERVIÇOS
model = Model(r'vosk_model')
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
            if 'assis' in texto:
                texto = texto.replace(' assis', '')
                texto = texto.replace('assis ', '')
                testar = texto.split(' ')
                # SAUDAÇÃO
                if 'bom' in testar and 'dia' in testar \
                        or 'boa' in testar and 'tarde' in testar \
                        or 'boa' in testar and 'noite' in testar \
                        or 'olá' in testar or 'oi' in testar:
                    falar.say(act.saudacao(texto, USUARIO))
                    falar.runAndWait()
                # MUSICA
                elif 'música' in testar:
                    # TOCAR MUSICA
                    if 'tocar' in testar \
                            or 'executar' in testar \
                            or 'rodar' in testar:
                        falar.say(f"Abrindo player de música,  {USUARIO}")
                        falar.runAndWait()
                        act.musica()
                    # FECHAR MUSICA
                    elif 'fechar' in testar \
                            or 'encerrar' in testar \
                            or 'parar' in testar:
                        act.fechar_musica()
                        falar.say(f"Pronto,  {USUARIO}, sem música!")
                        falar.runAndWait()
                # CLIMA
                elif 'temperatura' in testar \
                        or 'clima' in testar \
                        or 'previsão' in testar:
                    falar.say(act.clima(USUARIO))
                    falar.runAndWait()
                # PALAVRÕES
                elif 'puta' in testar \
                        or 'viado' in testar \
                        or 'caralho' in testar \
                        or 'puta' in testar \
                        or 'cú' in testar \
                        or 'idiota' in testar \
                        or 'retardado' in testar \
                        or 'imbecil' in testar:
                    falar.say(act.xingamento(USUARIO))
                    falar.runAndWait()
                # ENCERRAR
                elif 'desligar' in testar \
                        or 'encerrar' in testar\
                        or 'dormir' in testar:
                    falar.say(f"Até mais, {USUARIO}, estou indo dormir!")
                    falar.runAndWait()
                    break
