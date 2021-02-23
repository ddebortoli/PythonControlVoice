import speech_recognition as sr
import webbrowser
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def autoexec():
    "Funcion que obtiene un comando de voz dictado por el usuario"
    r = sr.Recognizer() 
    r.energy_threshold = 5000
    with sr.Microphone() as source:
        print('Di algo : ')
        audio = r.listen(source)
        text = 'none'
        try:
            text = r.recognize_google(audio,language= 'es-ES')
        except:
            print('Lo siento, no he podido detectar tu voz')
            text = 'vacio'
    return text

def findInList(command,show):
    "Funcion que muestra el listado de comandos u obtiene un comando existente"
    commands = pd.read_excel('Datos/Comandos.xlsx', sheet_name='ListadoDeWebs')
    for i in commands.index:
        if show:
            print(commands['COMANDO'][i] + "|" + commands['URL'][i])
        elif command == commands['COMANDO'][i]:
            return commands['URL'][i]
    return None    

def addNewCommand(command,url):
    "Funcion que inserta datos en el excel"
    
    commands = pd.read_excel('Datos/Comandos.xlsx', sheet_name='ListadoDeWebs')
    
    if findInList(command,False) != None:
        print("Error! El comando ya existe.")
    else:
        try:
            commands = commands.append({'COMANDO':command,'URL':url},ignore_index=True)
            print(commands)
            commands.to_excel("Datos/Comandos.xlsx",sheet_name='ListadoDeWebs')
        except:
            print("Error al guardar, intente nueveamente.")

def runCommand(command):
    "Funcion que ejecuta un comando"
    
    if command == 'AGREGAR WEB': #Si el comando es 'Agregar WEB' ejecuta la funcion addNewCommand
        print("Ingrese la sintaxis del comando:")
        newCommand = input()
        print("Ingrese la web a la que desea anexar este comando:")
        newUrl = input()
        addNewCommand(newCommand.upper(),newUrl)
        
    elif findInList(command,False) != None: #Si el comando dictado por el usuario esta en la lista, lo ejecuta
        webbrowser.open(findInList(command,False) , new=2, autoraise=True)
    elif command == 'MOSTRAR LISTA': #Muestra la lista de comandos
        findInList('pass',True)
        
    elif command == 'CERRAR PROGRAMA': #Termina el programa
        return False
    else:
        print("El comando dictado no corresponde con el listado disponible")
    return True

keepRuning = True
while(keepRuning):        
    keepRuning = runCommand(autoexec().upper())
    
    