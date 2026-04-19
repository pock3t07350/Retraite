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

# 🌐 config
st.set_page_config(page_title="Retraite Thomas", layout="wide")

# 🛰️ TITLE XXL
st.markdown("""
<h1 style="
    text-align:center;
    font-size:90px;
    color:#00ff66;
    font-family:monospace;
    text-shadow: 0px 0px 25px #00ff66;
">
🛰️ RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# ❌ mission terminée
if remaining.total_seconds() <= 0:
    st.markdown("""
    <h1 style='text-align:center;font-size:70px;color:#00ff66;'>
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
# 🧭 JAUGE ANALOGIQUE
# =========================
def gauge(progress):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress * 100,
        number={"suffix": "%"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#00ff66"},
            "steps": [
                {"range": [0, 50], "color": "#111111"},
                {"range": [50, 80], "color": "#222222"},
                {"range": [80, 100], "color": "#003300"},
            ],
            "threshold": {
                "line": {"color": "red", "width": 4},
                "thickness": 0.75,
                "value": 100
            }
        }
    ))

    fig.update_layout(
        paper_bgcolor="black",
        font={"color": "#00ff66"},
        height=350
    )
    return fig

# =========================
# 📡 RADAR (style progress circulaire)
# =========================
def radar(progress):
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[progress, progress, progress],
        theta=[0, 120, 240],
        fill='toself',
        line=dict(color="#00ff66")
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1])
        ),
        showlegend=False,
        paper_bgcolor="black",
        font_color="#00ff66",
        height=350
    )
    return fig

# =========================
# 🧱 LAYOUT PRINCIPAL
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"<h1 style='font-size:70px;text-align:center'>{days}</h1><p style='text-align:center'>JOURS</p>", unsafe_allow_html=True)
col2.markdown(f"<h1 style='font-size:70px;text-align:center'>{hours}</h1><p style='text-align:center'>HEURES</p>", unsafe_allow_html=True)
col3.markdown(f"<h1 style='font-size:70px;text-align:center'>{minutes}</h1><p style='text-align:center'>MINUTES</p>", unsafe_allow_html=True)
col4.markdown(f"<h1 style='font-size:70px;text-align:center'>{seconds}</h1><p style='text-align:center'>SECONDES</p>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# 🧭 GAUGE + RADAR
# =========================

col5, col6 = st.columns(2)

with col5:
    st.markdown("### 🧭 COMPTE-TOUR MISSION")
    st.plotly_chart(gauge(progress), use_container_width=True)

with col6:
    st.markdown("### 📡 RADAR RETRAITE")
    st.plotly_chart(radar(progress), use_container_width=True)

# =========================
# 📊 PROGRESSION BAR
# =========================

st.markdown("### 📊 PROGRESSION GLOBALE")
st.progress(progress)

# =========================
# 🚨 ALARME LOGIQUE
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
🛰️ système cockpit actif — contrôle mission retraite en temps réel
</p>
""", unsafe_allow_html=True)
