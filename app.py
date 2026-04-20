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
# 🎬 GIF BACKGROUND (FIABLE)
# =========================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

gif_base64 = get_base64("logo.gif")

st.markdown(f"""
<style>
/* =========================
   FOND GLOBAL GIF
========================= */
.stApp {{
    background: url("data:image/gif;base64,{gif_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* =========================
   SUPPRESSION FONDS STREAMLIT
========================= */
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main {{
    background: transparent !important;
}}

/* blocs UI transparents */
div[data-testid="stVerticalBlock"],
div[data-testid="stHorizontalBlock"],
div[data-testid="stMetric"],
div[data-testid="stDataFrame"],
div[data-testid="stPlotlyChart"] {{
    background: transparent !important;
    box-shadow: none !important;
}}

/* progress bar clean */
.stProgress > div > div > div > div {{
    background-color: #0a7a2f;
}}

/* texte */
html, body, [class*="css"] {{
    color: #0a7a2f;
}}

/* titre effet cockpit */
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
    font-size:90px;
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
# ⏳ TEMPS RESTANT
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
# ⏱ COMPTEUR
# =========================
st.markdown("### 🛰️ COMPTEUR RETRAITE")

st.markdown(f"""
<h1 style="
    font-size:70px;
    color:#0a7a2f;
    text-align:center;
    background: transparent;
">
{days} J  {hours} H  {minutes} M  {seconds} S
</h1>
""", unsafe_allow_html=True)

st.progress(progress)

st.markdown("---")

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
    st.warning("⚠️ Phase finale")
else:
    st.success("🟢 Mission active")

# =========================
# FOOTER
# =========================
st.markdown("""
<p style='text-align:center;color:rgba(0,0,0,0.5)'>
version cockpit transparent + fond GIF animé
</p>
""", unsafe_allow_html=True)
