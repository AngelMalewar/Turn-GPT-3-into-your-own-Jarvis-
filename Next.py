import openai
import pyttsx3
import speech_recognition as sr

# Set your OpenAI API Key
openai.api_key = "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"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response.choices[0].text

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    # print("Listening...")

def main():
    while True:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                # Transcribe audio to text
                text = recognizer.recognize_google(audio)
                if text:
                    print(f"You said: '{text}'")

                    # Generate response using GPT-3
                    response = generate_response(text)
                    print(f"GPT-3 says: {response}")

                    # Read response using text-to-speech
                    speak_text(response)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError:
                print("You are not audible...")
                # print("Could not request results from Google Speech Recognition service")

if __name__ == "__main__":
    main()
