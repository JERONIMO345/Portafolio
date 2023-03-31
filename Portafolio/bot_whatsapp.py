import pywhatkit

print("introduce numero de celular:")

numero = input()

print("Escribe tu mensaje:")

mensaje = input()

print("Introduce la hora que quieres que te envien el mensaje:")

hora = int(input())

print("Introduce el minuto que quieres que te envien el mensaje:")

minuto = int(input())

print(type(hora))
print(type(minuto))

pywhatkit.sendwhatmsg(numero,mensaje,hora,minuto)