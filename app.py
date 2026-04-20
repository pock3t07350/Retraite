import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Cockpit Mission", layout="wide")
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
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif_base64 = get_base64("logo.gif")

st.markdown(f"""
<style>

.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

html, body {{
    color: #00ff88;
    font-family: monospace;
}}

.bar {{
    position:relative;
    width:100%;
    height:25px;
    background: rgba(0,0,0,0.3);
    border-radius:12px;
    border:1px solid rgba(0,255,136,0.4);
    overflow:hidden;
}}

.fill {{
    height:100%;
    background: linear-gradient(90deg,#00ff88,#0a7a2f);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.markdown("""
<h1 style="text-align:center; font-size:70px; color:#00ff88;">
✈️ COCKPIT RETRAITE
</h1>
""", unsafe_allow_html=True)

# =========================
# COMPTEUR (IMPORTANT FIX)
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

col1, col2, col3, col4 = st.columns(4)

col1.metric("JOURS", days)
col2.metric("HEURES", hours)
col3.metric("MINUTES", minutes)
col4.metric("SECONDES", seconds)

# =========================
# PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# TIMELINE + AVION
# =========================
st.markdown("### 🛰️ NAVIGATION")

st.markdown(f"""
<div>

<div style="display:flex; justify-content:space-between;">
    <span>📅 Déc 2008</span>
    <span>🎯 29 Mai 2026</span>
</div>

<div class="bar">

    <div class="fill" style="width:{progress * 100}%;"></div>

    <div style="
        position:absolute;
        top:-18px;
        left:calc({progress * 100}% - 15px);
        font-size:28px;
        transform:rotate(90deg);
        filter: drop-shadow(0px 0px 6px #00ff88);
    ">
        ✈️
    </div>

</div>

<div style="text-align:center; font-size:40px; margin-top:10px;">
    {progress * 100:.8f} %
</div>

</div>
""", unsafe_allow_html=True)
