import streamlit as st
import os
import base64

pages_folder = os.path.dirname(os.path.abspath(__file__))

def img_to_base64(img_path):
    ext  = img_path.split(".")[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return mime, b64

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
    "#top-anchor { position: absolute; top: 0; }"
    ".top-btn {"
    "  position: fixed;"
    "  bottom: 40px;"
    "  right: 40px;"
    "  background: linear-gradient(135deg, #e53935, #ef9a9a);"
    "  color: white;"
    "  border: none;"
    "  border-radius: 50px;"
    "  padding: 12px 22px;"
    "  font-size: 16px;"
    "  font-weight: 800;"
    "  cursor: pointer;"
    "  box-shadow: 0 4px 16px rgba(229,57,53,0.4);"
    "  z-index: 9999;"
    "  text-decoration: none;"
    "}"
    ".top-btn:hover { background: linear-gradient(135deg,#c62828,#e53935); }"
    "</style>",
    unsafe_allow_html=True
)

st.markdown('<div id="top-anchor"></div>', unsafe_allow_html=True)

# ── 상단 메뉴 버튼 ──────────────────────────────────
mc    = st.columns([2, 2, 2, 2, 1])
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
        '윤리의식 여부 <span style="color:#8e24aa; font-weight:700;">(Q14_4_10)</span>'
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

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fce4ec,#f3e5f5);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:20px;'
        ' border-left:6px solid #e53935;">'
        '<div style="display:flex; flex-direction:column; gap:14px;">'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI를 사용한 경험 <span style="color:#e53935; font-weight:700;">(Q4)</span> 이 있는 학생과'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '일반고 <span style="color:#e53935; font-weight:700;">(SQ0_3 = 2)</span>,'
        ' 특성화고 <span style="color:#e53935; font-weight:700;">(SQ0_3 = 5)</span>'
        ' 대상인 학생 데이터 중에서'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">3</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI에 어떻게 질문하는지 알고 있다 <span style="color:#e53935; font-weight:700;">(Q14_2_4)</span>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">4</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI 사용빈도 _ 챗GPT <span style="color:#e53935; font-weight:700;">(Q6_1)</span>,'
        ' 제미나이 <span style="color:#e53935; font-weight:700;">(Q6_4)</span>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">5</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI의 사용목적이 성적향상 <span style="color:#e53935; font-weight:700;">(Q9_6)</span> 인 데이터와'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">6</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI 사용 시 윤리의식 여부 <span style="color:#e53935; font-weight:700;">(Q14_4_10)</span> 데이터 불러오기'
        '</div>'
        '</div>'

        '</div>'
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
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e8f5e9,#e0f7fa);'
            ' border-radius:12px; padding:20px 28px; margin-top:16px;'
            ' border-left:6px solid #26a69a;">'
            '<div style="display:flex; align-items:center; gap:12px;">'
            '<span style="font-size:24px;">✅</span>'
            '<div style="font-size:17px; line-height:1.9; color:#222;">'
            '생성형 AI 사용 시 윤리의식 여부 '
            '<span style="background:#e0f7fa; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#00695c;">ai_moral</span>'
            ' 의 값이 '
            '<span style="font-weight:700; color:#e53935;">리커트 척도 (1~5)</span>'
            ' 에서 '
            '<span style="font-weight:700; color:#1976d2;">0과 1 이진 분류 값</span>'
            ' 으로 수정되었다.'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("logit_2.jpg 파일을 pages 폴더에 추가해 주세요.")
    st.markdown('<div style="margin-bottom:60px;"></div>', unsafe_allow_html=True)

    # 03 - 상관계수 및 상관관계 확인하기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">03</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">상관계수 및 상관관계 확인하기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path3 = os.path.join(pages_folder, "logit_3.jpg")
    if os.path.exists(img_path3):
        st.image(img_path3, use_container_width=True)
    else:
        st.info("logit_3.jpg 파일을 pages 폴더에 추가해 주세요.")

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

# ── TOP 버튼 ──────────────────────────────────────
st.markdown(
    '<a href="#top-anchor" class="top-btn">▲ TOP</a>',
    unsafe_allow_html=True
)
