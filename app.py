import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# 🔁 refresh toutes les secondes
st_autorefresh(interval=1000, key="refresh")

# 🎯 Date cible (29 mai 2026 à 17h00)
TARGET = datetime(2026, 5, 29, 17, 0, 0)

# 🧠 Calcul du temps restant
now = datetime.now()
remaining = TARGET - now

# Si déjà passé
if remaining.total_seconds() <= 0:
    st.title("🎉 MISSION ACCOMPLIE")
    st.success("Départ en retraite atteint 🚀")
else:

    days = remaining.days
    hours = remaining.seconds // 3600
    minutes = (remaining.seconds % 3600) // 60
    seconds = remaining.seconds % 60

    # 🛰️ UI style cockpit simple
    st.set_page_config(page_title="Retraite Countdown", layout="centered")

    st.title("🛰️ MISSION RETRAITE COUNTDOWN")

    st.markdown("### ⏳ Temps restant")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Jours", days)
    col2.metric("Heures", hours)
    col3.metric("Minutes", minutes)
    col4.metric("Secondes", seconds)

    # 📊 progression globale
    total_duration = (TARGET - datetime(2025, 1, 1)).total_seconds()
    progress = max(0.0, min(1.0, remaining.total_seconds() / total_duration))

    st.progress(progress)

    st.caption("Système de mission actif — mise à jour en temps réel 🚀")
