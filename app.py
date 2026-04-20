import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import base64

# =========================
# 🌐 CONFIG PAGE
# =========================
st.set_page_config(page_title="Retraite Thomas", layout="wide")

# =========================
# 🔁 REFRESH LIVE
# =========================
st_autorefresh(interval=1000, key="refresh")

# =========================
# 📅 TIMELINE FIXE
# =========================
start = datetime(2008, 12, 1, 0, 0, 0)
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

/* BACKGROUND GIF */
.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* FULL TRANSPARENT UI */
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main {{
    background: transparent !important;
}}

/* HUD TEXT STYLE */
html, body {{
    color: #0a7a2f;
    font-family: monospace;
}}

h1, h2, h3 {{
    text-shadow: 0 0 10px rgba(0,0,0,0.4);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 🛰️ TITRE
# =========================
st.markdown("""
<h1 style="text-align:center; font-size:80px; color:#0a7a2f;">
🛰️ RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# =========================
# 📊 PROGRESSION
# =========================
total = (TARGET - start).total_seconds()
elapsed = (now - start).total_seconds()

progress = elapsed / total
progress = max(0.0, min(1.0, progress))

progress_percent = progress * 100

# =========================
# 🧭 HUD TIMELINE BAR
# =========================
st.markdown("### 🛰️ TIMELINE SYSTEM")

st.markdown(f"""
<div style="text-align:center;">

<!-- LABELS -->
<div style="display:flex; justify-content:space-between; font-size:18px;">
    <span>📅 Décembre 2008</span>
    <span>🎯 29 Mai 2026</span>
</div>

<!-- BAR -->
<div style="
    width:100%;
    height:25px;
    background: rgba(0,0,0,0.25);
    border: 1px solid rgba(10,122,47,0.5);
    border-radius: 12px;
    overflow: hidden;
    margin-top:10px;
">

    <div style="
        width:{progress * 100}%;
        height:100%;
        background: linear-gradient(90deg, #0a7a2f, #00ff88);
        box-shadow: 0 0 12px rgba(10,122,47,0.7);
    "></div>

</div>

<!-- % -->
<div style="font-size:40px; margin-top:10px;">
    {progress_percent:.3f} %
</div>

</div>
""", unsafe_allow_html=True)

# =========================
# 📌 STATUS LOGIC
# =========================
st.markdown("### 🧭 STATUS")

if progress > 0.99:
    st.error("🚨 PHASE FINALE CRITIQUE")
elif progress > 0.90:
    st.warning("⚠️ APPROCHE TERMINALE")
else:
    st.success("🟢 MISSION EN COURS")

# =========================
# FOOTER
# =========================
st.markdown("""
<p style='text-align:center; color:rgba(0,0,0,0.5)'>
HUD TIMELINE SYSTEM — 2008 → 2026
</p>
""", unsafe_allow_html=True)
