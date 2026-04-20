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
    color:#00ff88;
}}

.grid {{
    display:flex;
    justify-content:space-around;
    margin-top:30px;
}}

.block {{
    text-align:center;
}}

.number {{
    font-size:120px;
    margin:0;
}}

.label {{
    font-size:25px;
    opacity:0.8;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("<div class='title'>RETRAITE THOMAS</div>", unsafe_allow_html=True)

# =========================
# COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="grid">

    <div class="block">
        <div class="number">{days}</div>
        <div class="label">JOURS</div>
    </div>

    <div class="block">
        <div class="number">{hours}</div>
        <div class="label">HEURES</div>
    </div>

    <div class="block">
        <div class="number">{minutes}</div>
        <div class="label">MINUTES</div>
    </div>

    <div class="block">
        <div class="number">{seconds}</div>
        <div class="label">SECONDES</div>
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# barre native Streamlit (ULTRA STABLE)
st.progress(progress)

st.markdown(
    f"<div style='text-align:center;font-size:40px;margin-top:10px;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
