
import streamlit as st
import json
import os

# ---------- Config ----------
st.set_page_config(page_title="M8SUPER Login", layout="centered")
USER_DB_FILE = "users.json"

# ---------- Inisialisasi User Database ----------
def load_users():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=2)

users = load_users()

# ---------- CSS UI ----------
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

# ---------- Logo ----------
st.markdown("""
<div style="text-align: center; margin-bottom: -20px;">
    <img src="https://raw.githubusercontent.com/m8super/m8s_v1/main/logo-m8s.png" width="80" 
         style="border-radius: 50%; background: white; padding: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.2);"/>
</div>
""", unsafe_allow_html=True)

# ---------- Sesi Login ----------
if "login_user" not in st.session_state:
    st.session_state.login_user = None

# ---------- Sistem Login & Daftar ----------
if st.session_state.login_user:
    # DASHBOARD
    st.markdown(f"""
    <div class="login-box">
        <h2>Selamat datang, <span style='color:#2980b9'>{st.session_state.login_user}</span>!</h2>
        <p>Ini adalah dashboard utama M8SUPER.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Log Keluar"):
        st.session_state.login_user = None
        st.experimental_rerun()

else:
    menu = st.radio("Pilih Menu:", ["Log Masuk", "Daftar"], horizontal=True)

    if menu == "Log Masuk":
        username = st.text_input("👤 Nama Pengguna")
        password = st.text_input("🔑 Kata Laluan", type="password")
        if st.button("Log Masuk"):
            if username in users and users[username] == password:
                st.session_state.login_user = username
                st.experimental_rerun()
            else:
                st.error("Nama pengguna atau kata laluan salah.")

    elif menu == "Daftar":
        new_user = st.text_input("👤 Nama Pengguna Baharu")
        new_pass = st.text_input("🔑 Kata Laluan Baharu", type="password")
        if st.button("Daftar Akaun"):
            if new_user in users:
                st.warning("Nama pengguna sudah wujud.")
            elif new_user == "" or new_pass == "":
                st.warning("Sila isi semua maklumat.")
            else:
                users[new_user] = new_pass
                save_users(users)
                st.success("Akaun berjaya didaftarkan! Sila log masuk.")
