import pyttsx3

def text_to_audio(text, rate=200, voice_type='female'):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties: speed and voice
        engine.setProperty('rate', rate)  # Speed of speech (default: 200 words per minute)
        
        # Get available voices
        voices = engine.getProperty('voices')
        print("1. Male\n2. Female")
        voice_type = input("Please choose the option from above: ")

        # Select voice based on user input (male or female)
        if voice_type == '2':
            engine.setProperty('voice', voices[1].id)  # Female voice
        elif voice_type == "1":
             engine.setProperty('voice', voices[0].id)
        else:
            print("The option you opted for is invalid")
             # Male voice

        # Convert text to speech and play it
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")

# Example usage
text = input("Please enter the text you want to listen: ")
text_to_audio(text, rate=150, voice_type='male')  # Change rate and voice type as needed
