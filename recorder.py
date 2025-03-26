import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
from mood_analysis import analyze_mood  # Import the analyze_mood function

def record_audio(filename="recorded_audio.wav", duration=5, sample_rate=44100):
    try:
        print("Recording...", flush=True)
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
        sd.wait()
        wav.write(filename, sample_rate, audio_data)
        print("Recording saved as", filename, flush=True)

        # Analyze the audio data to extract pitch, tempo, and energy
        pitch = np.mean(np.abs(audio_data)) * 1000  # Placeholder for pitch extraction
        tempo = 120  # Placeholder for tempo extraction
        energy = np.sum(audio_data ** 2) / len(audio_data)  # Calculate energy

        # Determine the mood
        mood = analyze_mood(pitch, tempo, energy)
        print("Detected Mood:", mood, flush=True)

    except Exception as e:
        print("Error occurred during recording:", str(e))

# Call the function to record audio
record_audio()
