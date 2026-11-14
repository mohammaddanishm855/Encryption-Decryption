
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CipherVault | Encryption Tool",
    page_icon="🔐",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #07111f, #101d32);
    color: #ffffff;
}
h1, h2, h3, p, label {
    color: #ffffff !important;
}
.subtitle {
    color: #9eb4cc;
    text-align: center;
    font-size: 16px;
}
.result-box {
    background-color: #14243a;
    border: 1px solid #00c8ff;
    border-radius: 10px;
    padding: 18px;
}
div.stButton > button {
    background-color: #00a6d6;
    color: white;
    border-radius: 8px;
    border: none;
    width: 100%;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #007fa8;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Caesar Cipher logic
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += char

    return result


# Header
st.markdown("<h1 style='text-align:center;'>🔐 CipherVault</h1>",
            unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Basic Encryption & Decryption Using Caesar Cipher</p>",
    unsafe_allow_html=True
)

st.divider()

st.subheader("🛡️ Encryption Console")

mode = st.radio(
    "Select Operation",
    ["Encrypt", "Decrypt"],
    horizontal=True
)

user_text = st.text_area(
    "Enter your message",
    placeholder="Type your message here...",
    height=150
)

shift = st.number_input(
    "Enter Shift Key (0–25)",
    min_value=0,
    max_value=25,
    value=3,
    step=1
)

if st.button("🔒 Process Message"):

    if not user_text.strip():
        st.warning("Please enter a message before processing.")

    else:
        if mode == "Encrypt":
            output = caesar_cipher(user_text, shift)
            heading = "🔒 Encrypted Message"
        else:
            output = caesar_cipher(user_text, -shift)
            heading = "🔓 Decrypted Message"

        st.divider()
        st.subheader(heading)

        st.code(output, language=None)

        st.download_button(
            label="📥 Download Result",
            data=output,
            file_name="cipher_result.txt",
            mime="text/plain"
        )

        st.success(f"{mode}ion completed successfully!")

st.divider()

st.markdown("### 📘 How Caesar Cipher Works")

st.write(
    "Caesar Cipher is a substitution encryption technique "
    "that shifts each alphabet character by a fixed number "
    "of positions in the alphabet."
)

st.info(
    "Example: With shift key 3, HELLO becomes KHOOR. "
    "Decryption reverses the same shift."
)

st.caption(
    "CipherVault | Cyber Security Project 2 | DecodeLabs"
)
