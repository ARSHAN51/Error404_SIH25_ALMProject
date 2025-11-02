# src/build_metadata.py
import csv
from pathlib import Path

proc = Path("data/processed")
combined = Path("data/combined")
rows = []
# processed speech
for w in proc.rglob("*.wav"):
    lang = "unknown"
    # infer language by folder name if present
    parts = w.parts
    for p in parts:
        if p.lower() in ["english","hindi","urdu","telugu","tamil","bangla","mandarin","bengali","bn-IN","bn-BD"]:
            lang = p
            break
    rows.append([str(w).replace("\\","/"), lang, "speech", "", ""])
# combined
for w in combined.rglob("*.wav"):
    rows.append([str(w).replace("\\","/"), "mixed", "combined", "", ""])
# write CSV
Path("data").mkdir(exist_ok=True)
with open("data/metadata_full.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["file_path","language","type","transcript","notes"])
    writer.writerows(rows)
print("Wrote data/metadata_full.csv with", len(rows), "rows")
