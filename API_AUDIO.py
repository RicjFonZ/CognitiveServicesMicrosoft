from configparser import ConfigParser

from API_AUDIO import *


# ***********ESCUTAR AUDIO***************

def escutar_audio():
    config = ConfigParser()
    config.read('conf2.ini')
    KEY = config['speech_api']['key'];
    LANGUAGUE = config['speech_api']['language'];

    recognizer = sr.Recognizer();
    microphone = sr.Microphone();

    isLoop = True;

    print('Escutar Audio...\n');

    while isLoop:
        with microphone as source:

            recognizer.adjust_for_ambient_noise(source);
            audio = recognizer.listen(source);

        try:
            audio = str(recognizer.recognize_bing(audio, key=KEY, language=LANGUAGUE, show_all=True));

            # resultados = mat(audio);

            # print('Foi aqui' + str(resultados))

            isLoop = False;


        except sr.UnknownValueError as e:
            print('Não entendi', e);
            continue;
        except sr.RequestError as e:
            print('Não consegui fazer o pedido ao Servidor', e);
            continue;

    print('Operacao Completa');
    return audio


# ************ MODO MATEMATICA ************
def mat(audio):
    print('Modo Matematica Ativo\n');

    print('Audio Original:', audio);

    json_string = audio.replace("'", "\"")
    for ch in ['[', ']']:
        json_string_final = json_string.replace(ch, "")
        json_string = json_string_final

    print("JSON tratado:", json_string_final, '\n')

    resultado = json.loads(json_string_final);
    status = (resultado['header']['status'])

    if status == "error":
        print("Resultado do status:", status)
    else:
        print("Resultado do status:", status)

        name = (resultado['results']['name'])
        lexical = (resultado['results']['lexical'])
        confidence = (resultado['results']['confidence'])

        """
        print('Confianca:',confidence)
        print('Operacao:',name)
        print('Extensao:',lexical)
        print ('Resultado:',calculo_auxiliar(name))
        """

        resultados = []
        resultados.append(confidence)
        resultados.append(name)
        resultados.append(lexical)
        resultados.append(calculo_auxiliar(name))
        return resultados


def calculo_auxiliar(equacao):
    if '+' in equacao:
        y = equacao.split('+')
        x = int(y[0]) + int(y[1])

    elif '-' in equacao:
        y = equacao.split('-')
        x = int(y[0]) - int(y[1])

    elif '*' in equacao:
        y = equacao.split('*')
        x = int(y[0]) * int(y[1])

    elif '÷':
        y = equacao.split('÷')
        x = int(y[0]) / int(y[1])

    else:
        print('Não foi possivel reconhecer a operação')

    return x


# ************ MODO TEXTO LIVRE ************

def audio_livre(audio):
    print('Modo Audio Livre Ativo\n');

    print('Audio Original:', audio);

    json_string = audio.replace("'", "\"")
    for ch in ['[', ']']:
        json_string_final = json_string.replace(ch, "")
        json_string = json_string_final

    print("JSON tratado:", json_string_final, '\n')

    resultado = json.loads(json_string_final);
    status = (resultado['header']['status'])

    if status == "error":
        print("Resultado do status:", status)
    else:
        print("Resultado do status:", status)

        name = (resultado['results']['name'])
        confidence = (resultado['results']['confidence'])

        resultados = []
        resultados.append(confidence)
        resultados.append(name)
        return resultados


# ************MODO COMANDOS DE VOZ****************
def comandos_voz(audio):
    print('Modo Audio Livre Ativo\n');

    print('Audio Original:', audio);

    json_string = audio.replace("'", "\"")
    for ch in ['[', ']']:
        json_string_final = json_string.replace(ch, "")
        json_string = json_string_final

    print("JSON tratado:", json_string_final, '\n')

    resultado = json.loads(json_string_final);
    status = (resultado['header']['status'])

    if status == "error":
        print("Resultado do status:", status)
    else:
        print("Resultado do status:", status)

        name = (resultado['results']['name'])
        return name
