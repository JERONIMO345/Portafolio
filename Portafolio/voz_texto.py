from gtts import gTTS

idiomas = "en"

texto = input(str("Escribe lo que quieres escuchar:"))

audio = gTTS(text= texto, lang= idiomas, slow= False)

audio.save("Prueba4.mp3")

print("¡Listo!")