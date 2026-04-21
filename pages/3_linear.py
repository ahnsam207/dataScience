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

if "linear_page" not in st.session_state:
    st.session_state.linear_page = "연구주제"

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
    "  background: linear-gradient(135deg, #1976d2, #42a5f5);"
    "  color: white;"
    "  border: none;"
    "  border-radius: 50px;"
    "  padding: 12px 22px;"
    "  font-size: 16px;"
    "  font-weight: 800;"
    "  cursor: pointer;"
    "  box-shadow: 0 4px 16px rgba(25,118,210,0.4);"
    "  z-index: 9999;"
    "  text-decoration: none;"
    "}"
    ".top-btn:hover { background: linear-gradient(135deg,#1565c0,#1976d2); }"
    "</style>",
    unsafe_allow_html=True
)

st.markdown('<div id="top-anchor"></div>', unsafe_allow_html=True)

# ── 상단 메뉴 버튼 ──────────────────────────────────
mc    = st.columns([2, 2, 2, 2, 1])
tabs  = ["연구주제", "탐색적 데이터 분석", "다중공선성 확인", "다중 선형 회귀분석"]
icons = ["🔍", "📊", "🔬", "📈"]
for col, tab, icon in zip(mc[:4], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="linear_tab_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.linear_page == tab else "secondary"
        ):
            st.session_state.linear_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)
st.divider()

# ══════════════════════════════════════════════════
# 연구주제
# ══════════════════════════════════════════════════
if st.session_state.linear_page == "연구주제":

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
# 탐색적 데이터 분석
# ══════════════════════════════════════════════════
elif st.session_state.linear_page == "탐색적 데이터 분석":

    # 01 - 데이터 불러오기 및 정보 확인
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">데이터 불러오기 및 정보 확인</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:12px; padding:20px 28px; margin-bottom:16px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="display:flex; align-items:center; gap:12px;">'
        '<span style="font-size:20px;">📌</span>'
        '<div style="font-size:17px; color:#222; line-height:1.9;">'
        '(데이터) 청소년의 생성형 AI 이용실태 및 리터러시 증진방안 연구.xlsx'
        ' &nbsp;<span style="color:#555;">→</span>&nbsp; '
        '<span style="font-weight:700; color:#1976d2;">data.xlsx</span> 로 수정'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path1 = os.path.join(pages_folder, "ols_1.jpg")
    if os.path.exists(img_path1):
        st.image(img_path1, use_container_width=True)
    else:
        st.info("ols_1.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:40px;"></div>', unsafe_allow_html=True)

    # 02 - 분석 대상 데이터만 가져오기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">02</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">분석 대상 데이터만 가져오기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:20px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="display:flex; flex-direction:column; gap:14px;">'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#1976d2; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI를 사용한 경험 <span style="color:#1976d2; font-weight:700;">(Q4)</span> 이 있는 학생과'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#1976d2; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '일반고 <span style="color:#1976d2; font-weight:700;">(SQ0_3 = 2)</span>,'
        ' 특성화고 <span style="color:#1976d2; font-weight:700;">(SQ0_3 = 5)</span>'
        ' 학생 데이터 중에서'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#1976d2; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">3</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI의 사용목적이 숙제 <span style="color:#1976d2; font-weight:700;">(Q9_5)</span>, '
        '성적 향상 <span style="color:#1976d2; font-weight:700;">(Q9_6)</span> 인 데이터'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#1976d2; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">4</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '생성형 AI의 평균사용시간 <span style="color:#1976d2; font-weight:700;">(Q7)</span>, '
        '학업 성적 <span style="color:#1976d2; font-weight:700;">(DQ3)</span> 데이터만 가져오기'
        '</div>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path2 = os.path.join(pages_folder, "ols_2.jpg")
    if os.path.exists(img_path2):
        st.image(img_path2, use_container_width=True)
        st.markdown(
            '<div style="background:linear-gradient(135deg,#1a237e,#283593);'
            ' border-radius:16px; padding:28px 36px; margin-top:20px;">'

            '<div style="background:rgba(255,255,255,0.1); border-radius:12px; padding:20px 24px; margin-bottom:16px;">'
            '<div style="font-size:18px; font-weight:800; color:#ffeb3b; margin-bottom:10px;">🤔 질문</div>'
            '<div style="font-size:17px; line-height:1.9; color:white;">'
            '다중 선형 회귀분석의 종속 변수가 <span style="color:#ffeb3b; font-weight:700;">"1, 2, 3, 4, 5"</span>'
            ' 의 범주형 값을 갖는데 분석이 가능한가?'
            '</div>'
            '</div>'

            '<div style="background:rgba(255,255,255,0.1); border-radius:12px; padding:20px 24px; margin-bottom:16px;">'
            '<div style="font-size:18px; font-weight:800; color:#69f0ae; margin-bottom:10px;">✅ 답안</div>'
            '<div style="font-size:17px; line-height:1.9; color:white;">'
            '1, 2, 3, 4, 5 의 값은 엄밀히는 범주형이지만, '
            '<span style="color:#69f0ae; font-weight:700;">리커트 척도(Likert Scale)</span>'
            ' 처럼 등간성을 가정할 수 있는 경우에는 연속형 변수로 간주할 수 있습니다.<br>'
            '또한 <span style="color:#69f0ae; font-weight:700;">표본의 크기가 충분히 클 때</span>'
            ' 중심극한정리에 의해 정규성 가정이 완화되므로,'
            ' 다중 선형 회귀분석을 적용하는 것이 통계적으로 허용됩니다.'
            '</div>'
            '</div>'

            '<div style="background:rgba(255,255,255,0.07); border-radius:12px; padding:20px 24px; margin-bottom:16px;">'
            '<div style="font-size:18px; font-weight:800; color:#80d8ff; margin-bottom:10px;">📖 등간성이란?</div>'
            '<div style="font-size:16px; line-height:1.9; color:#cfd8dc;">'
            '등간성(等間性, Equal Interval)이란 척도의 각 단계 간 간격이 동일하다는 가정입니다.<br>'
            '예를 들어 <span style="color:#80d8ff; font-weight:700;">"1→2"의 차이</span>와 '
            '<span style="color:#80d8ff; font-weight:700;">"4→5"의 차이</span>가 심리적·통계적으로 동일하다고 볼 수 있을 때,'
            ' 해당 변수를 연속형으로 처리할 수 있습니다.<br>'
            '학업 성적(DQ3)처럼 순서 간격이 균등하다고 가정 가능한 경우 다중 선형 회귀분석 적용이 허용됩니다.'
            '</div>'
            '</div>'

            '<div style="background:rgba(255,255,255,0.07); border-radius:12px; padding:20px 24px;">'
            '<div style="font-size:18px; font-weight:800; color:#ffd180; margin-bottom:10px;">📖 중심극한정리란?</div>'
            '<div style="font-size:16px; line-height:1.9; color:#cfd8dc;">'
            '중심극한정리(中心極限定理, Central Limit Theorem)란 모집단의 분포 형태와 관계없이,'
            ' <span style="color:#ffd180; font-weight:700;">표본의 크기가 충분히 크면(일반적으로 n ≥ 30)</span>'
            ' 표본 평균의 분포가 정규분포에 가까워진다는 통계학의 핵심 정리입니다.<br>'
            '즉, 원래 데이터가 정규분포를 따르지 않더라도 표본이 크면 회귀분석의 정규성 가정을 완화할 수 있으며,'
            ' 본 연구의 표본 수는 <span style="color:#ffd180; font-weight:700;">1,952명</span> 으로'
            ' 충분히 크기 때문에 다중 선형 회귀분석 적용이 가능합니다.'
            '</div>'
            '</div>'

            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("ols_2.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:40px;"></div>', unsafe_allow_html=True)

    # 03 - 선별 데이터 변수명 수정하고 데이터 분석하기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">03</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">선별 데이터 변수명 수정하고 데이터 분석하기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:12px; padding:20px 28px; margin-bottom:16px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="font-size:16px; font-weight:800; color:#1565c0; margin-bottom:14px;">📝 변수명 수정</div>'
        '<div style="display:flex; flex-wrap:wrap; gap:12px;">'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 16px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:15px; color:#e53935; font-weight:700;">Q9_5</span>'
        '<span style="font-size:15px; color:#555; margin:0 4px;">→</span>'
        '<span style="font-size:15px; color:#1976d2; font-weight:700;">use_hw</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 16px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:15px; color:#e53935; font-weight:700;">Q9_6</span>'
        '<span style="font-size:15px; color:#555; margin:0 4px;">→</span>'
        '<span style="font-size:15px; color:#1976d2; font-weight:700;">use_grade</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 16px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:15px; color:#e53935; font-weight:700;">Q7</span>'
        '<span style="font-size:15px; color:#555; margin:0 4px;">→</span>'
        '<span style="font-size:15px; color:#1976d2; font-weight:700;">avg_time</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 16px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:15px; color:#e53935; font-weight:700;">DQ3</span>'
        '<span style="font-size:15px; color:#555; margin:0 4px;">→</span>'
        '<span style="font-size:15px; color:#1976d2; font-weight:700;">score</span>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path3 = os.path.join(pages_folder, "ols_3.jpg")
    if os.path.exists(img_path3):
        st.image(img_path3, use_container_width=True)
    else:
        st.info("ols_3.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e8f5e9,#e0f7fa);'
        ' border-radius:12px; padding:20px 28px; margin-top:16px; margin-bottom:40px;'
        ' border-left:6px solid #26a69a;">'
        '<div style="display:flex; flex-wrap:wrap; gap:12px;">'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 18px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:18px;">✅</span>'
        '<span style="font-size:16px; font-weight:700; color:#00695c;">결측치 없음</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 18px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:18px;">✅</span>'
        '<span style="font-size:16px; font-weight:700; color:#00695c;">이상치 없음</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:8px; background:white;'
        ' border-radius:10px; padding:8px 18px; box-shadow:0 1px 4px rgba(0,0,0,0.1);">'
        '<span style="font-size:18px;">✅</span>'
        '<span style="font-size:16px; font-weight:700; color:#00695c;">종속변수의 데이터가 리커트 척도 값(1,2,3,4,5)으로 Scaling과 Label Encoding 필요 없음</span>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">'
        '<span style="font-size:18px;">🔎</span>'
        '<span style="font-size:20px; font-weight:800; color:#1565c0;">이상치 확인</span>'
        '</div>',
        unsafe_allow_html=True
    )

    outlier_img = os.path.join(pages_folder, "outlier.jpg")
    if os.path.exists(outlier_img):
        st.image(outlier_img, use_container_width=True)
    else:
        st.info("outlier.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:40px;"></div>', unsafe_allow_html=True)

    # 04 - 상관계수 및 상관관계 확인하기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">04</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">상관계수 및 상관관계 확인하기</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path4 = os.path.join(pages_folder, "ols_4.jpg")
    if os.path.exists(img_path4):
        st.image(img_path4, use_container_width=True)
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
            ' border-radius:12px; padding:20px 28px; margin-top:16px;'
            ' border-left:6px solid #f9a825;">'
            '<div style="font-size:22px; font-weight:800; color:#e65100; margin-bottom:12px;">🔍 분석 결과</div>'
            '<div style="font-size:22px; line-height:2.0; color:#222;">'
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#e65100;">use_hw</span>'
            ' <span style="color:#888; font-size:22px;">(생성형 인공지능을 사용하는 목적이 학교 숙제)</span>'
            ' 와 '
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#e65100;">use_grade</span>'
            ' <span style="color:#888; font-size:22px;">(생성형 인공지능을 사용하는 목적이 학교 성적 향상)</span>'
            '</div>'
            '<div style="font-size:22px; line-height:2.0; color:#222; margin-top:8px;">'
            '변수 간 상관계수가 '
            '<span style="font-size:22px; font-weight:900; color:#e53935;">0.83</span>'
            ' 으로 <b>강한 양의 상관관계</b>가 있음을 확인할 수 있음.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("ols_4.jpg 파일을 pages 폴더에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 다중공선성 확인
# ══════════════════════════════════════════════════
elif st.session_state.linear_page == "다중공선성 확인":

    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">다중공선성 확인</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path5 = os.path.join(pages_folder, "ols_5.jpg")
    if os.path.exists(img_path5):
        st.image(img_path5, use_container_width=True)
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
            ' border-radius:12px; padding:20px 28px; margin-top:16px;'
            ' border-left:6px solid #f9a825;">'
            '<div style="font-size:24px; font-weight:800; color:#e65100; margin-bottom:12px;">🔍 분석 결과</div>'
            '<div style="font-size:22px; line-height:2.0; color:#222;">'
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#e65100;">use_hw</span>'
            ' 와 '
            '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#e65100;">use_grade</span>'
            ' 변수의 상관계수가 높고 다중공선성 수치가 높은 것으로 볼 때,'
            '</div>'
            '<div style="font-size:22px; line-height:2.0; color:#222; margin-top:8px;">'
            '숙제를 위해 AI를 사용하는 학생이 성적향상을 위해 AI를 사용하는 학생일 확률이 높다는 결론으로'
            '</div>'
            '<div style="font-size:22px; line-height:2.0; color:#222; margin-top:8px;">'
            '다중공선성 수치가 더 높은 '
            '<span style="background:#ffebee; border-radius:8px; padding:2px 10px;'
            ' font-weight:700; color:#e53935;">use_hw 제거</span>'
            ' 하기로 함.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("ols_5.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:60px;"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">02</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">최종 분석 데이터</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path6 = os.path.join(pages_folder, "ols_6.jpg")
    if os.path.exists(img_path6):
        st.image(img_path6, use_container_width=True)
    else:
        st.info("ols_6.jpg 파일을 pages 폴더에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 다중 선형 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.linear_page == "다중 선형 회귀분석":

    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">01</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">다중 선형 회귀분석</div>'
        '</div>',
        unsafe_allow_html=True
    )

    img_path7 = os.path.join(pages_folder, "ols_7.jpg")
    if os.path.exists(img_path7):
        st.image(img_path7, use_container_width=True)
    else:
        st.info("ols_7.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:60px;"></div>', unsafe_allow_html=True)

    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">02</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">결과 해석</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
        '<span style="font-size:20px; font-weight:800; color:#1565c0;">📊 모델 적합도 (R-squared)</span>'
        '<span style="background:#e53935; color:white; border-radius:20px;'
        ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">설명력 매우 낮음</span>'
        '</div>'
        '<div style="font-size:17px; line-height:2.0; color:#222;">'
        'R² 값이 <span style="font-weight:700; color:#e53935;">0.001 (0.1%)</span> 으로'
        ' 모델의 설명력이 매우 낮음'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fce4ec,#f3e5f5);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #e53935;">'
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
        '<span style="font-size:20px; font-weight:800; color:#b71c1c;">🔍 모델 전체 유의성 (F-statistic)</span>'
        '<span style="background:#e53935; color:white; border-radius:20px;'
        ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">유의하지 않음</span>'
        '</div>'
        '<div style="font-size:17px; line-height:2.0; color:#222;">'
        'F-통계량의 유의확률(p값)이 <span style="font-weight:700; color:#e53935;">0.443</span> 으로'
        ' 회귀모델이 통계적으로 유의하지 않음'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#f3e5f5,#ede7f6);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #8e24aa;">'
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
        '<span style="font-size:20px; font-weight:800; color:#6a1b9a;">📌 개별 변수 유의성 (P-value)</span>'
        '<span style="background:#e53935; color:white; border-radius:20px;'
        ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">두 변수 모두 유의하지 않음</span>'
        '</div>'
        '<div style="font-size:17px; line-height:2.0; color:#222;">'
        '<span style="background:#ede7f6; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#8e24aa;">use_grade</span>'
        ' 의 P값은 <span style="font-weight:700; color:#e53935;">0.378</span>,'
        ' <span style="background:#ede7f6; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#8e24aa;">avg_time</span>'
        ' 의 P값은 <span style="font-weight:700; color:#e53935;">0.474</span> 로,'
        ' 두 변수 모두 통계적으로 유의하지 않음'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #f9a825;">'
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
        '<span style="font-size:20px; font-weight:800; color:#e65100;">📈 회귀계수 해석</span>'
        '<span style="background:#f9a825; color:white; border-radius:20px;'
        ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">영향력 매우 미미</span>'
        '</div>'
        '<div style="font-size:17px; line-height:2.0; color:#222;">'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#e65100;">use_grade</span>'
        ' 의 계수는 <span style="font-weight:700; color:#1976d2;">0.014</span> 로,'
        ' 성적 향상 목적의 AI 사용이 1단위 증가할 때 학업 성적이 0.014 증가하지만 유의하지 않음<br>'
        '<span style="background:#fff3e0; border-radius:8px; padding:2px 10px;'
        ' font-weight:700; color:#e65100;">avg_time</span>'
        ' 의 계수는 <span style="font-weight:700; color:#1976d2;">0.014</span> 로,'
        ' AI 평균 사용시간이 1단위 증가할 때 학업 성적이 0.014 증가하지만 역시 유의하지 않음'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e8f5e9,#e0f7fa);'
        ' border-radius:16px; padding:28px 36px; margin-bottom:16px;'
        ' border-left:6px solid #26a69a;">'
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">'
        '<span style="font-size:20px; font-weight:800; color:#00695c;">💡 최종 결론</span>'
        '<span style="background:#26a69a; color:white; border-radius:20px;'
        ' padding:4px 16px; font-size:15px; font-weight:700; flex-shrink:0;">AI 사용이 학업 성적에 유의한 영향 없음</span>'
        '</div>'
        '<div style="font-size:17px; line-height:2.0; color:#222;">'
        '생성형 AI의 사용목적(성적 향상)과 평균 사용시간은'
        ' 고등학생의 학업 성적에 <span style="font-weight:700; color:#e53935;">통계적으로 유의한 영향을 미치지 않는 것</span>'
        ' 으로 나타났습니다.<br>'
        '즉, 생성형 AI 사용이 직접적으로 학업 성적 향상으로 이어진다고 보기 어려우며,'
        ' 학업 성적에 영향을 미치는 다른 요인들을 추가로 고려할 필요가 있습니다.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ── TOP 버튼 ──────────────────────────────────────
st.markdown(
    '<a href="#top-anchor" class="top-btn">▲ TOP</a>',
    unsafe_allow_html=True
)
