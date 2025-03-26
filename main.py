from recorder import record_audio
from features import extract_audio_features
from mood_analysis import analyze_mood

def main():
    record_audio(duration=5)
    pitch, tempo, energy = extract_audio_features()
    mood = analyze_mood(pitch, tempo, energy)
    print(f"Pitch: {pitch:.2f}, Tempo: {tempo:.2f}, Energy: {energy:.5f}")
    print(f"Detected Mood: {mood}")

if __name__ == "__main__":
    main()