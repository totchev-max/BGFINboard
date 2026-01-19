import streamlit as st
from demo_profile import DEMO_PROFILE_2026
from engine import run_demo_year

st.set_page_config(
    page_title="Национален финансов борд — DEMO",
    layout="wide"
)

st.title("🇧🇬 Национален финансов борд")
st.caption("Демонстрационна симулация на държавен бюджет (годишна)")

# --- Policy levers UI ---
st.subheader("🎛 Политически лостове (DEMO)")

col1, col2, col3 = st.columns(3)

with col1:
    admin_wages = st.slider("Заплати администрация (%)", 0, 20, 0)
    mon_wages = st.slider("Заплати МОН (%)", 0, 20, 0)

with col2:
    pensions = st.slider("Пенсии (%)", 0, 20, 0)
    capex = st.slider("Капиталови разходи (млрд €)", 0.0, 5.0, 0.0, 0.1)

with col3:
    vat_to = st.slider("ДДС ставка (%)", 20, 25, 20)

levers = {
    "admin_wages_pct": admin_wages,
    "mon_wages_pct": mon_wages,
    "pensions_pct": pensions,
    "capex_bn": capex,
    "vat_rate_from": 20.0,
    "vat_rate_to": float(vat_to),
    "growth_forecast_pct": 2.6,
    "inflation_forecast_pct": 3.2
}

if st.button("▶ Симулирай година"):
    out = run_demo_year(DEMO_PROFILE_2026, levers)

    st.subheader("📊 Резултат от симулацията")

    c1, c2, c3 = st.columns(3)
    c1.metric("Приходи", f"{out['revenues']:.1f} млрд €")
    c2.metric("Разходи", f"{out['expenditures']:.1f} млрд €")
    c3.metric("Дефицит", f"{out['deficit']:.1f} млрд €")

    st.markdown("### ⚠️ Фискални индикатори")
    st.write(f"Дефицит / БВП: **{out['deficit_pct']*100:.2f}%**")
    st.write(f"Дълг / БВП: **{out['debt_pct']*100:.2f}%**")

st.markdown("---")
st.caption("DEMO система • Всички данни са примерни • Цел: яснота за последствията")
