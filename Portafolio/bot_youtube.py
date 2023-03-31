import pywhatkit

print("Bienvenido")
print("Que video o canal de youtube quieres ver?:")

video = str(input())

try:
    pywhatkit.playonyt(video)

    print("Buscando y reproduciendo...")
except:

    print("Error x(")