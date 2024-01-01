import assemblyai as aai
import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")
    audio = r.record(source, duration=5)  # Listen for the first phrase and extract it into audio data
print("Recording stopped.")

# Save the audio to a .wav file
with open("recording.wav", "wb") as file:
    file.write(audio.get_wav_data())

# Initialize AssemblyAI client
aai.settings.api_key = "de93505212d1443595a4537ba2210237"

# Create a TranscriptionConfig object
config = aai.TranscriptionConfig(speaker_labels=True)

# Transcribe the audio file using AssemblyAI
FILE_URL = 'recording.wav'

transcriber = aai.Transcriber()

print("Transcription is processing...")
transcript = transcriber.transcribe(FILE_URL)

print("Transcript: ", transcript.text)

# Split the transcript into words
words = transcript.text.split()

# Define a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# Append "-v" to words that end with a vowel and "-c" to words that end with a consonant
modified_words = [word + '-v' if word[-1] in vowels else word + '-c' for word in words]

# Join the modified words back into a transcript
modified_transcript = ' '.join(modified_words)

print("Modified transcript (-v and -c): ", modified_transcript)