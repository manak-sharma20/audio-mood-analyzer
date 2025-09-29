# Audio Mood Analyzer 🎵😊

A Python-based tool to analyze the mood of an audio recording by extracting audio features and classifying emotional sentiment.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [How It Works](#how-it-works)  
- [Contributing](#contributing)  
- [License](#license)  
- [Acknowledgements](#acknowledgements)

---

## About

Audio Mood Analyzer is a Python application that records or loads an audio file, extracts acoustic and spectral features, and then predicts the mood or emotional state conveyed in the audio. It can be useful for musicians, content creators, or anyone interested in automatically annotating audio with mood tags.

---

## Features

- Records audio from microphone (via `recorder.py`)  
- Loads existing `.wav` audio files  
- Extracts features (e.g. spectral, pitch, MFCCs) using `features.py`  
- Performs mood / emotion classification in `mood_analysis.py`  
- Clean modular architecture  

---

## Getting Started

### Prerequisites

Make sure you have:

- Python 3.7 or newer  
- `pip` (Python package installer)  

You may also need packages like:

