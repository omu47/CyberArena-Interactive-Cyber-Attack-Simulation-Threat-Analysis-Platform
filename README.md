# 🛡️ CyberArena
### Interactive Cyber Attack Simulation & Threat Analysis Platform

CyberArena is a modern cybersecurity learning and simulation platform built using Flask, Python, SQLite, and multiple security-focused modules.

The platform provides interactive labs, phishing simulations, AI-powered threat analysis, steganography detection, encryption demos, gamification, and a cyber-themed dashboard experience.
<img width="866" height="427" alt="Animation12345 (1)" src="https://github.com/user-attachments/assets/45f0d7ea-3b9b-45f7-9ba1-5ab70b622b37" />

---

# 🚀 Features

## 🔐 Authentication System
- User Registration
- Secure Login System
- Password Hashing
- Session Management using Flask-Login

---

## 🧠 AI Threat Analyzer
Analyze suspicious emails, messages, or SMS content using custom threat intelligence logic.

### Detects:
- Phishing keywords
- Credential harvesting attempts
- Urgency manipulation
- Social engineering patterns
- Suspicious links and payload indicators

### Generates:
- Threat score
- Risk level
- Threat reports
<img width="679" height="359" alt="{1649002F-F099-450F-9F93-6658B9DE644E}" src="https://github.com/user-attachments/assets/3a6697ab-4112-4893-b4ca-dcbd5411b882" />

---

## 🧬 Steganography Detection Lab
Upload images and inspect them for hidden data.

### Includes:
- Hidden message extraction
- Image metadata analysis
- LSB steganography detection

---

## 🔑 RSA Encryption Simulator
Educational RSA encryption demonstration.

### Shows:
- Encryption process
- Weak RSA vulnerabilities
- Small exponent attack explanation

---

## 🧪 Base64 Decoder Lab
Decode suspicious Base64 encoded payloads commonly used in malware and phishing attacks.

---

## 🎭 Phishing Simulation
A realistic phishing attack simulator that demonstrates how attackers steal:
- Credentials
- OTPs
- User trust

Used for cybersecurity awareness training.

---

## 🌍 Global Threat Map
Interactive cyber threat visualization map using Leaflet.js.

---

## 🏆 Gamification System
Users earn:
- XP points
- Security ranks
- Leaderboard positions

Ranks upgrade automatically based on activity.

---

## 🎨 Cyberpunk UI
Modern responsive interface with:
- Matrix animation background
- Neon cyber theme
- Responsive mobile layout
- Animated buttons and cards

---

# 🛠️ Technologies Used

## Backend
- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite

## Frontend
- HTML5
- CSS3
- JavaScript

## Security / Cyber Modules
- Stegano
- RSA Demonstration
- Threat Intelligence Logic
- Base64 Analysis

## Deployment
- Docker
  <img width="700" height="268" alt="{BE7AA45D-335B-4B04-9EF9-C64639BE95FC}" src="https://github.com/user-attachments/assets/0df60d10-f6cc-4d4e-af8c-37b4d3f99bb5" />

- Render
  <img width="678" height="315" alt="{A1D04339-5D48-4E4C-B370-87AD3299DF65}" src="https://github.com/user-attachments/assets/1c5e48b9-60b9-4c3b-917d-9138dbb3609b" />
<img width="643" height="257" alt="image" src="https://github.com/user-attachments/assets/facab59d-ab3f-4982-babe-aa9649cdb44b" />

- GitHub


---

# 📂 Project Structure

```bash
CyberArena/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── render.yaml
│
├── modules/
│   ├── base64_lab.py
│   ├── rsa_demo.py
│   ├── steg_detector.py
│   ├── threat_analyzer.py
│   └── report_generator.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── phishing.html
│   ├── rsa_lab.html
│   ├── ai_analyzer.html
│   ├── steganography.html
│   └── leaderboard.html
│
└── instance/
    └── cyberarena.db
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/CyberArena.git

cd CyberArena
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate

#### Windows
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

Application runs on:

```bash
http://127.0.0.1:5000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t cyberarena .
```

## Run Container

```bash
docker run -p 5000:5000 cyberarena
```

---

# ☁️ Deploy on Render

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
gunicorn app:app
```

---

# 🔒 Security Features

- Password hashing
- Session protection
- Secure file upload handling
- Threat intelligence analysis
- Steganography inspection
- Cyber attack simulation

---

# 📸 Screenshots

## Dashboard
- Live threat feed
- Threat activity panel
- Cyberpunk interface

## Threat Analyzer
- AI-based risk scoring
- Threat indicator detection

## Steganography Lab
- Hidden message extraction
- Metadata inspection

---

# 📈 Future Improvements

- Real AI/LLM integration
- Live network packet monitoring
- Malware sandbox
- JWT authentication
- PostgreSQL database
- Real-time WebSocket alerts
- Kubernetes deployment
- Kafka-based event streaming
- SOC dashboard analytics

---

# 👨‍💻 Author

## Uma Shankar

Crafted with ❤️ for cybersecurity education, awareness, and interactive learning.

---

# 📜 License

This project is for educational and ethical cybersecurity learning purposes only.

Use responsibly.
