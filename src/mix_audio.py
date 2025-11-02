mix_audio# src/mix_audio.py
import random
from pathlib import Path
import librosa, soundfile as sf
SR = 16000
PROC_SPEECH = Path("data/processed")
OUT_DIR = Path("data/combined")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def mix_two(speech, noise, snr_db=5):
    s, _ = librosa.load(speech, sr=SR)
    n, _ = librosa.load(noise, sr=SR)
    min_len = min(len(s), len(n))
    s = s[:min_len]; n = n[:min_len]
    eps = 1e-9
    rms_s = (s**2).mean()**0.5 + eps
    rms_n = (n**2).mean()**0.5 + eps
    target_rms_n = rms_s / (10**(snr_db/20))
    n_scaled = n * (target_rms_n / rms_n)
    mixed = s + n_scaled
    mixed = mixed / max(abs(mixed))
    return mixed

def build_demo(num=10):
    speech_files = list(PROC_SPEECH.rglob("*speech*.wav")) + list(PROC_SPEECH.rglob("**/*.wav"))
    noise_files = list(PROC_SPEECH.rglob("*noise*.wav")) + list(PROC_SPEECH.rglob("**/*noise*.wav"))
    # if no explicit names, just pick two different files
    if not speech_files or not noise_files:
        # attempt to separate by folders: speech vs nonspeech
        speech_files = list(Path("data/processed/speech").glob("*.wav"))
        noise_files = list(Path("data/processed/nonspeech").glob("*.wav"))
    idx = 0
    for i in range(min(num, len(speech_files))):
        s = random.choice(speech_files)
        n = random.choice(noise_files) if noise_files else s  # if no noise, duplicate speech
        mixed = mix_two(s, n, snr_db=random.choice([0,5,10]))
        out = OUT_DIR / f"mix_demo_{idx:03d}.wav"
        sf.write(out, mixed, SR)
        idx += 1
    print("Created", idx, "demo mixes in", OUT_DIR)

if __name__ == "__main__":
    build_demo(10)
