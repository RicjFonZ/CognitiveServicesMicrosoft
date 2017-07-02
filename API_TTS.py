# -*- coding: utf-8 -*-

import http.client
from configparser import ConfigParser
from xml.etree import ElementTree


def API_TTS(TEXT):
    config = ConfigParser()
    config.read('conf2.ini')
    KEY = config['speech_api']['key'];
    TTS_LANG = config['speech_api']['tts'];

    params = ""
    headers = {"Ocp-Apim-Subscription-Key": KEY}

    # AccessTokenUri = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken";
    AccessTokenHost = "api.cognitive.microsoft.com"
    path = "/sts/v1.0/issueToken"

    # Connect to server to get the Access Token
    print("Connect to server to get the Access Token")
    conn = http.client.HTTPSConnection(AccessTokenHost)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    data = response.read()
    conn.close()

    accesstoken = data.decode("UTF-8")
    print("Access Token: " + accesstoken)

    body = ElementTree.Element('speak', version='1.0')
    body.set('{http://www.w3.org/XML/1998/namespace}lang', 'pt-pt')
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (' + TTS_LANG + ')')
    voice.text = TEXT

    headers = {"Content-type": "application/ssml+xml",
               "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
               "Authorization": "Bearer " + accesstoken,
               "X-Search-AppId": "07D3234E49CE426DAA29772419F436CA",
               "X-Search-ClientID": "1ECFAE91408841A480F00935DC390960",
               "User-Agent": "TTSForPython"}

    # Connect to server to synthesize the wave
    print("\nConnect to server to synthesize the wave")
    conn = http.client.HTTPSConnection("speech.platform.bing.com")
    conn.request("POST", "/synthesize", ElementTree.tostring(body), headers)
    response = conn.getresponse()

    print(response.status, response.reason)

    data = response.read()

    file = open("resposta.mp3", "wb")
    file.write(data)
    file.close()
    conn.close()

    print("The synthesized wave length: %d" % (len(data)))
