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
tabs  = ["연구주제", "탐색적 데이터 분석", "다중공선성 확인", "로지스틱 회귀분석"]
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
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
            ' border-radius:12px; padding:20px 28px; margin-top:16px;'
            ' border-left:6px solid #f9a825;">'
            '<div style="font-size:22px; font-weight:800; color:#e65100; margin-bottom:16px;">🔍 상관계수 분석 결과</div>'
            '<div style="display:flex; flex-direction:column; gap:14px;">'

            '<div style="display:flex; align-items:flex-start; gap:12px;">'
            '<span style="background:#f9a825; color:white; border-radius:50%; min-width:28px; height:28px;'
            ' display:flex; align-items:center; justify-content:center; font-size:14px;'
            ' font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
            '<div style="font-size:17px; line-height:1.9; color:#222;">'
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 8px; font-weight:700; color:#e65100;">ai_query</span>'
            ' 와 '
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 8px; font-weight:700; color:#e65100;">ai_moral</span>'
            ' 의 상관계수는 <span style="font-weight:900; color:#e53935;">0.453</span> 으로,'
            ' 생성형 AI에 질문하는 방법을 아는 학생일수록 <b>윤리의식도 높은 경향</b>이 있음.'
            '</div>'
            '</div>'

            '<div style="display:flex; align-items:flex-start; gap:12px;">'
            '<span style="background:#f9a825; color:white; border-radius:50%; min-width:28px; height:28px;'
            ' display:flex; align-items:center; justify-content:center; font-size:14px;'
            ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
            '<div style="font-size:17px; line-height:1.9; color:#222;">'
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 8px; font-weight:700; color:#e65100;">ai_gpt</span>'
            ' 와 '
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 8px; font-weight:700; color:#e65100;">use_grade</span>'
            ' 의 상관계수는 <span style="font-weight:900; color:#e53935;">0.490</span> 으로,'
            ' 챗GPT 사용빈도가 높을수록 <b>성적향상 목적의 AI 사용도 높은 경향</b>이 있음.'
            '</div>'
            '</div>'

            '<div style="display:flex; align-items:flex-start; gap:12px;">'
            '<span style="background:#f9a825; color:white; border-radius:50%; min-width:28px; height:28px;'
            ' display:flex; align-items:center; justify-content:center; font-size:14px;'
            ' font-weight:700; flex-shrink:0; margin-top:2px;">3</span>'
            '<div style="font-size:17px; line-height:1.9; color:#222;">'
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 8px; font-weight:700; color:#e65100;">ai_gemi</span>'
            ' 는 모든 변수와의 상관계수가 <span style="font-weight:900; color:#1976d2;">0.18 이하</span> 로,'
            ' 제미나이 사용빈도는 다른 변수들과 <b>낮은 상관관계</b>를 보임.'
            '</div>'
            '</div>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("logit_3.jpg 파일을 pages 폴더에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 다중공선성 확인
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "다중공선성 확인":

    # 01 - 다중공선성 확인
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">다중공선성 확인</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path4 = os.path.join(pages_folder, "logit_4.jpg")
    if os.path.exists(img_path4):
        st.image(img_path4, use_container_width=True)
    else:
        st.info("logit_4.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:40px;"></div>', unsafe_allow_html=True)

    # 02 - 다중공선성 분석
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">02</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">다중공선성 분석</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #f9a825;">'
        '<div style="font-size:24px; font-weight:800; color:#e65100; margin-bottom:20px;">🔍 VIF 분석 결과</div>'
        '<div style="display:flex; flex-direction:column; gap:20px;">'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#f9a825; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:15px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
        '<div style="font-size:19px; line-height:2.0; color:#222;">'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px; font-weight:700; color:#e65100;">ai_gpt</span>'
        ' &nbsp; VIF <span style="font-weight:900; color:#e53935;">15.79</span> &nbsp;'
        '<span style="background:#ffebee; border-radius:8px; padding:2px 10px; font-size:15px; font-weight:700; color:#e53935;">기준값 초과 ⚠️</span><br>'
        '<span style="font-size:17px; color:#555;">'
        'ai_gpt ↔ use_grade (0.490), ai_gpt ↔ ai_query (0.361) 로 여러 변수와 중간 이상의 상관관계를 가지고 있어'
        ' 다중공선성의 주요 원인으로 판단됩니다.'
        '</span>'
        '</div>'
        '</div>'

        '<div style="border-top:1px solid #ffe082; margin:4px 0;"></div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#f9a825; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:15px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
        '<div style="font-size:19px; line-height:2.0; color:#222;">'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px; font-weight:700; color:#e65100;">ai_query</span>'
        ' &nbsp; VIF <span style="font-weight:900; color:#e53935;">12.14</span> &nbsp;'
        '<span style="background:#ffebee; border-radius:8px; padding:2px 10px; font-size:15px; font-weight:700; color:#e53935;">기준값 초과 ⚠️</span><br>'
        '<span style="font-size:17px; color:#555;">'
        'ai_query ↔ ai_moral (0.453), ai_query ↔ ai_gpt (0.361), ai_query ↔ use_grade (0.273) 로'
        ' 종속변수 및 다른 독립변수들과 고루 상관관계를 보입니다.'
        '</span>'
        '</div>'
        '</div>'

        '<div style="border-top:1px solid #ffe082; margin:4px 0;"></div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#f9a825; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:15px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">3</span>'
        '<div style="font-size:19px; line-height:2.0; color:#222;">'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px; font-weight:700; color:#e65100;">use_grade</span>'
        ' &nbsp; VIF <span style="font-weight:900; color:#f9a825;">8.33</span> &nbsp;'
        '<span style="background:#fff8e1; border-radius:8px; padding:2px 10px; font-size:15px; font-weight:700; color:#f9a825;">기준값 미만 ✔️</span><br>'
        '<span style="font-size:17px; color:#555;">'
        'ai_gpt ↔ use_grade (0.490) 의 높은 상관관계로 인해 ai_gpt 제거 시 VIF 가 크게 낮아질 것으로 예상됩니다.'
        '</span>'
        '</div>'
        '</div>'

        '<div style="border-top:1px solid #ffe082; margin:4px 0;"></div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#f9a825; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:15px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">4</span>'
        '<div style="font-size:19px; line-height:2.0; color:#222;">'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px; font-weight:700; color:#e65100;">ai_gemi</span>'
        ' &nbsp; VIF <span style="font-weight:900; color:#1976d2;">3.53</span> &nbsp;'
        '<span style="background:#e3f2fd; border-radius:8px; padding:2px 10px; font-size:15px; font-weight:700; color:#1976d2;">문제 없음 ✔️</span><br>'
        '<span style="font-size:17px; color:#555;">'
        '모든 변수와 0.18 이하의 낮은 상관관계를 보여 다중공선성 문제가 없는 것으로 판단됩니다.'
        '</span>'
        '</div>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fce4ec,#f3e5f5);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:20px;'
        ' border-left:6px solid #e53935;">'
        '<div style="font-size:24px; font-weight:800; color:#b71c1c; margin-bottom:14px;">💡 조치 사항</div>'
        '<div style="font-size:19px; line-height:2.2; color:#222;">'
        'VIF 값이 가장 높은 '
        '<span style="background:#ffebee; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#e53935;">ai_gpt 제거</span>'
        ' 후 재분석을 진행합니다.<br>'
        '<span style="font-size:17px; color:#555;">'
        'ai_gpt ↔ use_grade (0.490), ai_gpt ↔ ai_query (0.361) 의 상관관계로 볼 때,'
        ' 챗GPT 사용빈도가 높은 학생은 성적향상 목적으로 AI를 사용하고 AI 질문 방법도 잘 아는 경향이 있습니다.<br>'
        '따라서 VIF 가 더 높고 다른 변수들과 더 많은 상관관계를 가진 '
        '<span style="background:#ffebee; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#e53935;">ai_gpt</span>'
        ' 를 제거하는 것이 통계적으로 적절합니다.'
        '</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)

    img_path5 = os.path.join(pages_folder, "logit_5.jpg")
    if os.path.exists(img_path5):
        st.image(img_path5, use_container_width=True)
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e8f5e9,#e0f7fa);'
            ' border-radius:16px; padding:28px 36px; margin-top:16px;'
            ' border-left:6px solid #26a69a;">'
            '<div style="font-size:22px; font-weight:800; color:#00695c; margin-bottom:20px;">✅ ai_gpt 제거 후 결과</div>'

            '<div style="display:flex; flex-direction:column; gap:12px; margin-bottom:20px;">'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="font-size:17px; font-weight:700; color:#555; min-width:90px;">ai_query</span>'
            '<span style="font-size:17px; color:#e53935; font-weight:700;">12.14</span>'
            '<span style="font-size:17px; color:#555;">→</span>'
            '<span style="font-size:17px; color:#1976d2; font-weight:700;">7.44</span>'
            '<span style="font-size:17px; color:#26a69a; font-weight:700;">✔ 정상</span>'
            '</div>'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="font-size:17px; font-weight:700; color:#555; min-width:90px;">ai_gemi</span>'
            '<span style="font-size:17px; color:#e53935; font-weight:700;">3.53</span>'
            '<span style="font-size:17px; color:#555;">→</span>'
            '<span style="font-size:17px; color:#1976d2; font-weight:700;">3.38</span>'
            '<span style="font-size:17px; color:#26a69a; font-weight:700;">✔ 정상</span>'
            '</div>'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="font-size:17px; font-weight:700; color:#555; min-width:90px;">use_grade</span>'
            '<span style="font-size:17px; color:#e53935; font-weight:700;">8.33</span>'
            '<span style="font-size:17px; color:#555;">→</span>'
            '<span style="font-size:17px; color:#1976d2; font-weight:700;">6.29</span>'
            '<span style="font-size:17px; color:#26a69a; font-weight:700;">✔ 정상</span>'
            '</div>'

            '</div>'

            '<div style="border-top:1px solid #b2dfdb; padding-top:16px;">'
            '<div style="font-size:19px; font-weight:800; color:#00695c; line-height:1.8;">'
            '🎯 모든 변수 VIF 10 미만 &nbsp;→&nbsp; <span style="color:#e53935;">다중공선성 해소!</span><br>'
            '<span style="font-size:17px; font-weight:600; color:#555;">'
            '최종 분석 변수 : ai_query &nbsp;·&nbsp; ai_gemi &nbsp;·&nbsp; use_grade'
            '</span>'
            '</div>'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("logit_5.jpg 파일을 pages 폴더에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 로지스틱 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.logistic_page == "로지스틱 회귀분석":

    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e53935,#ef9a9a);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#b71c1c;">로지스틱 회귀분석</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path6 = os.path.join(pages_folder, "logit_6.jpg")
    if os.path.exists(img_path6):
        st.image(img_path6, use_container_width=True)
        st.markdown('<div style="margin-bottom:16px;"></div>', unsafe_allow_html=True)

        # 카드 1 - 모델 적합도
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
            ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
            ' border-left:6px solid #1976d2;">'
            '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
            '<span style="font-size:20px; font-weight:800; color:#1565c0;">📊 모델 적합도 (Pseudo R-squared)</span>'
            '<span style="background:#1976d2; color:white; border-radius:20px;'
            ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">설명력 보통</span>'
            '</div>'
            '<div style="font-size:17px; line-height:2.0; color:#222;">'
            'Pseudo R² 값이 <span style="font-weight:900; color:#1976d2;">0.1641</span> 로,'
            ' 독립변수들이 윤리의식 여부 변동의 약 <span style="font-weight:900; color:#1976d2;">16.4%</span> 를 설명합니다.'
            ' 로지스틱 회귀분석에서 0.1 이상이면 의미 있는 설명력으로 판단합니다.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # 카드 2 - 모델 전체 유의성
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e8f5e9,#e0f7fa);'
            ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
            ' border-left:6px solid #26a69a;">'
            '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
            '<span style="font-size:20px; font-weight:800; color:#00695c;">🔍 모델 전체 유의성 (LLR p-value)</span>'
            '<span style="background:#26a69a; color:white; border-radius:20px;'
            ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">통계적으로 유의 ✔️</span>'
            '</div>'
            '<div style="font-size:17px; line-height:2.0; color:#222;">'
            'LLR p-value 가 <span style="font-weight:900; color:#26a69a;">1.333e-94</span> 로'
            ' 유의수준 0.05보다 매우 작으므로,'
            ' 이 로지스틱 회귀모델은 <span style="font-weight:700; color:#26a69a;">통계적으로 매우 유의</span>합니다.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # 카드 3 - 개별 변수 유의성
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
            ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
            ' border-left:6px solid #f9a825;">'
            '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
            '<span style="font-size:20px; font-weight:800; color:#e65100;">📌 개별 변수 유의성 (P-value)</span>'
            '</div>'
            '<div style="display:flex; flex-direction:column; gap:14px;">'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="background:#26a69a; color:white; border-radius:10px;'
            ' padding:4px 14px; font-size:15px; font-weight:700; min-width:90px; text-align:center;">ai_query</span>'
            '<span style="font-size:17px; color:#222; line-height:1.9;">'
            'P값 <span style="font-weight:900; color:#26a69a;">0.000</span> &nbsp;→&nbsp;'
            ' <span style="font-weight:700; color:#26a69a;">유의 ✔️</span> &nbsp;|&nbsp;'
            ' 계수 <span style="font-weight:700; color:#1976d2;">1.1018</span> —'
            ' AI 질문 능력이 높을수록 윤리의식이 높아질 확률 <b>증가</b>'
            '</span>'
            '</div>'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="background:#e53935; color:white; border-radius:10px;'
            ' padding:4px 14px; font-size:15px; font-weight:700; min-width:90px; text-align:center;">ai_gemi</span>'
            '<span style="font-size:17px; color:#222; line-height:1.9;">'
            'P값 <span style="font-weight:900; color:#e53935;">0.976</span> &nbsp;→&nbsp;'
            ' <span style="font-weight:700; color:#e53935;">유의하지 않음 ✖️</span> &nbsp;|&nbsp;'
            ' 제미나이 사용빈도는 윤리의식에 <b>영향 없음</b>'
            '</span>'
            '</div>'

            '<div style="display:flex; align-items:center; gap:16px;">'
            '<span style="background:#e53935; color:white; border-radius:10px;'
            ' padding:4px 14px; font-size:15px; font-weight:700; min-width:90px; text-align:center;">use_grade</span>'
            '<span style="font-size:17px; color:#222; line-height:1.9;">'
            'P값 <span style="font-weight:900; color:#e53935;">0.373</span> &nbsp;→&nbsp;'
            ' <span style="font-weight:700; color:#e53935;">유의하지 않음 ✖️</span> &nbsp;|&nbsp;'
            ' 성적향상 목적 AI 사용은 윤리의식에 <b>영향 없음</b>'
            '</span>'
            '</div>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

        # 카드 4 - 최종 결론
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fce4ec,#f3e5f5);'
            ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
            ' border-left:6px solid #e53935;">'
            '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
            '<span style="font-size:20px; font-weight:800; color:#b71c1c;">💡 최종 결론</span>'
            '<span style="background:#e53935; color:white; border-radius:20px;'
            ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">ai_query 만 유의</span>'
            '</div>'
            '<div style="font-size:17px; line-height:2.0; color:#222;">'
            '생성형 AI에 <b>질문하는 방법을 아는 것(ai_query)</b> 만이 윤리의식 여부에'
            ' <span style="font-weight:700; color:#e53935;">통계적으로 유의한 영향</span>을 미칩니다.<br>'
            'AI를 얼마나 자주 사용하느냐보다 <span style="font-weight:700; color:#e53935;">'
            'AI를 올바르게 활용하는 방법을 아는 것</span>이 윤리의식과 더 깊은 관련이 있습니다.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("logit_6.jpg 파일을 pages 폴더에 추가해 주세요.")
