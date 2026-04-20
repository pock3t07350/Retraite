import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="MISSION CONTROL", layout="wide")
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
    font-size:55px;
    font-weight:bold;
    margin-bottom:10px;
}}

.sub {{
    text-align:center;
    font-size:22px;
    opacity:0.8;
}}

.grid {{
    display:flex;
    justify-content:space-around;
    margin-top:25px;
}}

.box {{
    text-align:center;
}}

.big {{
    font-size:60px;
    margin:0;
}}

.label {{
    font-size:18px;
    opacity:0.8;
}}

.bar {{
    width:100%;
    height:22px;
    background: rgba(0,0,0,0.4);
    border-radius:12px;
    border:1px solid rgba(0,255,136,0.4);
    position:relative;
    overflow:hidden;
    margin-top:25px;
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#1f8f5f);
}}

.plane {{
    position:absolute;
    top:-16px;
    font-size:24px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("<div class='title'>MISSION CONTROL</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>RETRAITE THOMAS</div>", unsafe_allow_html=True)

# =========================
# COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="grid">

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
# PROGRESSION (FIX PROPRE)
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# BARRE FIXE (SANS calc)
# =========================
st.markdown(f"""
<div>

<div style="display:flex; justify-content:space-between; margin-top:25px;">
    <span>📅 2008</span>
    <span>🎯 2026</span>
</div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div class="plane" style="left:{progress * 100}%;">
        ✈️
    </div>

</div>

<div style="text-align:center; font-size:30px; margin-top:10px;">
    {progress * 100:.8f} %
</div>

</div>
""", unsafe_allow_html=True)
