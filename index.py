import pyaudio
import pywhatkit
import pyttsx3
import wikipedia
import datetime
import keyboard
import colors
import os
import subprocess
import speech_recognition as sr
from pygame import mixer
import subprocess as sub
import threading as tr


name = "luna"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites={
                    'google':'google.com',
                    'youtube': 'youtube.com',
                    'facebook':'facebook.com',
                    'whatsapp': 'web.whatsapp.com',
                    'cursos':'freecodecomp.org/learn'
}

files = {
    'carta':'Carta Pasantia.pdf',
    'cedula':'cedula.docx',
    'foto':'foto.jpg'
}

programs = {
    'google': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'heroes 5': r"P:\Heroes of Might and Magic V\Hammers of Fate\bin\H5_Game.exe",
    'lol': r"D:\Riot Games\Riot Client\RiotClientServices.exe",
    'gta 5': r"P:\Grand Theft Auto V\GTA5.exe",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'excel': r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'power Point': r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
    
}

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            talk("En que te puedo ayudar hoy?")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
            

    except:
        print("Ocurrio un Error!")
    return rec

#Funcion Principal

def run_luna():
    rec = listen()
    #Reproducir Youtube
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciendo " + music)
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)
    #Buscar Wikipedia
    elif 'busca' in rec:
        search = rec.replace('busca', '')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(search, 1)
        print(search +": " + wiki)
        talk(wiki)
    #Crear Alarma
    elif 'alarma' in rec:
        num = rec.replace('alarma', '')
        num = num.strip()
        talk("Alarma activada a las " + num + " horas")
        while True:
            if datetime.datetime.now().strftime('%H:%M') == num:
                print("Despierta!!")
                mixer.init()
                mixer.music.load("auronplay-alarma.mp3")
                mixer.music.play()
                if keyboard.read_key() == "s":
                    mixer.music.stop()
                    break
                
    #Abrir reconocimineto de Colores mediante la Camara Web
    elif 'colores' in rec:
        talk("Enseguida")
        colors.capture()

    #Abrir paginas Web
    elif 'abre' in rec:
        for site in sites:
            if site in sites:
                sub.call(f'start chrome.exe {sites[site]}', shell=True)
                talk(f'Abriendo {site}')
        for app in programs:
            if app in rec:
                talk(f'Abriendo {app}')
                sub.Popen(programs[app])

    #Abrir archivos
    elif 'archivo' in rec:
        for file in files:
            if file in rec:
                sub.Popen([files[file]], shell=True)
                talk(f'Abriendo {file}')
    elif 'escribe' in rec:
        try:
            with open("nota.txt", 'a') as f:
                write(f)

        except FileNotFoundError as e:
            file = open("nota.txt", 'w')
            write(file)
            
    elif 'termina' in rec:
        talk('Adios!')
        pass #Aqui el codigo era Break pero no lo reconoce (Verificar)

    elif 'apagar' in rec:
        talk('Apagando!')
        subprocess.run("shutdown -s") #Apagar PC

    elif 'reiniciar' in rec:
        talk('reiniciando!')
        subprocess.run("shutdown -r") #Reiniciar PC

    elif 'suspender' in rec:
        talk('sustendiendo!')
        subprocess.run("shutdown -l") #Suspender PC

def write(f):
    talk("Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, Puedes revisarlo")
    sub.Popen("nota.txt", shell=True)
    




if __name__ == '__main__':
    run_luna()