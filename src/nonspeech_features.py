import os
import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm

# Paths
DATA_DIR = "data/processed/nonspeech"       # where MUSAN was processed
FEATURES_PATH = "data/features/nonspeech_features.csv"

# Function to extract MFCC features
def extract_mfcc(file_path, n_mfcc=13):
    try:
        y, sr = librosa.load(file_path, sr=None)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        mfcc_mean = np.mean(mfcc, axis=1)
        return mfcc_mean
    except Exception as e:
        print(f"⚠️ Error processing {file_path}: {e}")
        return None

def main():
    features = []
    files = []

    # Recursively find all .wav files
    for root, _, filenames in os.walk(DATA_DIR):
        for f in filenames:
            if f.lower().endswith('.wav'):
                files.append(os.path.join(root, f))

    print(f"Extracting MFCC features from {len(files)} non-speech audio files...")

    for file in tqdm(files):
        mfcc = extract_mfcc(file)
        if mfcc is not None:   # skip failed files
            features.append({
                "filename": file.replace("\\", "/"),
                **{f"mfcc_{i+1}": val for i, val in enumerate(mfcc)},
                "label": "non_speech"
            })

    df = pd.DataFrame(features)
    os.makedirs(os.path.dirname(FEATURES_PATH), exist_ok=True)
    df.to_csv(FEATURES_PATH, index=False)
    print(f"✅ Non-speech features saved to {FEATURES_PATH}")
    print(f"Total processed files: {len(df)}")

if __name__ == "__main__":
    main()
