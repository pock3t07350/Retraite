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
    margin-bottom:60px;
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

col1, col2, col3, col4 = st.columns(4, gap="large")

col1.markdown(
    f"<div style='text-align:center'><div>JOURS</div><div style='font-size:70px;font-weight:800'>{days}</div></div>",
    unsafe_allow_html=True
)

col2.markdown(
    f"<div style='text-align:center'><div>HEURES</div><div style='font-size:70px;font-weight:800'>{hours}</div></div>",
    unsafe_allow_html=True
)

col3.markdown(
    f"<div style='text-align:center'><div>MINUTES</div><div style='font-size:70px;font-weight:800'>{minutes}</div></div>",
    unsafe_allow_html=True
)

col4.markdown(
    f"<div style='text-align:center'><div>SECONDES</div><div style='font-size:70px;font-weight:800'>{seconds}</div></div>",
    unsafe_allow_html=True
)

# =========================
# BARRE
# =========================
st.progress(progress)

st.markdown(
    f"<div style='text-align:center;font-size:35px;color:#0a2a43;margin-top:100px;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
