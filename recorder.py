import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np

def record_audio(filename="recorded_audio.wav", duration=5, sample_rate=44100):
    try:
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
        sd.wait()
        wav.write(filename, sample_rate, audio_data)
        print("Recording saved as", filename)
    except Exception as e:
        print("Error occurred during recording:", str(e))

# Call the function to record audio
record_audio()
