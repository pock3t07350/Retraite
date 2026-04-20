import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# 🌐 CONFIG
# =========================
st.set_page_config(page_title="Cockpit Retraite", layout="wide")

# =========================
# 🔁 REFRESH LIVE
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
# 🎬 BACKGROUND GIF
# =========================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif_base64 = get_base64("logo.gif")

st.markdown(f"""
<style>

/* BACKGROUND */
.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main {{
    background: transparent !important;
}}

html, body {{
    color: #00ff88;
    font-family: monospace;
}}

/* PANNEAUX COMPTEUR */
.panel {{
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(0,255,136,0.4);
    border-radius: 12px;
    padding: 20px;
    text-align:center;
    box-shadow: 0 0 15px rgba(0,255,136,0.2);
}}

.big {{
    font-size:110px;
    margin:0;
    line-height:1;
}}

.label {{
    font-size:22px;
    letter-spacing:3px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 🛰️ TITRE
# =========================
st.markdown("""
<h1 style="text-align:center; font-size:70px; color:#00ff88;">
✈️ COCKPIT MISSION - RETRAITE
</h1>
""", unsafe_allow_html=True)

# =========================
# ⏳ COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="panel">
        <div class="big">{days}</div>
        <div class="label">JOURS</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="panel">
        <div class="big">{hours}</div>
        <div class="label">HEURES</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# 📊 PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# ✈️ TIMELINE AVION
# =========================
st.markdown("### 🛰️ NAVIGATION")

st.markdown(f"""
<div style="position:relative; width:100%;">

    <!-- DATES -->
    <div style="display:flex; justify-content:space-between; font-size:18px;">
        <span>📅 Décembre 2008</span>
        <span>🎯 29 Mai 2026</span>
    </div>

    <!-- BARRE -->
    <div style="
        position:relative;
        width:100%;
        height:25px;
        margin-top:10px;
        background: rgba(0,0,0,0.25);
        border:1px solid rgba(0,255,136,0.4);
        border-radius:12px;
        overflow:hidden;
    ">

        <!-- FILL -->
        <div style="
            width:{progress * 100}%;
            height:100%;
            background: linear-gradient(90deg,#00ff88,#0a7a2f);
            box-shadow: 0 0 10px #00ff88;
        "></div>

        <!-- AVION -->
        <div style="
            position:absolute;
            top:-18px;
            left:calc({progress * 100}% - 15px);
            font-size:30px;
            transform:rotate(90deg);
            filter: drop-shadow(0px 0px 6px #00ff88);
        ">
            ✈️
        </div>

    </div>

    <!-- % -->
    <div style="text-align:center; font-size:40px; margin-top:10px;">
        {progress * 100:.8f} %
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# 🚨 STATUS SIMPLE
# =========================
if progress > 0.9:
    st.warning("⚠️ APPROCHE TERMINALE")
else:
    st.success("🟢 MISSION ACTIVE")
