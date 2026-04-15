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
    "</style>",
    unsafe_allow_html=True
)

# ── 상단 메뉴 버튼 ──────────────────────────────────
mc    = st.columns([1, 1, 1, 1, 2])
tabs  = ["연구주제", "탐색적 데이터 분석", "다중공선성 확인", "회귀분석"]
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
    img_path = os.path.join(pages_folder, "ols_1.jpg")
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
        st.markdown(
            '<div style="font-size:15px; color:#666;'
            ' border-left:3px solid #bbb; padding:8px 14px; margin-top:8px;">'
            '📌 (데이터) 청소년의 생성형 AI 이용실태 및 리터러시 증진방안 연구.xlsx'
            '&nbsp;&nbsp;→&nbsp;&nbsp;'
            '<b>data.xlsx</b> 로 수정'
            '</div>',
            unsafe_allow_html=True
        )
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
        '생성형 AI를 사용한 경험 <span style="color:#1976d2; font-weight:700;">(Q4)</span> 이 있는 학생'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#1976d2; color:white; border-radius:50%; min-width:28px; height:28px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px;'
        ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '고등학생 <span style="color:#1976d2; font-weight:700;">(일반고, 특성화고)</span> 대상인 학생 데이터'
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
    else:
        st.info("ols_2.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('<div style="margin-bottom:40px;"></div>', unsafe_allow_html=True)

    # 03 - 선별 데이터 탐색적 데이터 분석하기
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#1976d2,#42a5f5);'
        ' color:white; border-radius:16px; padding:8px 20px;'
        ' font-size:28px; font-weight:900; letter-spacing:2px; flex-shrink:0;">03</div>'
        '<div style="font-size:28px; font-weight:800; color:#1565c0;">선별 데이터 탐색적 데이터 분석하기</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.info("선별 데이터 탐색적 데이터 분석하기 내용을 여기에 추가해 주세요.")

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
    st.info("상관계수 및 상관관계 확인하기 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 다중공선성 확인
# ══════════════════════════════════════════════════
elif st.session_state.linear_page == "다중공선성 확인":
    st.subheader("🔬 다중공선성 확인")
    st.divider()
    st.info("다중공선성 확인 내용을 여기에 추가해 주세요.")

# ══════════════════════════════════════════════════
# 회귀분석
# ══════════════════════════════════════════════════
elif st.session_state.linear_page == "회귀분석":
    st.subheader("📈 회귀분석")
    st.divider()
    st.info("회귀분석 내용을 여기에 추가해 주세요.")