import streamlit as st

if "subject_page" not in st.session_state:
    st.session_state.subject_page = "다중 선형 회귀분석"

st.markdown(
    "<style>"
    ".block-container {"
    "  padding-top: 4rem !important;"
    "  padding-left: 2rem !important;"
    "  padding-right: 2rem !important;"
    "}"
    "div[data-testid='stHorizontalBlock'] button p {"
    "  font-size: 20px !important;"
    "  font-weight: 700 !important;"
    "}"
    "div[data-testid='stHorizontalBlock'] button {"
    "  height: 3.5rem !important;"
    "}"
    "</style>",
    unsafe_allow_html=True
)

# ── 상단 메뉴 버튼 ──────────────────────────────────
mc    = st.columns([1, 1, 2])
tabs  = ["다중 선형 회귀분석", "로지스틱 회귀분석"]
icons = ["📈", "📉"]
for col, tab, icon in zip(mc[:2], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="subject_tab_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.subject_page == tab else "secondary"
        ):
            st.session_state.subject_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════════════════
# 다중 선형 회귀분석
# ══════════════════════════════════════════════════
if st.session_state.subject_page == "다중 선형 회귀분석":
    st.subheader("📈 다중 선형 회귀분석")
    st.divider()
    st.info("다중 선형 회귀분석 연구주제 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 로지스틱 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.subject_page == "로지스틱 회귀분석":
    st.subheader("📉 로지스틱 회귀분석")
    st.divider()
    st.info("로지스틱 회귀분석 연구주제 내용을 여기에 추가해 주세요.")