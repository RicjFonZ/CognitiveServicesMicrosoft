# coding: utf8
import os
from random import shuffle
from tkinter import *
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk
from num2words import num2words

from API_AUDIO import *
from API_TTS import *
from API_VISION import *

# ******** LOAD CONFIGURATIONS *************
config = ConfigParser()
config.read('conf2.ini')


# ********* ALL MENUS AND WIDGET *************

def menu():
    frame_menu["bg"] = "aquamarine2"
    bt1 = Button(frame_menu, width=20, height=8, text="Síntese de Voz", command=call_voice)
    bt1.place(x=150, y=100)
    """
    bt2 = Button(frame_menu, width=20, height=8, text="????")
    bt2.place(x=500, y=100)
    """
    bt3 = Button(frame_menu, width=20, height=8, text="Reconhecimento de \nCelebridades", command=call_famous)
    bt3.place(x=500, y=100)
    bt4 = Button(frame_menu, width=20, height=8, text="Configurações", command=call_config)
    bt4.place(x=325, y=350)


def config():
    def limpar_speech():
        config = ConfigParser()
        config.read('conf2.ini')
        config.set('speech_api', 'key', '')
        config.set('speech_api', 'language', '')
        config.set('speech_api', 'tts', '')
        with open('conf2.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
        call_config()

    def limpar_vision():
        print("entrou")
        config = ConfigParser()
        config.read('conf2.ini')
        config.set('vision_api', 'key', '')
        with open('conf2.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
        call_config()

    def gravar_speech():
        key = en_key.get()
        lan = en_lan.get()
        tts = en_tts.get()

        config = ConfigParser()
        config.read('conf2.ini')
        config.set('speech_api', 'key', key)
        config.set('speech_api', 'language', lan)
        config.set('speech_api', 'tts', tts)
        with open('conf2.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
        call_config()

    def gravar_vision():
        key = en_key2.get()
        config = ConfigParser()
        config.read('conf2.ini')
        config.set('vision_api', 'key', key)
        with open('conf2.ini', 'w') as configfile:
            config.write(configfile)
            configfile.close()
        call_config()

    config = ConfigParser()
    config.read('conf2.ini')
    KEY_SPEECH = config['speech_api']['key'];
    LANGUAGUE = config['speech_api']['language'];
    TTS = config['speech_api']['tts'];
    KEY_VISION = config['vision_api']['key'];

    frame_config["bg"] = "aquamarine2"
    lb_tittle = Label(frame_config, text="Menu de Configurações", bg="aquamarine2", font=("Consolas", 20))
    lb_tittle.place(x=250, y=30)

    lb_sp = Label(frame_config, text=(("_" * 154)), bg="aquamarine2")
    lb_sp.place(x=10, y=65)

    lb_sp2 = Label(frame_config, text=(("_" * 154)), bg="aquamarine2")
    lb_sp2.place(x=10, y=520)

    bt_voltar = Button(frame_config, width=8, text="Voltar", command=call_menu)
    bt_voltar.place(x=375, y=550)

    # *************** BING SPEECH API ***********************

    lb_tittle_speech_api = Label(frame_config, text="Bing Speech API", bg="aquamarine2", font=("Consolas", 15))
    lb_tittle_speech_api.place(x=10, y=100)

    lb_key = Label(frame_config, text="API KEY:", bg="aquamarine2")
    lb_key.place(x=10, y=140)

    en_key = Entry(frame_config, width=35)
    en_key.insert(END, KEY_SPEECH)
    en_key.place(x=120, y=140)

    lb_lan = Label(frame_config, text="LANGUAGE:", bg="aquamarine2")
    lb_lan.place(x=10, y=165)

    en_lan = Entry(frame_config, width=35)
    en_lan.insert(END, LANGUAGUE)
    en_lan.place(x=120, y=165)

    lb_tts = Label(frame_config, text="TTS LANGUAGE:", bg="aquamarine2")
    lb_tts.place(x=10, y=190)

    en_tts = Entry(frame_config, width=35)
    en_tts.insert(END, TTS)
    en_tts.place(x=120, y=190)

    bt_speech_save = Button(frame_config, text="Gravar", command=gravar_speech)
    bt_speech_save.place(x=120, y=215)

    bt_speech_clean = Button(frame_config, text="Limpar", command=limpar_speech)
    bt_speech_clean.place(x=170, y=215)

    # ********************** BING COMPUTER VISION API ***********************

    lb_tittle_vision_api = Label(frame_config, text="Computer Vision API", bg="aquamarine2", font=("Consolas", 15))
    lb_tittle_vision_api.place(x=10, y=290)

    lb_key2 = Label(frame_config, text="API KEY:", bg="aquamarine2")
    lb_key2.place(x=10, y=330)

    en_key2 = Entry(frame_config, width=35)
    en_key2.insert(END, KEY_VISION)
    en_key2.place(x=120, y=330)

    bt_vision_save = Button(frame_config, text="Gravar", command=gravar_vision)
    bt_vision_save.place(x=120, y=355)

    bt_vision_clean = Button(frame_config, text="Limpar", command=limpar_vision)
    bt_vision_clean.place(x=170, y=355)


def voice():
    # ******FUNCOES DE APOIO***********

    def livre():

        def livre_ouvir():
            def baralhar():
                split = livre_ouvir.frase.split()
                shuffle(split)
                frase = ' '.join(split)

                API_TTS(frase)
                os.system('start \"\" resposta.mp3');

            def ouvir():
                API_TTS(livre_ouvir.frase)
                os.system('start \"\" resposta.mp3');

            def detalhes():
                palavras = len(livre_ouvir.frase.split())
                caracteres = len(livre_ouvir.frase)

                frase = "A frase tem " + str(palavras) + " palavras e " + str(caracteres) + " caracteres"

                API_TTS(frase)

                os.system('start \"\" resposta.mp3');

            audio = escutar_audio()
            resultado = audio_livre(audio)
            confi = (resultado[0])
            livre_ouvir.frase = (resultado[1])

            lb_frase = Label(frame_voice, text=livre_ouvir.frase, bg="aquamarine2", font=("bold"))
            lb_frase.place(x=140, y=250)

            lb_conf = Label(frame_voice, text=confi, bg="aquamarine2", font=("bold"))
            lb_conf.place(x=140, y=290)

            bt_ouvir = Button(frame_voice, width=8, text="Ouvir", command=ouvir)
            bt_ouvir.place(x=290, y=325)

            bt_detalhes = Button(frame_voice, width=8, text="Detalhes", command=detalhes)
            bt_detalhes.place(x=365, y=325)

            bt_detalhes = Button(frame_voice, width=8, text="Baralhar", command=baralhar)
            bt_detalhes.place(x=440, y=325)

        def ouvir_tx():
            frase_tx = (en_texto.get())
            API_TTS(frase_tx)
            os.system('start \"\" resposta.mp3');

        def detalhe_tx():
            palavras_tx = len(en_texto.get().split())
            caracteres_tx = len(en_texto.get())

            frase_tx = "A frase tem " + str(palavras_tx) + " palavras e " + str(caracteres_tx) + " caracteres"

            API_TTS(frase_tx)
            os.system('start \"\" resposta.mp3');

        def baralhar_tx():
            split = en_texto.get().split()
            shuffle(split)
            frase_tx = ' '.join(split)

            API_TTS(frase_tx)
            os.system('start \"\" resposta.mp3');

        def limpar_um():
            lb_branca = Label(frame_voice, width=100, height=8, bg="aquamarine2")
            lb_branca.place(x=130, y=230)

        def limpar_dois():
            pass

        lb_branca = Label(frame_voice, text=(" " * 600), width=108, height=26, bg="aquamarine2")
        lb_branca.place(x=25, y=130)

        lb_tittle_livre = Label(frame_voice, text="Modo de Texto Livre Ativo", bg="aquamarine2", font=("Consolas", 15))
        lb_tittle_livre.place(x=250, y=150)

        lb_sp = Label(frame_voice, text=(("- " * 97)), bg="aquamarine2")
        lb_sp.place(x=10, y=350)

        bt_voltar = Button(frame_voice, width=8, text="Voltar", command=call_menu)
        bt_voltar.place(x=360, y=550)

        bt_escutar_livre = Button(frame_voice, text="Escutar Audio", width=15, command=livre_ouvir)
        bt_escutar_livre.place(x=50, y=200)

        bt_limpar_livre = Button(frame_voice, text="Limpar", width=15, command=limpar_um)
        bt_limpar_livre.place(x=175, y=200)

        lb_frase = Label(frame_voice, text="Frase:", bg="aquamarine2", font=("bold"))
        lb_frase.place(x=50, y=250)

        lb_conf = Label(frame_voice, text="Confianca:", bg="aquamarine2", font=("bold"))
        lb_conf.place(x=50, y=290)

        lb_tittle_texto = Label(frame_voice, text="Escreva Texto", bg="aquamarine2", font=("Consolas", 15))
        lb_tittle_texto.place(x=315, y=370)

        en_texto = Entry(frame_voice, width=115)
        en_texto.place(x=45, y=425)

        bt_ouvir_tx = Button(frame_voice, width=12, text="Ouvir o Texto", command=ouvir_tx)
        bt_ouvir_tx.place(x=210, y=475)

        bt_detalhes_tx = Button(frame_voice, width=15, text="Detalhes do Texto", command=detalhe_tx)
        bt_detalhes_tx.place(x=345, y=475)

        bt_detalhes_tx = Button(frame_voice, width=12, text="Baralhar o Texto", command=baralhar_tx)
        bt_detalhes_tx.place(x=490, y=475)

    def comandos():

        def escutar_comando():
            audio = escutar_audio()
            resultado = comandos_voz(audio)
            print(resultado)

            if 'tudo bem' in resultado:
                frase = 'Estou bem, obrigado'
                API_TTS(frase)
                os.system('start \"\" resposta.mp3');

            # Diz-me o nome do utilizador (getpass) -> Username é %

            # Abrir o meu Facebook -> Abre face
            if 'facebook' in resultado:
                os.system('start \"\" https://www.facebook.com/ricardofnsc');

            if 'youtube' in resultado:
                os.system('start \"\" https://www.youtube.com/');

            if 'bloco de notas' in audio:
                os.system('start \"\" notepad.exe');

        lb_branca = Label(frame_voice, text=(" " * 600), width=108, height=26, bg="aquamarine2")
        lb_branca.place(x=25, y=130)

        lb_tittle_comandos = Label(frame_voice, text="Modo de Comandos de Voz Ativo", bg="aquamarine2",
                                   font=("Consolas", 15))
        lb_tittle_comandos.place(x=225, y=150)

        bt_escutar_comandos = Button(frame_voice, text="Escutar Audio", width=15, command=escutar_comando)
        bt_escutar_comandos.place(x=335, y=300)

    def matematica():
        def mat_repro():
            numero = str(mat_ouvir.resultado)
            numero = numero.replace(".", ",")

            API_TTS("O resultado é " + numero)

            os.system('start \"\" resposta.mp3');
            # print(mat_ouvir.resultado)

        def mat_ouvir():
            lb_lexical = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_lexical.place(x=183, y=275)

            lb_operacao = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_operacao.place(x=215, y=300)

            lb_resultado = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_resultado.place(x=130, y=325)

            lb_confianca = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_confianca.place(x=130, y=350)

            audio = escutar_audio()
            resultados = mat(audio)

            lexical = resultados[2]
            operacao = resultados[1]
            mat_ouvir.resultado = resultados[3]
            confianca = resultados[0]

            result = mat_ouvir.resultado, '(' + (num2words(mat_ouvir.resultado, lang='pt_BR')) + ')'

            lb_lexical = Label(frame_voice, text=lexical, bg="aquamarine2", font=("bold"))
            lb_lexical.place(x=183, y=275)

            lb_operacao = Label(frame_voice, text=operacao, bg="aquamarine2", font=("bold"))
            lb_operacao.place(x=215, y=300)

            lb_resultado = Label(frame_voice, text=result, bg="aquamarine2", font=("bold"))
            lb_resultado.place(x=130, y=325)

            lb_confianca = Label(frame_voice, text=confianca, bg="aquamarine2", font=("bold"))
            lb_confianca.place(x=130, y=350)

            bt_ouvir_mat = Button(frame_voice, text="Reproduzir Audio", width=15, command=mat_repro)
            bt_ouvir_mat.place(x=340, y=400)

        def mat_limpar():
            lb_lexical = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_lexical.place(x=183, y=275)

            lb_operacao = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_operacao.place(x=215, y=300)

            lb_resultado = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_resultado.place(x=130, y=325)

            lb_confianca = Label(frame_voice, text=(" " * 90), bg="aquamarine2", font=("bold"))
            lb_confianca.place(x=130, y=350)

            lb_confianca = Label(frame_voice, width=25, height=5, bg="aquamarine2")
            lb_confianca.place(x=300, y=350)

        lb_branca = Label(frame_voice, text=(" " * 600), width=108, height=26, bg="aquamarine2")
        lb_branca.place(x=25, y=130)

        lb_tittle_matematica = Label(frame_voice, text="Modo de Matematica Ativo", bg="aquamarine2",
                                     font=("Consolas", 15))
        lb_tittle_matematica.place(x=260, y=150)

        bt_escutar_mat = Button(frame_voice, text="Escutar Audio", width=15, command=mat_ouvir)
        bt_escutar_mat.place(x=275, y=190)

        bt_limpar_mat = Button(frame_voice, text="Limpar", width=15, command=mat_limpar)
        bt_limpar_mat.place(x=400, y=190)

        lb_operacao = Label(frame_voice, text="Operacao Lexical:", bg="aquamarine2", font=("bold"))
        lb_operacao.place(x=50, y=275)

        lb_operacao_mat = Label(frame_voice, text="Operacao Matematica:", bg="aquamarine2", font=("bold"))
        lb_operacao_mat.place(x=50, y=300)

        lb_operacao_resultado = Label(frame_voice, text="Resultado:", bg="aquamarine2", font=("bold"))
        lb_operacao_resultado.place(x=50, y=325)

        lb_operacao_canfianca = Label(frame_voice, text="Confianca:", bg="aquamarine2", font=("bold"))
        lb_operacao_canfianca.place(x=50, y=350)

    frame_voice["bg"] = "aquamarine2"
    lb_tittle = Label(frame_voice, text="Sintese de Voz", bg="aquamarine2", font=("Consolas", 20))
    lb_tittle.place(x=290, y=30)

    lb_sp = Label(frame_voice, text=(("_" * 154)), bg="aquamarine2")
    lb_sp.place(x=10, y=65)

    lb_sp2 = Label(frame_voice, text=(("_" * 154)), bg="aquamarine2")
    lb_sp2.place(x=10, y=520)

    bt_voltar = Button(frame_voice, width=8, text="Voltar", command=call_menu)
    bt_voltar.place(x=360, y=550)

    # ************** BOTOES DE COMANDO **********************+

    bt_livre = Button(frame_voice, width=20, text="Modo Texto Livre", command=livre)
    bt_livre.place(x=50, y=100)

    bt_comandos = Button(frame_voice, width=20, text="Modo Comandos de Voz", command=comandos)
    bt_comandos.place(x=325, y=100)

    bt_matematica = Button(frame_voice, width=20, text="Modo Matematica", command=matematica)
    bt_matematica.place(x=600, y=100)


def famous():
    def limpar_famous():
        lb_result_cel = Label(frame_famous, text=(" " * 90), bg="aquamarine2")
        lb_result_cel.place(x=490, y=190)

        lb_result_conf = Label(frame_famous, text=(" " * 90), bg="aquamarine2")
        lb_result_conf.place(x=480, y=230)

        lb_des = Label(frame_famous, text=(" " * 90), bg="aquamarine2")
        lb_des.place(x=479, y=310)

        lb_con_des = Label(frame_famous, text=(" " * 90), bg="aquamarine2")
        lb_con_des.place(x=551, y=350)

        lb_des = Label(frame_famous, width=54, height=28, bg="aquamarine2")
        lb_des.place(x=13, y=95)

        call_famous()

    def open_image():
        open_image.filename = askopenfilename(
            filetypes=[('Images files (*.jpeg, *.jpg, *.gif, *.bmp)', ('*.jpeg', '*.jpg', '*.gif', '*.bmp'))])
        image = Image.open(open_image.filename)
        image = image.resize((365, 425), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = Label(frame_famous, image=photo)
        label.image = photo
        label.place(x=13, y=95)

    def verify():

        celebridade = ""
        print(open_image.filename)
        config = ConfigParser()
        config.read('conf2.ini')
        key_api_vision = config['vision_api']['key'];
        # r = detect_celebrity("ill.jpeg", APIKEY)
        r = detect_celebrity(open_image.filename, key_api_vision)
        print(r.content)
        print(r.status_code)
        # nome
        celebridade = r.content['categories'][0]['detail']['celebrities'][0]['name']

        # confianca
        cel_confi = r.content['categories'][0]['detail']['celebrities'][0]['confidence']

        for i in r.content['description']['tags']:
            print(i)

            # descricao
        descricao = r.content['description']['captions'][0]['text']

        # confianca da descricao
        conf_desc = r.content['description']['captions'][0]['confidence']

        lb_result_cel = Label(frame_famous, text=celebridade, bg="aquamarine2")
        lb_result_cel.place(x=490, y=190)

        lb_result_conf = Label(frame_famous, text=cel_confi, bg="aquamarine2")
        lb_result_conf.place(x=480, y=230)

        if (int(len(descricao)) >= 59):
            print("entro")
            descricao = descricao[:59] + '\n' + descricao[59:]
            print(descricao)
        lb_des = Label(frame_famous, text=descricao, bg="aquamarine2")
        lb_des.place(x=479, y=310)

        lb_con_des = Label(frame_famous, text=conf_desc, bg="aquamarine2")
        lb_con_des.place(x=551, y=350)

    frame_famous["bg"] = "aquamarine2"
    lb_tittle = Label(frame_famous, text="Reconhecimento de Celebridades", bg="aquamarine2", font=("Consolas", 20))
    lb_tittle.place(x=185, y=30)

    lb_sp = Label(frame_famous, text=(("_" * 154)), bg="aquamarine2")
    lb_sp.place(x=10, y=65)

    lb_sp2 = Label(frame_famous, text=(("_" * 154)), bg="aquamarine2")
    lb_sp2.place(x=10, y=520)

    lb_sp3 = Label(frame_famous, text=(("|\n" * 31)), bg="aquamarine2")
    lb_sp3.place(x=390, y=72)

    bt_voltar = Button(frame_famous, width=8, text="Voltar", command=call_menu)
    bt_voltar.place(x=360, y=550)

    bt_abrir = Button(frame_famous, width=10, text="Abrir Foto", command=open_image)
    bt_abrir.place(x=425, y=100)

    bt_limpar = Button(frame_famous, width=10, text="Limpar", command=limpar_famous)
    bt_limpar.place(x=550, y=100)

    bt_pedir = Button(frame_famous, width=10, text="Verificar", command=verify)
    bt_pedir.place(x=675, y=100)

    lb_tittle_resultado = Label(frame_famous, text="Resultados", bg="aquamarine2", font=("Consolas", 15))
    lb_tittle_resultado.place(x=420, y=150)

    # ****RESULTADOS******

    lb_cel = Label(frame_famous, text="Celebridade:", bg="aquamarine2")
    lb_cel.place(x=420, y=190)

    lb_con = Label(frame_famous, text="Confiança:", bg="aquamarine2")
    lb_con.place(x=420, y=230)

    lb_tittle_resultado = Label(frame_famous, text="Informação Adicional", bg="aquamarine2", font=("Consolas", 15))
    lb_tittle_resultado.place(x=420, y=270)

    # ****ADICINAL******

    lb_cel = Label(frame_famous, text="Descrição:", bg="aquamarine2")
    lb_cel.place(x=420, y=310)

    lb_con = Label(frame_famous, text="Confiança da Descrição:", bg="aquamarine2")
    lb_con.place(x=420, y=350)

    lb_con = Label(frame_famous, text="Tags:", bg="aquamarine2")
    lb_con.place(x=420, y=390)


# ***********CALL FUNCTIONS***********

def call_config():
    config()
    frame_config.place(x=0, y=0)
    frame_menu.place_forget()
    frame_famous.place_forget()
    frame_voice.place_forget()


def call_menu():
    frame_menu.place(x=0, y=0)
    frame_config.place_forget()
    frame_voice.place_forget()
    frame_famous.place_forget()


def call_voice():
    frame_menu.place_forget()
    frame_config.place_forget()
    frame_voice.place(x=0, y=0)
    frame_famous.place_forget()


def call_famous():
    famous()
    frame_famous.place(x=0, y=0)
    frame_menu.place_forget()
    frame_config.place_forget()
    frame_voice.place_forget()


# *********ROOT CONFIGURATIONS*********

root = Tk()

window_width = 800
window_heigth = 600

root.title("Serviços Cognitivos Microsoft")
root["bg"] = "aquamarine2"
root.iconbitmap('icon.ico')
window_size = "800x600+300+50"
root.geometry(window_size)
root.resizable(width=False, height=False)

# CREATE ALL FRAMES
frame_menu = Frame(root, width=window_width, height=window_heigth)
frame_menu.place(x=0, y=0)

frame_config = Frame(root, width=window_width, height=window_heigth)
frame_config.place(x=0, y=0)

frame_voice = Frame(root, width=window_width, height=window_heigth)
frame_voice.place(x=0, y=0)

frame_famous = Frame(root, width=window_width, height=window_heigth)
frame_famous.place(x=0, y=0)

# CALL WINDOWS
menu()
config()
voice()
famous()

# HIDE FRAMES
frame_config.place_forget()
frame_voice.place_forget()
frame_famous.place_forget()
# frame_menu.place_forget()

root.mainloop()
