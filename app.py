import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go

# 🔁 refresh live
st_autorefresh(interval=1000, key="refresh")

# 🎯 date cible
TARGET = datetime(2026, 5, 29, 17, 0, 0)

now = datetime.now()
remaining = TARGET - now

# 🌐 config page
st.set_page_config(page_title="Retraite Thomas", layout="wide")

# 🧠 départ figé (0% = première ouverture)
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()

start = st.session_state.start_time

# ⚪ fond blanc propre
st.markdown("""
<style>
body {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# 🛰️ TITRE XXL
st.markdown("""
<h1 style="
    text-align:center;
    font-size:90px;
    color:#0a7a2f;
    font-family:monospace;
">
🛰️ RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# ❌ mission terminée
if remaining.total_seconds() <= 0:
    st.markdown("""
    <h1 style='text-align:center;font-size:70px;color:#0a7a2f;'>
    🎉 MISSION ACCOMPLIE 🚀
    </h1>
    """, unsafe_allow_html=True)
    st.stop()

# ⏳ temps
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# 📊 progression figée (0 → 100%)
progress = (now - start).total_seconds() / (TARGET - start).total_seconds()
progress = max(0.0, min(1.0, progress))

# =========================
# 🎣 PÊCHEUR (SAFE)
# =========================

# 👉 OPTION 1 : GIF local (RECOMMANDÉ)
# Mets un fichier fishing.gif dans ton repo GitHub
fishing_path = "fishing.gif"

# fallback si fichier absent
try:
    st.image(fishing_path, caption="🎣 Pêche à la mouche", use_container_width=True)
except:
    st.info("🎣 (Ajoute fishing.gif dans ton repo pour afficher l’animation)")

# =========================
# ⏱ COMPTEUR
# =========================

st.markdown("### 🛰️ RETRAITE THOMAS")

st.markdown(f"""
<h1 style='font-size:60px;color:#0a7a2f'>
{days} j {hours} h {minutes} m {seconds} s
</h1>
""", unsafe_allow_html=True)

st.progress(progress)

st.markdown("---")

# =========================
# 🧭 JAUGE
# =========================

def gauge(progress):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress * 100,
        number={"suffix": "%"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#0a7a2f"},
            "steps": [
                {"range": [0, 50], "color": "#f2f2f2"},
                {"range": [50, 80], "color": "#e6e6e6"},
                {"range": [80, 100], "color": "#d9d9d9"},
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": 100
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor="white",
        font={"color": "#0a7a2f"},
        height=350
    )
    return fig

st.markdown("### 🧭 COMPTE-TOUR MISSION")
st.plotly_chart(gauge(progress), use_container_width=True)

# =========================
# 🚨 ALARMES
# =========================

st.markdown("---")

if progress > 0.9:
    st.error("🚨 ALERTE : RETRAITE IMMINENTE")
elif progress > 0.75:
    st.warning("⚠️ Phase finale mission")
else:
    st.success("🟢 Mission en cours nominale")

# =========================
# FOOTER
# =========================

st.markdown("""
<p style='text-align:center;color:gray'>
🛰️ système cockpit actif — version stable sans dépendances externes
</p>
""", unsafe_allow_html=True)
