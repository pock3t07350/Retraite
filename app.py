import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
import base64

# =========================
# 🌐 CONFIG PAGE
# =========================
st.set_page_config(page_title="Retraite Thomas", layout="wide")

# =========================
# 🔁 REFRESH LIVE
# =========================
st_autorefresh(interval=1000, key="refresh")

# =========================
# 🎯 DATE CIBLE
# =========================
TARGET = datetime(2026, 5, 29, 17, 0, 0)

now = datetime.now()
remaining = TARGET - now

# =========================
# 🧠 START FIXE
# =========================
if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()

start = st.session_state.start_time

# =========================
# 🎬 GIF BACKGROUND
# =========================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif_base64 = get_base64("logo.gif")

st.markdown(f"""
<style>

/* =========================
   BACKGROUND HUD
========================= */
.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* transparent global */
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main {{
    background: transparent !important;
}}

/* =========================
   HUD PANEL STYLE
========================= */
.hud-box {{
    background: rgba(0,0,0,0.25);
    border: 1px solid rgba(10,122,47,0.5);
    border-radius: 12px;
    padding: 20px;
    margin: 10px auto;
    width: 280px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(10,122,47,0.2);
}}

.hud-number {{
    font-size: 70px;
    color: #0a7a2f;
    font-family: monospace;
    margin: 0;
}}

.hud-label {{
    font-size: 22px;
    color: #0a7a2f;
    letter-spacing: 2px;
}}

/* texte global */
html, body, [class*="css"] {{
    color: #0a7a2f;
}}

h1, h2, h3 {{
    text-shadow: 0px 0px 10px rgba(0,0,0,0.4);
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 🛰️ TITRE
# =========================
st.markdown("""
<h1 style="
    text-align:center;
    font-size:85px;
    color:#0a7a2f;
    font-family:monospace;
">
🛰️ RETRAITE THOMAS
</h1>
""", unsafe_allow_html=True)

# =========================
# ❌ FIN MISSION
# =========================
if remaining.total_seconds() <= 0:
    st.markdown("""
    <h1 style='text-align:center;font-size:70px;color:#0a7a2f;'>
    🎉 MISSION ACCOMPLIE 🚀
    </h1>
    """, unsafe_allow_html=True)
    st.stop()

# =========================
# ⏳ TEMPS
# =========================
days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

# =========================
# 📊 PROGRESSION
# =========================
progress = (now - start).total_seconds() / (TARGET - start).total_seconds()
progress = max(0.0, min(1.0, progress))

# =========================
# 🛰️ HUD COMPTEUR
# =========================
st.markdown("### 🛰️ HUD SYSTEM STATUS")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="hud-box">
        <div class="hud-number">{days}</div>
        <div class="hud-label">JOURS</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="hud-box">
        <div class="hud-number">{hours}</div>
        <div class="hud-label">HEURES</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="hud-box">
        <div class="hud-number">{minutes}</div>
        <div class="hud-label">MINUTES</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="hud-box">
        <div class="hud-number">{seconds}</div>
        <div class="hud-label">SECONDES</div>
    </div>
    """, unsafe_allow_html=True)

st.progress(progress)

# =========================
# 🧭 GAUGE
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
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
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
    st.warning("⚠️ PHASE FINALE")
else:
    st.success("🟢 MISSION ACTIVE")

# =========================
# FOOTER
# =========================
st.markdown("""
<p style='text-align:center;color:rgba(0,0,0,0.5)'>
HUD SYSTEM v1 — transparent cockpit mode
</p>
""", unsafe_allow_html=True)
