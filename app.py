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
# GIF BACKGROUND (SAFE)
# =========================
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif = get_base64("logo.gif")

st.markdown(f"""
<style>

/* GIF EN FOND */
.stApp {{
    background-image: url("data:image/gif;base64,{gif}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* améliore lisibilité */
.main {{
    background-color: rgba(0,0,0,0.35);
    padding: 20px;
    border-radius: 10px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# TITRE
# =========================
st.title("RETRAITE THOMAS")

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

st.write(f"{progress * 100:.8f} %")
