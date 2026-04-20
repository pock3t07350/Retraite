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
# GIF BACKGROUND (SAFE)
# =========================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif = get_base64("logo.gif")

st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

.title {{
    text-align:center;
    font-size:80px;
    color:#00ff88;
    margin-bottom:30px;
    font-weight:bold;
}}

.grid {{
    display:flex;
    justify-content:space-around;
    text-align:center;
    margin-top:20px;
    color:#00ff88;
}}

.number {{
    font-size:140px;
    margin:0;
}}

.label {{
    font-size:35px;
    opacity:0.8;
}}

.bar {{
    width:100%;
    height:25px;
    background:rgba(0,0,0,0.4);
    border-radius:10px;
    margin-top:30px;
    position:relative;
    overflow:hidden;
}}

.fill {{
    height:100%;
    background:linear-gradient(90deg,#00ff88,#1f8f5f);
}}

.plane {{
    position:absolute;
    top:-15px;
    font-size:25px;
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

    <div>
        <div class="number">{days}</div>
        <div class="label">JOURS</div>
    </div>

    <div>
        <div class="number">{hours}</div>
        <div class="label">HEURES</div>
    </div>

    <div>
        <div class="number">{minutes}</div>
        <div class="label">MINUTES</div>
    </div>

    <div>
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

# =========================
# BARRE FIABLE
# =========================
st.markdown(f"""
<div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div class="plane" style="left:{progress * 100}%;">
        ✈️
    </div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================
# POURCENTAGE
# =========================
st.markdown(
    f"<div style='text-align:center;font-size:50px;color:#00ff88;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
