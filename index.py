import speech_recognition as sr
import webbrowser


listOfWebSites = {
        'ABRIR GOOGLE':'https://www.google.com/',
        'ABRIR FACEBOOK': 'https://www.facebook.com/',
        'ABRIR INSTAGRAM': 'https://www.instagram.com/'
        }

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


def runCommand(command):
    "Funcion que ejecuta un comando"
    if command == 'AGREGAR WEB':
        print("Ingrese la sintaxis del comando:")
        newCommand = input()
        print("Ingrese la web a la que desea anexar este comando:")
        newUrl = input()
        addItem = listOfWebSites.setdefault(newCommand.upper(),newUrl)
        
        print("{} agregado exitosamente con el comando!" .format(listOfWebSites[newCommand]))      
    elif listOfWebSites.get(command) != None:
        webbrowser.open(listOfWebSites.get(command) , new=2, autoraise=True)
    elif command == 'MOSTRAR LISTA':
        for key in listOfWebSites:
            print (key, ":", listOfWebSites[key])
        
    elif command == 'CERRAR PROGRAMA':
        return False
    else:
        print("El comando dictado no corresponde con el listado disponible")
    return True
   #webbrowser.open("https://www.instagram.com/", new=2, autoraise=True)

keepRuning = True
while(keepRuning):        
    keepRuning = runCommand(autoexec().upper())
    
    