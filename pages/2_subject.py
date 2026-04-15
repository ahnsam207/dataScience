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

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:24px; color:#1565c0;">📈 다중 선형 회귀분석 연구주제</div>'
        '<div style="display:flex; flex-direction:column; gap:20px;">'

        '<div style="display:flex; align-items:flex-start; gap:16px;">'
        '<span style="background:#1976d2; color:white; border-radius:10px;'
        ' padding:4px 14px; font-size:15px; font-weight:700; flex-shrink:0; margin-top:2px;">독립변수 (3개)</span>'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '생성형 AI의 사용목적 : 숙제 <span style="color:#1976d2; font-weight:700;">(Q9_5)</span>, '
        '성적 향상 <span style="color:#1976d2; font-weight:700;">(Q9_6)</span><br>'
        '생성형 AI의 평균사용시간 <span style="color:#1976d2; font-weight:700;">(Q7)</span>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:16px;">'
        '<span style="background:#26a69a; color:white; border-radius:10px;'
        ' padding:4px 14px; font-size:15px; font-weight:700; flex-shrink:0; margin-top:2px;">종속변수 (1개)</span>'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '학업 성적 <span style="color:#26a69a; font-weight:700;">(DQ3)</span>'
        '</div>'
        '</div>'

        '<div style="border-top:1px solid #bbdefb; padding-top:16px;">'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '💡 생성형 AI의 사용목적과 평균사용시간이 <b>학업 성적</b>에 주는 영향 분석'
        '</div>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════
# 로지스틱 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.subject_page == "로지스틱 회귀분석":

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