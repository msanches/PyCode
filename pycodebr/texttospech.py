#Convertendo texto em fala com Python
#pip install pyttsx3

import pyttsx3

#carrega a lib
engine = pyttsx3.init()

#texto
engine.say("Olá Cristina")
#engine.say("Eu sou o samba")
engine.say("Gostosona")

#executa
engine.runAndWait()