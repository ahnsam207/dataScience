import streamlit as st

if "logistic_page" not in st.session_state:
    st.session_state.logistic_page = "연구주제"

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
tabs  = ["연구주제", "탐색적 데이터 분석", "회귀분석"]
icons = ["🔍", "📊", "📉"]
for col, tab, icon in zip(mc[:3], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="logistic_tab_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.logistic_page == tab else "secondary"
        ):
            st.session_state.logistic_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════════════════
# 연구주제
# ══════════════════════════════════════════════════
if st.session_state.logistic_page == "연구주제":

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fce4ec,#f3e5f5);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #e53935;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:24px; color:#b71c1c;">📉 로지스틱 회귀분석 연구주제</div>'
        '<div style="display:flex; flex-direction:column; gap:20px;">'

        '<div style="display:flex; align-items:flex-start; gap:16px;">'
        '<span style="background:#e53935; color:white; border-radius:10px;'
        ' padding:4px 14px; font-size:15px; font-weight:700; flex-shrink:0; margin-top:2px;">독립변수 (4개)</span>'
        '<div style="display:flex; flex-direction:column; gap:10px; font-size:17px; color:#222; line-height:1.9;">'

        '<div style="display:flex; align-items:center; gap:10px;">'
        '<span style="color:#e53935; font-size:18px;">▪</span>'
        '생성형 AI에 어떻게 질문하는지 알고 있다 '
        '<span style="color:#e53935; font-weight:700; margin-left:4px;">(Q14_2_4)</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:10px;">'
        '<span style="color:#e53935; font-size:18px;">▪</span>'
        '생성형 AI 사용빈도 _ 챗GPT '
        '<span style="color:#e53935; font-weight:700; margin-left:4px;">(Q6_1)</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:10px;">'
        '<span style="color:#e53935; font-size:18px;">▪</span>'
        '생성형 AI 사용빈도 _ 제미나이 '
        '<span style="color:#e53935; font-weight:700; margin-left:4px;">(Q6_4)</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:10px;">'
        '<span style="color:#e53935; font-size:18px;">▪</span>'
        '생성형 AI의 사용목적 _ 성적향상 '
        '<span style="color:#e53935; font-weight:700; margin-left:4px;">(Q9_6)</span>'
        '</div>'

        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:16px;">'
        '<span style="background:#8e24aa; color:white; border-radius:10px;'
        ' padding:4px 14px; font-size:15px; font-weight:700; flex-shrink:0; margin-top:2px;">종속변수 (1개)</span>'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '윤리의식 여부'
        '</div>'
        '</div>'

        '<div style="border-top:1px solid #f8bbd0; padding-top:16px;">'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '💡 생성형 AI 사용 관련 요인들이 <b>윤리의식 여부</b>에 주는 영향 분석'
        '</div>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════
# 탐색적 데이터 분석
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "탐색적 데이터 분석":
    st.subheader("📊 탐색적 데이터 분석")
    st.divider()
    st.info("탐색적 데이터 분석 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "회귀분석":
    st.subheader("📉 회귀분석")
    st.divider()
    st.info("회귀분석 내용을 여기에 추가해 주세요.")