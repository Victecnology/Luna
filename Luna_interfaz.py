import pyaudio
import pywhatkit, pyttsx3, wikipedia, datetime, keyboard, colors, os
import speech_recognition as sr
from pygame import mixer
import subprocess as sub
import threading as tr
from tkinter import *
from PIL import Image, ImageTk



main_window = Tk()
main_window.title("Luna IA")

main_window.geometry("800x400")
main_window.resizable(0,0) # Linea de codigo para inhabilitar Maximizar pantalla
main_window.configure(bg='#00B4DB')

label_title = Label(main_window, text="Luna IA", bg="#6DD5FA", fg="#2c3e50",
                    font=('Arial', 30, 'bold'))
label_title.pack(pady=10)


#Lina de Codigo para colocar una foto en el interfaz

#luna_photo = ImageTk.PhotoImage(Image.open("#Nombre de la foto"))

#window_photo = Label(main_window, image=nombre de la imagen)
#window_photo.pack(pady=5)


def mexican_voice():
    change_voice(0)

def spanish_voice():
    change_voice(1)

def english_voice():
    change_voice(2)

def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("Hola!, Soy Luna")

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

def write(f):
    talk("Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, Puedes revisarlo")
    sub.Popen("nota.txt", shell=True)



button_voice_mx = Button(main_window, text="Voz Mexico", fg="white", bg="green",
                            font=("Arial", 10, "bold"), command=mexican_voice)
button_voice_mx.place(x=500, y=180, width=100, height=30)
button_voice_mx = Button(main_window, text="Voz España", fg="white", bg="red",
                            font=("Arial", 10, "bold"), command=spanish_voice)
button_voice_mx.place(x=500, y=130, width=100, height=30)
button_voice_mx = Button(main_window, text="Voz USA", fg="white", bg="blue",
                            font=("Arial", 10, "bold"), command=english_voice)
button_voice_mx.place(x=500, y=80, width=100, height=30)

    

main_window.mainloop()