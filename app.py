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

# 🌐 config (fond blanc)
st.set_page_config(page_title="Retraite Thomas", layout="wide")

st.markdown("""
<style>
body {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# 🛰️ TITLE XXL (fond blanc)
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

# ⏳ calculs
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# 📊 progression globale
total = (TARGET - datetime(2025, 1, 1)).total_seconds()
progress = max(0.0, min(1.0, remaining.total_seconds() / total))

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

# =========================
# 🧱 COMPTEURS
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<h1 style='font-size:70px;text-align:center;color:#0a7a2f'>{days}</h1><p style='text-align:center'>JOURS</p>", unsafe_allow_html=True)
col2.markdown(f"<h1 style='font-size:70px;text-align:center;color:#0a7a2f'>{hours}</h1><p style='text-align:center'>HEURES</p>", unsafe_allow_html=True)
col3.markdown(f"<h1 style='font-size:70px;text-align:center;color:#0a7a2f'>{minutes}</h1><p style='text-align:center'>MINUTES</p>", unsafe_allow_html=True)
col4.markdown(f"<h1 style='font-size:70px;text-align:center;color:#0a7a2f'>{seconds}</h1><p style='text-align:center'>SECONDES</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 🧭 GAUGE
# =========================

st.markdown("### 🧭 COMPTE-TOUR MISSION")

st.plotly_chart(gauge(progress), use_container_width=True)

# =========================
# 📊 PROGRESSION
# =========================

st.markdown("### 📊 PROGRESSION GLOBALE")
st.progress(progress)

# =========================
# 🚨 ALERTES
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
🛰️ système cockpit actif — mode fond blanc
</p>
""", unsafe_allow_html=True)
