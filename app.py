import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="MISSION CONTROL - RETRAITE", layout="wide")
st_autorefresh(interval=1000, key="refresh")

# =========================
# TIMELINE
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
    color: #ffffff;
    font-family: monospace;
}}

/* TITRE SPACE X */
.title {{
    text-align:center;
    font-size:70px;
    font-weight:bold;
    letter-spacing:2px;
    color:white;
    text-shadow: 0 0 10px #00ff88;
}}

/* COMPTEUR */
.big {{
    font-size:110px;
    text-align:center;
    margin:0;
    color:#00ff88;
}}

.label {{
    text-align:center;
    font-size:22px;
    opacity:0.8;
}}

/* BARRE */
.bar {{
    width:100%;
    height:28px;
    background: rgba(0,0,0,0.5);
    border:1px solid rgba(0,255,136,0.5);
    border-radius:12px;
    position:relative;
    overflow:hidden;
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#1f8f5f);
}}

/* AVION SPACE */
.plane {{
    position:absolute;
    top:-20px;
    font-size:30px;
    transform:rotate(90deg);
    filter: drop-shadow(0 0 8px #00ff88);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("<div class='title'>🚀 MISSION CONTROL</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center;font-size:40px;color:#00ff88;'>RETRAITE THOMAS</div>", unsafe_allow_html=True)

# =========================
# COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="big">{days}</div>
<div class="label">DAYS UNTIL MISSION END</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<div class='big'>{hours}</div><div class='label'>HOURS</div>", unsafe_allow_html=True)
col2.markdown(f"<div class='big'>{minutes}</div><div class='label'>MINUTES</div>", unsafe_allow_html=True)
col3.markdown(f"<div class='big'>{seconds}</div><div class='label'>SECONDS</div>", unsafe_allow_html=True)

# =========================
# PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# SPACEX BAR + AVION
# =========================
st.markdown(f"""
<div style="margin-top:40px;">

<div style="display:flex; justify-content:space-between; font-size:18px;">
    <span>📅 DEC 2008</span>
    <span>🎯 MAY 2026</span>
</div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div class="plane" style="left:calc({progress * 100}% - 10px);">
        ✈️
    </div>

</div>

<div style="text-align:center; font-size:40px; margin-top:10px; color:#00ff88;">
    {progress * 100:.8f} %
</div>

</div>
""", unsafe_allow_html=True)
