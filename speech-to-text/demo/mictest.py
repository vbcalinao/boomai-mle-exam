import speech_recognition as sr
import pyaudio
import wave

# Create a recognizer instance
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Testing microphone... Please say something.")
    audio = r.record(source, duration=5)  # Record for 5 seconds

# Save the audio to a .wav file
with open("test.wav", "wb") as file:
    file.write(audio.get_wav_data())

print("Playing back the recorded audio...")

# Define stream chunk
chunk = 1024

# Open a wav format music
f = wave.open("test.wav", "rb")
# Instantiate PyAudio
p = pyaudio.PyAudio()
# Open stream
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)
# Read data
data = f.readframes(chunk)

# Play stream
while data:
    stream.write(data)
    data = f.readframes(chunk)

# Stop stream
stream.stop_stream()
stream.close()

# Close PyAudio
p.terminate()

print("If you heard the audio, the microphone is working.")