import pywhatkit

print("Bienvenido")

print("Escribe el tema que quieres investigar")
tema = str(input())

print("En cuentas lineas quieres la invetigacion?:")

lineas = int(input())

pywhatkit.info(tema, lines = lineas)

"Nota: tiene error con las palabras (xbox, google, auronplay), pronto se solucionara"