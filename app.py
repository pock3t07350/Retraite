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
# PROGRESSION
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = max(0.0, min(1.0, elapsed / total))

# =========================
# GIF BACKGROUND
# =========================
def get_base64(file):
    with open(file, "rb") as f:
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
    font-size:60px;
    font-weight:700;
    color:#0a2a43;
    margin-bottom:160px;
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

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"### JOURS\n# {days}")
col2.markdown(f"### HEURES\n# {hours}")
col3.markdown(f"### MINUTES\n# {minutes}")
col4.markdown(f"### SECONDES\n# {seconds}")

# =========================
# BARRE SIMPLE (VERSION QUI MARCHE)
# =========================
st.progress(progress)

st.markdown(
    f"<div style='text-align:center;font-size:35px;color:#0a2a43;margin-top:10px;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
