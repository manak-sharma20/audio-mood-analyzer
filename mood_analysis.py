def analyze_mood(pitch, tempo, energy):
    if pitch > 200 and tempo > 120 and energy > 0.05:
        return "Happy / Excited 😀"
    elif pitch < 150 and tempo < 90 and energy < 0.02:
        return "Sad / Low Energy 😔"
    elif tempo > 100 and energy > 0.03:
        return "Neutral / Normal Mood 🙂"
    else:
        return "Calm / Relaxed 😌"