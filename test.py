import speech_recognition as sr

def main():
    # Crea una instancia del reconocedor de voz
    recognizer = sr.Recognizer()

    # Usa el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental. Por favor, espera...")
        recognizer.adjust_for_ambient_noise(source, duration=5)  # Ajusta el ruido ambiental
        print("Listo. Por favor, di algo...")

        try:
            # Escucha el audio del micrófono
            audio = recognizer.listen(source)
           
            # Convierte el audio a texto usando el servicio de Google
            text = recognizer.recognize_google(audio, language='es-ES')
            print(f"Has dicho: {text}")

        except sr.UnknownValueError:
            print("Lo siento, no pude entender lo que dijiste.")
        except sr.RequestError as e:
            print(f"Hubo un error con el servicio de Google Speech Recognition; {e}")

if __name__ == "__main__":
    main()