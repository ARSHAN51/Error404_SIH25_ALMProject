# src/data_checks.py
from pathlib import Path
import soundfile as sf

p = Path("data/processed")
wav_files = list(p.rglob("*.wav"))
print("Processed WAV count:", len(wav_files))
for w in wav_files[:10]:
    info = sf.info(w)
    print(w, info.samplerate, info.channels)
