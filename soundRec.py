import sounddevice as sd
import wavio

# Set the recording duration (in seconds)
duration = 10

# Record audio from the default input device
print("Recording started...")
audio = sd.rec(int(duration * 44100), samplerate=44100, channels=2)

# Wait for the recording to complete
sd.wait()
print("Recording ended.")

# Save the recorded audio to a WAV file
wavio.write("recording.wav", audio, 44100, sampwidth=2)
print("Audio saved as 'recording.wav'")