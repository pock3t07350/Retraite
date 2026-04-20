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

# =========================
# STYLE GLOBAL
# =========================
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
    color: #00ff88;
    font-family: monospace;
}}

/* GROS HUD */
.big {{
    font-size:120px;
    text-align:center;
    margin:0;
}}

.label {{
    font-size:28px;
    text-align:center;
}}

/* BARRE */
.bar {{
    width:100%;
    height:30px;
    background: rgba(0,0,0,0.4);
    border:1px solid rgba(0,255,136,0.5);
    border-radius:12px;
    position:relative;
    overflow:hidden;
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#0a7a2f);
}}

.plane {{
    position:absolute;
    top:-20px;
    font-size:30px;
    transform:rotate(90deg);
    filter: drop-shadow(0px 0px 8px #00ff88);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("""
<h1 style="text-align:center; font-size:80px; color:#00ff88;">
RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# =========================
# COMPTEUR (GROS)
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown(f"""
<div class="big">{days}</div>
<div class="label">JOURS</div>

<div style="display:flex; justify-content:center; gap:120px; margin-top:20px;">
    <div>
        <div class="big" style="font-size:90px;">{hours}</div>
        <div class="label">HEURES</div>
    </div>

    <div>
        <div class="big" style="font-size:90px;">{minutes}</div>
        <div class="label">MINUTES</div>
    </div>

    <div>
        <div class="big" style="font-size:90px;">{seconds}</div>
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
# BARRE + AVION
# =========================
st.markdown(f"""
<div style="margin-top:40px;">

<div style="display:flex; justify-content:space-between;">
    <span>Déc 2008</span>
    <span>29 Mai 2026</span>
</div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div class="plane" style="left:calc({progress * 100}% - 15px);">
        ✈️
    </div>

</div>

<div style="text-align:center; font-size:45px; margin-top:10px;">
    {progress * 100:.8f} %
</div>

</div>
""", unsafe_allow_html=True)
