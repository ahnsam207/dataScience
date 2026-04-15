import streamlit as st

if "data_page" not in st.session_state:
    st.session_state.data_page = "출처"

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
mc    = st.columns([1, 1, 1, 3])
tabs  = ["출처", "찾아보기", "미리보기"]
icons = ["📂", "🔍", "👀"]
for col, tab, icon in zip(mc[:3], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="btn_data_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.data_page == tab else "secondary"
        ):
            st.session_state.data_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════════════════
# 출처
# ══════════════════════════════════════════════════
if st.session_state.data_page == "출처":
    st.subheader("📂 출처")
    st.divider()
    st.info("데이터 출처 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 찾아보기
# ══════════════════════════════════════════════════
elif st.session_state.data_page == "찾아보기":
    st.subheader("🔍 찾아보기")
    st.divider()
    st.info("데이터 찾아보기 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 미리보기
# ══════════════════════════════════════════════════
elif st.session_state.data_page == "미리보기":
    st.subheader("👀 미리보기")
    st.divider()
    st.info("데이터 미리보기 내용을 여기에 추가해 주세요.")