import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def record_audio(duration=5, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
    sd.wait()  
    wav.write("recorded_audio.wav", sample_rate, audio_data)
    print("Recording saved as recorded_audio.wav")
