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
}}

html, body {{
    font-family: monospace;
    color: #00ff88;
}}

.big {{
    font-size:90px;
    text-align:center;
    margin:0;
}}

.label {{
    font-size:22px;
    text-align:center;
    opacity:0.9;
}}

.bar {{
    width:100%;
    height:25px;
    background: rgba(0,0,0,0.35);
    border-radius:12px;
    border:1px solid rgba(0,255,136,0.4);
    position:relative;
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

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("<h1 style='text-align:center;'>RETRAITE THOMAS</h1>", unsafe_allow_html=True)

# =========================
# COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="big">{days}</div>
<div class="label">JOURS</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='big'>{hours}</div><div class='label'>HEURES</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='big'>{minutes}</div><div class='label'>MINUTES</div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='big'>{seconds}</div><div class='label'>SECONDES</div>", unsafe_allow_html=True)

# =========================
# PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# BARRE + AVION
# =========================
st.markdown(f"""
<div style="margin-top:40px;">

<div style="display:flex; justify-content:space-between;">
    <span>📅 Déc 2008</span>
    <span>🎯 29 Mai 2026</span>
</div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div class="plane" style="left:calc({progress * 100}% - 10px);">
        ✈️
    </div>

</div>

<div style="text-align:center; font-size:40px; margin-top:10px;">
    {progress * 100:.8f} %
</div>

</div>
""", unsafe_allow_html=True)
