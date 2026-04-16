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
mc    = st.columns([1, 1, 1, 1, 2])
tabs  = ["연구주제", "탐색적 데이터 분석", "다중공선성 확인", "회귀분석"]
icons = ["🔍", "📊", "🔬", "📉"]
for col, tab, icon in zip(mc[:4], tabs, icons):
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

    # 01 - 분석 대상 데이터만 가져오기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">분석 대상 데이터만 가져오기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path1 = os.path.join(pages_folder, "logit_1.jpg")
    if os.path.exists(img_path1):
        st.image(img_path1, use_container_width=True)
    else:
        st.info("logit_1.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:60px;"></div>', unsafe_allow_html=True)

    # 02 - 종속변수의 값 수정하기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">02</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">종속변수의 값 수정하기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # 짚고 넘어가기 섹션
    st.markdown(
        '<div style="background:linear-gradient(135deg,#1a237e,#283593);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:20px;">'

        '<div style="background:rgba(255,255,255,0.1); border-radius:12px; padding:20px 24px;">'
        '<div style="font-size:18px; font-weight:800; color:#ffeb3b; margin-bottom:12px;">📌 짚고 넘어가기</div>'
        '<div style="font-size:17px; line-height:1.9; color:white;">'
        '로지스틱 회귀분석의 결과 값은 '
        '<span style="color:#69f0ae; font-weight:700;">시그모이드 함수(Sigmoid Function)</span>'
        ' 를 거치며 '
        '<span style="color:#ffeb3b; font-weight:700;">0과 1 값으로 출력</span>'
        ' 되는 범주형 분석의 결과가 되므로,<br>'
        '종속변수의 값을 <span style="color:#ff8a80; font-weight:700;">이진분류(Binary Classification)</span>'
        ' 화 해야 합니다.'
        '</div>'
        '</div>'

        '</div>',
        unsafe_allow_html=True
    )

    img_path2 = os.path.join(pages_folder, "logit_2.jpg")
    if os.path.exists(img_path2):
        st.image(img_path2, use_container_width=True)
    else:
        st.info("logit_2.jpg 파일을 pages 폴더에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 다중공선성 확인
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "다중공선성 확인":
    st.subheader("🔬 다중공선성 확인")
    st.divider()
    st.info("다중공선성 확인 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "회귀분석":
    st.subheader("📉 회귀분석")
    st.divider()
    st.info("회귀분석 내용을 여기에 추가해 주세요.")