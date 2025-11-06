import pandas as pd
import os

# File paths
SPEECH_FEATURES = "data/features/speech_features.csv"
NONSPEECH_FEATURES = "data/features/nonspeech_features.csv"
MERGED_PATH = "data/features/combined_features.csv"

def main():
    # Load both datasets
    print("🔹 Loading speech and non-speech feature files...")
    df_speech = pd.read_csv(SPEECH_FEATURES)
    df_nonspeech = pd.read_csv(NONSPEECH_FEATURES)

    # Add labels if missing
    if 'label' not in df_speech.columns:
        df_speech['label'] = 'speech'
    if 'label' not in df_nonspeech.columns:
        df_nonspeech['label'] = 'non_speech'

    # Merge them
    combined = pd.concat([df_speech, df_nonspeech], ignore_index=True)

    # Shuffle the dataset
    combined = combined.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save merged file
    os.makedirs(os.path.dirname(MERGED_PATH), exist_ok=True)
    combined.to_csv(MERGED_PATH, index=False)

    print(f"✅ Combined dataset saved to {MERGED_PATH}")
    print(f"Total samples: {len(combined)}")
    print(f"Speech: {len(df_speech)}, Non-speech: {len(df_nonspeech)}")

if __name__ == "__main__":
    main()
