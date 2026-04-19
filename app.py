import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# 🔁 refresh chaque seconde
st_autorefresh(interval=1000, key="refresh")

# 🎯 date cible
TARGET = datetime(2026, 5, 29, 17, 0, 0)

# 🧠 calcul temps restant
now = datetime.now()
remaining = TARGET - now

# 🌐 config page
st.set_page_config(page_title="Retraite Thomas", layout="wide")

# 🛰️ TITRE XXL
st.markdown(
    """
    <h1 style="
        text-align:center;
        font-size:90px;
        color:#00ff66;
        font-family:monospace;
        text-shadow: 0px 0px 20px #00ff66;
    ">
    🛰️ RETRAITE THOMAS
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# 🎯 fin de mission
if remaining.total_seconds() <= 0:
    st.markdown(
        "<h2 style='text-align:center;font-size:60px;color:#00ff66;'>🎉 MISSION ACCOMPLIE 🚀</h2>",
        unsafe_allow_html=True
    )
    st.stop()

# ⏳ calculs
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# 🧱 layout XXL
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<h1 style='font-size:70px;text-align:center'>{days}</h1><p style='text-align:center'>JOURS</p>", unsafe_allow_html=True)
col2.markdown(f"<h1 style='font-size:70px;text-align:center'>{hours}</h1><p style='text-align:center'>HEURES</p>", unsafe_allow_html=True)
col3.markdown(f"<h1 style='font-size:70px;text-align:center'>{minutes}</h1><p style='text-align:center'>MINUTES</p>", unsafe_allow_html=True)
col4.markdown(f"<h1 style='font-size:70px;text-align:center'>{seconds}</h1><p style='text-align:center'>SECONDES</p>", unsafe_allow_html=True)

st.markdown("---")

# 📊 progression
total = (TARGET - datetime(2025, 1, 1)).total_seconds()
progress = max(0.0, min(1.0, remaining.total_seconds() / total))

st.progress(progress)

# 🛰️ footer
st.markdown(
    "<p style='text-align:center;color:gray'>🛰️ système de mission actif — temps réel</p>",
    unsafe_allow_html=True
)
