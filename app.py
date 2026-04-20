import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# 🌐 CONFIG
# =========================
st.set_page_config(page_title="Retraite Thomas", layout="wide")

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

# =========================
# 🎬 GIF BACKGROUND
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

[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main {{
    background: transparent !important;
}}

html, body {{
    color: #0a7a2f;
    font-family: monospace;
}}

.hud-bar {{
    width: 100%;
    height: 25px;
    background: rgba(0,0,0,0.25);
    border: 1px solid rgba(10,122,47,0.5);
    border-radius: 12px;
    overflow: hidden;
}}

.hud-fill {{
    height: 100%;
    background: linear-gradient(90deg,#0a7a2f,#00ff88);
    box-shadow: 0 0 10px rgba(10,122,47,0.6);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 🛰️ TITRE
# =========================
st.markdown("""
<h1 style="text-align:center; font-size:75px; color:#0a7a2f;">
🛰️ RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# =========================
# ⏳ COMPTEUR
# =========================
remaining = TARGET - now

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
# 📊 PROGRESSION ULTRA PRÉCISE
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = elapsed / total
progress = max(0.0, min(1.0, progress))

# =========================
# 🧭 BARRE TIMELINE
# =========================
st.markdown("### 🛰️ TIMELINE 2008 → 2026")

st.markdown(f"""
<div style="display:flex; justify-content:space-between; font-size:18px;">
    <span>📅 Décembre 2008</span>
    <span>🎯 29 Mai 2026</span>
</div>

<div class="hud-bar">
    <div class="hud-fill" style="width:{progress * 100}%;"></div>
</div>

<div style="text-align:center; font-size:45px; margin-top:10px;">
    {progress * 100:.8f} %
</div>
""", unsafe_allow_html=True)
