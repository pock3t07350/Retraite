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

# ⚪ fond blanc
st.markdown("""
<style>
body {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# 🛰️ TITRE
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

# ❌ fin mission
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

# 📊 progression 0 → 100
progress = (now - start).total_seconds() / (TARGET - start).total_seconds()
progress = max(0.0, min(1.0, progress))

# =========================
# ⏱ COMPTEUR
# =========================

st.markdown("### 🛰️ COMPTEUR RETRAITE")

st.markdown(f"""
<h1 style='font-size:70px;color:#0a7a2f;text-align:center;'>
{days} J  {hours} H  {minutes} M  {seconds} S
</h1>
""", unsafe_allow_html=True)

st.progress(progress)

st.markdown("---")

# =========================
# 🧭 Jauge simple
# =========================

def gauge(progress):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=progress * 100,
        number={"suffix": "%"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#0a7a2f"},
        }
    ))

    fig.update_layout(
        paper_bgcolor="white",
        font={"color": "#0a7a2f"},
        height=300
    )
    return fig

st.markdown("### 🧭 PROGRESSION")

st.plotly_chart(gauge(progress), use_container_width=True)

# =========================
# 🚨 STATUS
# =========================

if progress > 0.9:
    st.error("🚨 RETRAITE IMMINENTE")
elif progress > 0.75:
    st.warning("⚠️ Phase finale")
else:
    st.success("🟢 Mission active")

# =========================
# FOOTER
# =========================

st.markdown("""
<p style='text-align:center;color:gray'>
version stable sans images ni dépendances externes
</p>
""", unsafe_allow_html=True)
