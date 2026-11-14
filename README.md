# 🔐 CipherVault – Basic Encryption & Decryption

A Python-based encryption and decryption application built using Streamlit and the Caesar Cipher algorithm.

CipherVault allows users to encrypt and decrypt text messages using a customizable shift key through a simple, interactive web interface.

## 🚀 Features

- **Text Encryption:** Encrypt messages using the Caesar Cipher algorithm.
- **Text Decryption:** Reverse the encryption process to recover the original message.
- **Custom Shift Key:** Choose a shift value between 0 and 25.
- **Interactive Interface:** Simple and user-friendly Streamlit interface.
- **Download Results:** Download encrypted or decrypted output as a text file.
- **Case Preservation:** Maintains uppercase and lowercase letters.
- **Character Preservation:** Spaces, numbers, and special characters remain unchanged.
- **One-Click Launcher:** Start the application using the included batch file.

## 🛠️ Technologies Used

- Python 3.11
- Streamlit
- Caesar Cipher Algorithm
- HTML/CSS (custom interface styling)

## 📂 Project Structure

```text
Encryption-Decryption/
│
├── app.py
├── requirements.txt
├── .gitignore
├── Start_Project.bat
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11 or later
- pip package manager

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Encryption-Decryption
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

**Option 1: Double-click**

Run `Start_Project.bat`.

**Option 2: Terminal**

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 🔍 How It Works

CipherVault uses the Caesar Cipher, a substitution encryption technique that shifts each alphabet character by a specified number of positions.

### Example

| Operation | Input | Shift Key | Output |
|---|---|---:|---|
| Encryption | HELLO | 3 | KHOOR |
| Decryption | KHOOR | 3 | HELLO |
| Encryption | DANISH | 5 | IFSNXM |

### Encryption Formula

```text
E(x) = (x + k) mod 26
```

### Decryption Formula

```text
D(x) = (x - k) mod 26
```

Where:
- `x` = Position of the alphabet character
- `k` = User-defined shift key
- `mod 26` = Keeps the result within the 26-letter alphabet

## 🧪 Testing

The application was tested with:

- Uppercase and lowercase text.
- Different shift key values.
- Encryption and decryption operations.
- Spaces and special characters.
- Empty input validation.
- Downloading processed results.

## ⚠️ Security Note

Caesar Cipher is a classical educational encryption technique. It is not suitable for protecting sensitive information in real-world applications because it can be easily broken.

This project demonstrates fundamental encryption concepts and reversible cryptographic logic.

## 🎯 Project Objective

To understand basic encryption and decryption techniques, implement cryptographic logic using Python, and demonstrate the fundamental concept of data confidentiality.

## 👨‍💻 Author

**Mohammad Danish**

Cybersecurity Enthusiast | Aspiring SOC Analyst

## 📜 License

This project is available for educational and learning purposes under the MIT License.
