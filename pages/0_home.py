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

st.markdown(
    "<style>"
    ":root { --label-color: #333; }"
    "@media (prefers-color-scheme: dark) { :root { --label-color: #e8e8e8; } }"
    "[data-theme='dark'] { --label-color: #e8e8e8; }"
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

if "intro_page" not in st.session_state:
    st.session_state.intro_page = "2ok"

# ── 상단 메뉴 버튼 ──────────────────────────────────
mc    = st.columns([1, 1, 4])
tabs  = ["2ok", "오늘의 과제"]
icons = ["👩‍🏫", "📝"]
for col, tab, icon in zip(mc[:2], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="btn_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.intro_page == tab else "secondary"
        ):
            st.session_state.intro_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════
# 2ok
# ══════════════════════════════════════════════════
if st.session_state.intro_page == "2ok":
    intro_img = os.path.join(pages_folder, "intro.jpg")
    if os.path.exists(intro_img):
        mime, b64 = img_to_base64(intro_img)
        st.markdown(
            '<div style="max-width:800px;">'
            '<img src="data:' + mime + ';base64,' + b64 + '"'
            ' style="width:100%; height:auto; border-radius:12px; display:block;">'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div style="max-width:800px; background:linear-gradient(135deg,#a8edea 0%,#fed6e3 100%);'
            ' border-radius:16px; padding:60px; text-align:center; margin:20px 0;">'
            '<div style="font-size:80px;">👩‍🏫</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📋 기본 정보")
        st.markdown(
            "| | |\n"
            "|---|---|\n"
            "| 👩‍🏫 | 안이옥 선생님 |\n"
            "| 📚 | 정보 · 컴퓨터 교과 |\n"
            "| 🏫 | 경복비즈니스고등학교 |\n"
            "| 📧 | 2ok25@daum.net |\n"
            "| ⏰ | 월-금 08:20 ~ 16:20 |"
        )
    with col2:
        st.subheader("🏆 담당 교과")
        st.markdown(
            "| | 교과명 |\n"
            "|---|---|\n"
            "| 🖨️ | 3D프린터제품제작 |\n"
            "| 💻 | 프로그래밍 |\n"
            "| 🔌 | 디지털논리회로 |\n"
            "| 📱 | 스마트문화앱콘텐츠제작 |\n"
            "| 📊 | 비즈니스엑셀 |\n"
            "| 🗂️ | 기타 정보관련 교과 |"
        )
    with col3:
        pass

    st.divider()
    st.subheader("💬 4기 파이팅!")
    st.markdown(
        '<div style="max-width:800px;">'
        '<div style="background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);'
        'border-radius:16px; padding:32px 36px; margin:12px 0; color:white;'
        'box-shadow:0 4px 20px rgba(102,126,234,0.4);">'
        '<div style="font-size:17px; line-height:2.2;">'
        '각자의 자리에서 치열하게 하루를 보내고, 밤늦게까지 데이터와 수식을 들여다보며 '
        '연구를 이어가는 동기 선생님들을 볼 때마다 큰 자극과 위로를 동시에 받습니다.'
        '</div>'
        '<div style="border-top:1px solid rgba(255,255,255,0.3); margin:18px 0;"></div>'
        '<div style="font-size:17px; line-height:2.2;">'
        '가끔은 정체기처럼 느껴져 답답할 때도 있지만, 우리가 지금까지 끈기 있게 분석하고 '
        '고민해 온 시간들은 결측치(NaN)로 <b>dropna()</b> 되지 않을 것이라 생각해요.'
        '</div>'
        '<div style="border-top:1px solid rgba(255,255,255,0.3); margin:18px 0;"></div>'
        '<div style="font-size:17px; line-height:2.2;">'
        '체력 관리 잘하면서 성공적으로 함께 완주했으면 좋겠습니다.'
        '</div>'
        '<div style="margin-top:24px; display:flex; gap:12px; flex-wrap:wrap;">'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🔥 다들 파이팅!</span>'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🎓 교수님 ALL PASS!!!</span>'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🙏 감사해요</span>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════
# 오늘의 과제
# ══════════════════════════════════════════════════
elif st.session_state.intro_page == "오늘의 과제":

    # 카드 1 - 프로젝트 목표
    st.markdown(
        '<div style="background:linear-gradient(135deg,#e0f7fa,#e8f5e9);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #26a69a;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:20px; color:#00695c;">🎯 프로젝트 목표</div>'
        '<div style="display:flex; flex-direction:column; gap:14px;">'
        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="color:#26a69a; font-size:22px; flex-shrink:0; margin-top:0px;">▪</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '연구 주제를 자유롭게 설정한 뒤 <b>다중선형 회귀분석</b> 또는 <b>로지스틱 회귀분석</b>을 적용하여 교육 데이터 분석을 수행'
        '</div>'
        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # 카드 2 - 프로젝트 진행
    st.markdown(
        '<div style="background:linear-gradient(135deg,#f3e5f5,#ede7f6);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #8e24aa;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:20px; color:#6a1b9a;">🔬 프로젝트 진행</div>'
        '<div style="display:flex; flex-direction:column; gap:16px;">'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '활용 가능한 데이터를 살펴보면서 관심이 가는 내용과 관련하여 <b>연구 문제 설정</b>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '데이터의 변수를 살펴보면서 <b>종속변수와 독립변수 설정</b>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:700; flex-shrink:0; margin-top:2px;">3</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '탐색적 데이터 분석 및 회귀분석 진행 <b>(ipynb 활용)</b>'
        '</div>'
        '</div>'

        '<div style="display:flex; align-items:flex-start; gap:14px;">'
        '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:30px; height:30px;'
        ' display:flex; align-items:center; justify-content:center; font-size:14px; font-weight:700; flex-shrink:0; margin-top:2px;">4</span>'
        '<div style="font-size:17px; line-height:1.9; color:#222;">'
        '분석 결과를 <b>Streamlit URL</b> 형태로 공유 및 발표'
        ' <span style="color:#8e24aa; font-weight:600;">(PPT 없이 발표하는 것을 권장)</span>'
        '</div>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # 카드 3 - 발표 내용
    st.markdown(
        '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #f9a825;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:20px; color:#e65100;">🎤 발표 내용</div>'
        '<div style="display:flex; flex-direction:column; gap:12px;">'

        '<div style="display:flex; align-items:center; gap:14px;">'
        '<span style="background:#f9a825; color:white; border-radius:10px;'
        ' padding:6px 18px; font-size:16px; font-weight:700; min-width:44px; text-align:center;">01</span>'
        '<span style="font-size:17px; color:#222; font-weight:500;">📂 활용한 데이터</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:14px;">'
        '<span style="background:#fb8c00; color:white; border-radius:10px;'
        ' padding:6px 18px; font-size:16px; font-weight:700; min-width:44px; text-align:center;">02</span>'
        '<span style="font-size:17px; color:#222; font-weight:500;">🔍 연구주제</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:14px;">'
        '<span style="background:#f4511e; color:white; border-radius:10px;'
        ' padding:6px 18px; font-size:16px; font-weight:700; min-width:44px; text-align:center;">03</span>'
        '<span style="font-size:17px; color:#222; font-weight:500;">⚙️ 분석 방법 및 과정</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:14px;">'
        '<span style="background:#e53935; color:white; border-radius:10px;'
        ' padding:6px 18px; font-size:16px; font-weight:700; min-width:44px; text-align:center;">04</span>'
        '<span style="font-size:17px; color:#222; font-weight:500;">📊 분석 결과</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:14px;">'
        '<span style="background:#8e24aa; color:white; border-radius:10px;'
        ' padding:6px 18px; font-size:16px; font-weight:700; min-width:44px; text-align:center;">05</span>'
        '<span style="font-size:17px; color:#222; font-weight:500;">💡 결과 해석 및 논의</span>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )