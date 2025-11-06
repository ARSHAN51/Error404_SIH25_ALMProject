import os
import librosa
import numpy as np
import pandas as pd
from tqdm import tqdm

# Paths (adjust if needed)
DATA_DIR = "data/processed"
FEATURES_PATH = "data/features/speech_features.csv"

# Function to extract MFCC features
def extract_mfcc(file_path, n_mfcc=13):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean

def main():
    features = []
    files = []
    for root, _, filenames in os.walk(DATA_DIR):
      for f in filenames:
        if f.endswith('.wav'):
            files.append(os.path.join(root, f))


    print(f"Extracting MFCC features from {len(files)} audio files...")
    for file in tqdm(files):
        # path = os.path.join(DATA_DIR, file)
        path = file
        mfcc = extract_mfcc(path)
        features.append({
            "filename": file,
            **{f"mfcc_{i+1}": val for i, val in enumerate(mfcc)}
        })

    df = pd.DataFrame(features)
    os.makedirs(os.path.dirname(FEATURES_PATH), exist_ok=True)
    df.to_csv(FEATURES_PATH, index=False)
    print(f"✅ Features saved to {FEATURES_PATH}")

if __name__ == "__main__":
    main()
