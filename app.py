import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# 🌐 CONFIG
# =========================
st.set_page_config(page_title="HUD AVION - Retraite", layout="wide")

# =========================
# 🔁 REFRESH
# =========================
st_autorefresh(interval=1000, key="refresh")

# =========================
# 📅 TIMELINE FIXE
# =========================
START = datetime(2008, 12, 1, 0, 0, 0)
TARGET = datetime(2026, 5, 29, 17, 0, 0)

now = datetime.now()
remaining = TARGET - now

# =========================
# 🎬 FOND GIF
# =========================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif_base64 = get_base64("logo.gif")

st.markdown(f"""
<style>

/* BACKGROUND AVION */
.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* HUD GLOBAL */
html, body {{
    color: #00ff88;
    font-family: monospace;
}}

/* PANNEAUX AVION */
.panel {{
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(0,255,136,0.4);
    border-radius: 12px;
    padding: 20px;
    text-align:center;
    box-shadow: 0 0 15px rgba(0,255,136,0.2);
}}

/* GROS CHIFFRES */
.big {{
    font-size:110px;
    margin:0;
    line-height:1;
}}

.label {{
    font-size:22px;
    letter-spacing:3px;
}}

.small {{
    font-size:50px;
}}

.bar {{
    width:100%;
    height:20px;
    background: rgba(255,255,255,0.1);
    border-radius:10px;
    overflow:hidden;
    border:1px solid rgba(0,255,136,0.4);
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#0a7a2f);
    box-shadow: 0 0 10px #00ff88;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 🛰️ TITRE AVION
# =========================
st.markdown("""
<h1 style='text-align:center; font-size:70px; color:#00ff88;'>
✈️ COCKPIT MISSION - RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# =========================
# ⏳ TEMPS
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# =========================
# 📊 PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# ✈️ HUD COMPTEUR
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="panel">
        <div class="big">{days}</div>
        <div class="label">JOURS DE VOL</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="panel">
        <div class="big">{hours}</div>
        <div class="label">HEURES DE VOL</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="panel">
        <div class="small">{minutes}</div>
        <div class="label">MIN</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="panel">
        <div class="small">{seconds}</div>
        <div class="label">SEC</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# 🧭 BARRE AVION
# =========================
st.markdown("### 🧭 NAVIGATION")

st.markdown(f"""
<div class="bar">
    <div class="fill" style="width:{progress * 100}%;"></div>
</div>

<div style="text-align:center; font-size:40px; margin-top:10px;">
    {progress * 100:.8f} %
</div>
""", unsafe_allow_html=True)
