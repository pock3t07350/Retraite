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
# GIF BACKGROUND SAFE
# =========================
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif = get_base64("logo.gif")

st.markdown(f"""
<style>

/* BACKGROUND */
.stApp {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* OVERLAY pour lisibilité */
.block-container {{
    background-color: rgba(0,0,0,0.45);
    padding: 2rem;
    border-radius: 12px;
}}

/* TITRE */
.title {{
    text-align:center;
    font-size:70px;
    font-weight:700;
    color:#00ff88;
    margin-bottom:20px;
}}

/* METRICS PLUS CLEAN */
div[data-testid="metric-container"] {{
    background: rgba(0,255,136,0.08);
    border: 1px solid rgba(0,255,136,0.25);
    padding: 15px;
    border-radius: 12px;
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

st.progress(progress)

st.markdown(
    f"<div style='text-align:center;font-size:40px;color:#00ff88;'>"
    f"{progress * 100:.8f} %</div>",
    unsafe_allow_html=True
)
