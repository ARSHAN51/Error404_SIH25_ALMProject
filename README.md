# Error404_SIH25_ALMProject
Deep Learning-based Audio Language Model that listens, thinks &amp; understands both speech and non-speech sounds

# === ALM Project Auto Setup ===
# Run this inside your project folder (e.g., Error404_SIH25_ALMProject)

# Create main folders
"data","src","app","reports","notebooks","logs" | ForEach-Object { mkdir $_ -Force }

# === Create subfolders ===
# Data subfolders
"speech","nonspeech","combined" | ForEach-Object { mkdir "data\$_" -Force }

# === Create placeholder files ===
New-Item -Path "src\preprocessing.py" -ItemType File -Force
New-Item -Path "src\speech_features.py" -ItemType File -Force
New-Item -Path "src\nonspeech_features.py" -ItemType File -Force
New-Item -Path "src\model.py" -ItemType File -Force
New-Item -Path "src\train.py" -ItemType File -Force
New-Item -Path "src\evaluate.py" -ItemType File -Force
New-Item -Path "src\inference.py" -ItemType File -Force
New-Item -Path "app\demo_app.py" -ItemType File -Force
New-Item -Path "reports\literature_review.docx" -ItemType File -Force
New-Item -Path "reports\datasets_summary.csv" -ItemType File -Force
New-Item -Path "reports\model_results.xlsx" -ItemType File -Force

# === Create README.md ===
$readme = @"
# 🎧 Deep Learning-based Audio Language Model (ALM)
### SIH Problem ID: 25242  
> **Title:** Deep learning based ALM (Audio Language Model), which Listen, Think, and Understand the speech and non-speech Together.

---

## 🧠 Overview
Humans live in a multifarious environment of audio signals that include speech and non-speech sounds.  
The ability to accurately discern, interpret, and integrate these elements — and understand their relationship — forms a key aspect of human cognition.

This project aims to develop an **Audio-Language Model (ALM)** that can:
- Listen to both **speech and non-speech audio**
- Think and interpret meaning from combined signals
- Understand and respond appropriately

---

## 📂 Project Structure
| Folder | Description |
|--------|--------------|
| /data | Dataset and audio samples |
| /src | Source code (model, preprocessing, training scripts) |
| /app | Application interface / deployment |
| /reports | Documentation, analysis, and outputs |
| /notebooks | Jupyter experiments |
| /logs | Training logs and checkpoints |

---

## 👨‍💻 Team – Error404 (SIH 2025)
| Role | Name | Email | Contact | Gender |
|------|------|--------|----------|--------|
| **Team Leader** | Shaikh Mohammad Arshan | [sarshan51@gmail.com](mailto:sarshan51@gmail.com) | 8446060277 | Male |
| **Member** | Yaser Saleem | [yasersaleem404@gmail.com](mailto:yasersaleem404@gmail.com) | 8767928989 | Male |
| **Member** | Anjali Waghmare | [anjalijnec28@gmail.com](mailto:anjalijnec28@gmail.com) | 8237586328 | Female |
| **Member** | Siddiqui Faiz Ahmed | [faizahmed3578@gmail.com](mailto:faizahmed3578@gmail.com) | 7249788564 | Male |
| **Member** | Fahad Qureshi | [fahadq749@gmail.com](mailto:fahadq749@gmail.com) | 9619031788 | Male |
| **Member** | Taleya Sayed | [taleyajnec@gmail.com](mailto:taleyajnec@gmail.com) | 9172460928 | Female |

---

## 🧩 Tech Stack
- Python (TensorFlow / PyTorch)
- Librosa, NumPy, Pandas
- Flask / FastAPI (for app)
- GitHub & Google Colab for collaboration

---

## 🚀 Setup Instructions
\`\`\`bash
git clone https://github.com/<your-username>/Error404_SIH25_ALMProject.git
cd Error404_SIH25_ALMProject
pip install -r requirements.txt
\`\`\`

---

## 📜 License
This project is part of **Smart India Hackathon (SIH) 2025**  
All rights reserved © Team Error404
"@
$readme | Out-File -FilePath "README.md" -Encoding utf8 -Force

# === Create .gitignore ===
$gitignore = @"
# Python cache
__pycache__/
*.pyc

# Virtual environment
venv/
.env/

# Data
data/*
!data/README.md

# Logs
logs/*
!logs/README.md

# Notebooks
notebooks/*.ipynb_checkpoints/

# Reports
reports/*.tmp

# System files
.DS_Store
Thumbs.db
"@
$gitignore | Out-File -FilePath ".gitignore" -Encoding utf8 -Force

# === Create requirements.txt ===
$requirements = @"
numpy
pandas
librosa
torch
torchvision
torchaudio
scikit-learn
matplotlib
seaborn
flask
"@
$requirements | Out-File -FilePath "requirements.txt" -Encoding utf8 -Force

Write-Host "`n✅ ALM Project structure created successfully!"
