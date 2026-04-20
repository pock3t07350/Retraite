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
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif = get_base64("logo.gif")

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
    margin-bottom:40px;
}}

.big {{
    font-size:120px;
    text-align:center;
    margin:0;
}}

.label {{
    font-size:28px;
    text-align:center;
    opacity:0.9;
}}

.row {{
    display:flex;
    justify-content:space-around;
    margin-top:30px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE UNIQUE
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
<div class="row">

    <div>
        <div class="big">{days}</div>
        <div class="label">JOURS</div>
    </div>

    <div>
        <div class="big">{hours}</div>
        <div class="label">HEURES</div>
    </div>

    <div>
        <div class="big">{minutes}</div>
        <div class="label">MINUTES</div>
    </div>

    <div>
        <div class="big">{seconds}</div>
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

st.progress(progress)

st.markdown(
    f"<div style='text-align:center;font-size:40px;margin-top:20px;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
