import librosa
import numpy as np

def extract_audio_features(filename="recorded_audio.wav"):
    y, sr = librosa.load(filename)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch = np.mean(pitches[magnitudes > np.median(magnitudes)]) if np.any(magnitudes) else 0
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    energy = np.sum(y ** 2) / len(y)
    return pitch, tempo, energy
