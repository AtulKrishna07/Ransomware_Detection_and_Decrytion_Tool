# Ransomware Detection and Decryption Tool 🔐

A GUI-based Python tool to scan files or folders for ransomware-like encrypted files, using entropy analysis and XOR decryption.

## 🔧 Features
- Scan folders or individual files
- Detect high-entropy (suspicious) files
- Automatically attempts XOR decryption
- Simple and user-friendly Tkinter GUI

## 📂 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ransomware-tool.git
   cd ransomware-tool
   
2. python main.py

3. Use the GUI to
 - Select files or folders
 - View suspicious files with high entropy
 - Attempt basic XOR decryption

 4. Use the included script to generate a test encrypted file:
    python create_sample_encrypted.py
