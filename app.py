import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="RETRAITE THOMAS", layout="wide")
st_autorefresh(interval=1000, key="refresh")

# =========================
# DATES
# =========================
START = datetime(2008, 12, 1, 0, 0, 0)
TARGET = datetime(2026, 5, 29, 17, 0, 0)

now = datetime.now()
remaining = TARGET - now

# =========================
# GIF BACKGROUND
# =========================
def b64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif = b64("logo.gif")

st.markdown(f"""
<style>

.stApp {{
    background: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: #00ff88;
    font-family: monospace;
}}

.title {{
    text-align:center;
    font-size:70px;
    margin-bottom:30px;
}}

.box {{
    text-align:center;
}}

.big {{
    font-size:90px;
    margin:0;
}}

.label {{
    font-size:22px;
    opacity:0.9;
}}

.bar-container {{
    width:100%;
    margin-top:40px;
}}

.bar {{
    position:relative;
    height:25px;
    background: rgba(0,0,0,0.35);
    border-radius:12px;
    border:1px solid rgba(0,255,136,0.4);
    overflow:hidden;
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#0a7a2f);
}}

.plane {{
    position:absolute;
    top:-18px;
    font-size:28px;
    transform:rotate(90deg);
    filter: drop-shadow(0px 0px 6px #00ff88);
}}

.row {{
    display:flex;
    justify-content:space-around;
    margin-top:20px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("<div class='title'>RETRAITE THOMAS</div>", unsafe_allow_html=True)

# =========================
# COMPTEUR ALIGNÉ PROPRE
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="row">

    <div class="box">
        <div class="big">{days}</div>
        <div class="label">JOURS</div>
    </div>

    <div class="box">
        <div class="big">{hours}</div>
        <div class="label">HEURES</div>
    </div>

    <div class="box">
        <div class="big">{minutes}</div>
        <div class="label">MINUTES</div>
    </div>

    <div class="box">
        <div class="big">{seconds}</div>
        <div class="label">SECONDES</div>
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# PROGRESSION (CORRIGÉE)
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = elapsed / total
progress = max(0.0, min(1.0, progress))

# =========================
# BARRE FIABLE + AVION
# =========================
st.markdown(f"""
<div class="bar-container">

    <div style="display:flex; justify-content:space-between;">
        <span>📅 Déc 2008</span>
        <span>🎯 29 Mai 2026</span>
    </div>

    <div class="bar">

        <div class="fill" style="width:{progress * 100}%;"></div>

        <div class="plane" style="left:{progress * 100}%;">
            ✈️
        </div>

    </div>

    <div style="text-align:center; font-size:40px; margin-top:10px;">
        {progress * 100:.8f} %
    </div>

</div>
""", unsafe_allow_html=True)
