# 🔐 StegoVault – Secure File Steganography using Hybrid Encryption

StegoVault is a Python-based cybersecurity project that securely encrypts files and hides them inside PNG images using Least Significant Bit (LSB) steganography. The project combines RSA and AES (Fernet) encryption to ensure confidentiality before embedding the encrypted data into an image.

## 🚀 Features

- Hybrid Encryption (RSA + AES/Fernet)
- LSB-based PNG image steganography
- Supports embedding any file type (PDF, TXT, EXE, DOCX, etc.)
- Secure extraction and recovery of original files
- Command-Line Interface (CLI)
- Modular Python architecture

## 🛠️ Technologies Used

- Python 3
- Cryptography
- Pillow
- RSA
- AES (Fernet)
- LSB Steganography

## 📂 Project Structure

```
StegoVault/
│── main.py
│── encrypt.py
│── decrypt.py
│── hybrid_encrypt.py
│── hybrid_decrypt.py
│── image_encoder.py
│── image_decoder.py
│── binary_utils.py
│── file_utils.py
│── requirements.txt
│── README.md
```

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/StegoVault.git
cd StegoVault
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python main.py
```

Follow the on-screen menu to:

- Encrypt a file
- Hide it inside a PNG image
- Extract the hidden data
- Recover the original file

## 🔒 Security Workflow

```
Input File
      │
      ▼
AES (Fernet) Encryption
      │
      ▼
RSA Encrypts AES Key
      │
      ▼
Embed into PNG (LSB)
      │
      ▼
Stego Image
```

## 👨‍💻 Author

**Adnan Neelamji**

Computer Science Graduate | Aspiring SOC Analyst | Cybersecurity Enthusiast
