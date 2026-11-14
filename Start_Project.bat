
@echo off
title CipherVault - Encryption and Decryption

echo ==========================================
echo       CIPHERVAULT - CYBER SECURITY
echo          Encryption and Decryption
echo ==========================================
echo.

cd /d "%~dp0"

echo Starting CipherVault...
echo.

python -m streamlit run app.py

pause
