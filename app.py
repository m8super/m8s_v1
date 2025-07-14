
import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="M8SUPER Login", layout="centered")

# CSS gaya login-form-08 (Colorlib inspired)
st.markdown("""
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(120deg, #2980b9, #8e44ad);
    height: 100vh;
    margin: 0;
}
[data-testid="stAppViewContainer"] > .main {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 10vh;
    background: transparent;
}
.login-box {
    background: #fff;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    width: 100%;
    max-width: 400px;
    text-align: center;
}
.login-box h2 {
    margin-bottom: 20px;
    color: #333;
}
.stTextInput > div > input {
    background-color: #f1f1f1;
    border: none;
    padding: 12px 15px;
    border-radius: 30px;
    width: 100%;
    margin-bottom: 20px;
}
.stButton > button {
    background-color: #2980b9;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 30px;
    font-weight: bold;
    cursor: pointer;
    transition: background 0.3s ease;
    width: 100%;
}
.stButton > button:hover {
    background-color: #3498db;
}
</style>
""", unsafe_allow_html=True)

# Logo + kotak login
st.markdown("""
<div style="text-align: center; margin-bottom: -20px;">
    <img src="https://raw.githubusercontent.com/m8super/m8s_v1/main/logo-m8s.png" width="80" 
         style="border-radius: 50%; background: transparent; padding: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);"/>
</div>
<div class="login-box">
    <h2>Welcome To M8SUPER</h2>
""", unsafe_allow_html=True)

# Input dan butang
username = st.text_input("👤 Nama Pengguna")
password = st.text_input("🔑 Kata Laluan", type="password")
st.button("Log Masuk")
