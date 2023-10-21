import speech_recognition as sr
import subprocess

def main():
    # Inicializar el reconocedor de voz
    recognizer = sr.Recognizer()
   
    # Capturar audio del micrófono
    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental. Por favor, espera...")
        recognizer.adjust_for_ambient_noise(source, duration=5)  # Ajusta el ruido ambiental
        print("Esperando comando: ")
        audio = recognizer.listen(source)
   
    try:
        # Convertir el audio a texto
        command = recognizer.recognize_google(audio, language='es-ES').lower()
        print(f"Comando reconocido: {command}")
       
        # Verificar si el comando es "abrir internet"
        if "abrir internet" in command:
            print("Abriendo Google Chrome...")
            # Ejecutar Google Chrome
            subprocess.run(["google-chrome"])
        else:
            print("Comando no reconocido.")
   
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio.")
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados a Google Speech Recognition; {e}")

if __name__ == "__main__":
    main()