import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Cockpit Retraite", layout="wide")
st_autorefresh(interval=1000, key="refresh")

# =========================
# TIMELINE
# =========================
START = datetime(2008, 12, 1, 0, 0, 0)
TARGET = datetime(2026, 5, 29, 17, 0, 0)

now = datetime.now()
remaining = TARGET - now

# =========================
# COMPTEUR
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.title("✈️ COCKPIT RETRAITE")

col1, col2, col3, col4 = st.columns(4)
col1.metric("JOURS", days)
col2.metric("HEURES", hours)
col3.metric("MINUTES", minutes)
col4.metric("SECONDES", seconds)

# =========================
# PROGRESSION SAFE
# =========================
total = (TARGET - START).total_seconds()
elapsed = (now - START).total_seconds()

progress = elapsed / total
progress = max(0.0, min(1.0, progress))

# =========================
# DATES (SAFE STREAMLIT)
# =========================
st.write("📅 Décembre 2008 → 🎯 29 Mai 2026")

# =========================
# BARRE + AVION (SAFE VERSION)
# =========================
st.progress(progress)

st.write(f"✈️ Avion position : {progress*100:.8f} %")
