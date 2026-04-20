# =========================
# ⏳ COMPTEUR HUD GÉANT
# =========================
remaining = TARGET - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60
seconds = remaining.seconds % 60

st.markdown("""
<style>
.hud-big {
    text-align:center;
    font-family: monospace;
    color:#0a7a2f;
}

/* blocs principaux énormes */
.big-number {
    font-size:120px;
    margin:0;
    line-height:1;
}

/* labels */
.big-label {
    font-size:28px;
    letter-spacing:3px;
}

/* secondaire */
.small-number {
    font-size:50px;
    margin:0;
}

.small-label {
    font-size:18px;
    opacity:0.8;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hud-big">

    <div>
        <div class="big-number">{days}</div>
        <div class="big-label">JOURS</div>
    </div>

    <br>

    <div>
        <div class="big-number">{hours}</div>
        <div class="big-label">HEURES</div>
    </div>

    <br>

    <div style="display:flex; justify-content:center; gap:80px; margin-top:20px;">

        <div>
            <div class="small-number">{minutes}</div>
            <div class="small-label">MIN</div>
        </div>

        <div>
            <div class="small-number">{seconds}</div>
            <div class="small-label">SEC</div>
        </div>

    </div>

</div>
""", unsafe_allow_html=True)
