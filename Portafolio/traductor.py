from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source="en",target="es")

print("Copia y pega el texto que quieres traducir:")

texto = input(str())

print("traduciendo...")
print("¡Listo!")

resultado = traductor.translate(texto)

print(resultado)