import pywhatkit

print("Bienvenido")
print("Que quieres buscar?:")

try:

    valor = str(input())

    pywhatkit.search(valor)

    print("Buscando...")
except:

    print("No se puedo buscar :(")