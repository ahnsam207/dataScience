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
    "  padding-top: 1rem !important;"
    "  padding-left: 2rem !important;"
    "  padding-right: 2rem !important;"
    "}"
    "div[data-testid='stHorizontalBlock'] button {"
    "  height: 3rem !important;"
    "  font-size: 18px !important;"
    "  font-weight: 700 !important;"
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

st.markdown('<div style="margin-bottom:12px;"></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════
# 2ok
# ══════════════════════════════════════════════════
if st.session_state.intro_page == "2ok":
    st.markdown(
        "<style>"
        ".content-2ok { max-width: 800px; }"
        "</style>",
        unsafe_allow_html=True
    )

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

    st.markdown('<div style="max-width:800px;">', unsafe_allow_html=True)
    st.divider()
    col1, col2 = st.columns(2)
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

    st.divider()
    st.subheader("💬 4기 파이팅!")
    st.markdown(
        '<div style="max-width:800px;">'
        '<div style="'
        'background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);'
        'border-radius: 16px; padding: 32px 36px; margin: 12px 0; color: white;'
        'box-shadow: 0 4px 20px rgba(102,126,234,0.4);">'
        '<div style="font-size:17px; line-height:2.2; font-weight:400;">'
        '각자의 자리에서 치열하게 하루를 보내고, 밤늦게까지 데이터와 수식을 들여다보며 '
        '연구를 이어가는 동기 선생님들을 볼 때마다 큰 자극과 위로를 동시에 받습니다.'
        '</div>'
        '<div style="border-top: 1px solid rgba(255,255,255,0.3); margin: 18px 0;"></div>'
        '<div style="font-size:17px; line-height:2.2; font-weight:400;">'
        '가끔은 정체기처럼 느껴져 답답할 때도 있지만, 우리가 지금까지 끈기 있게 분석하고 '
        '고민해 온 시간들은 결측치(NaN)로 <b>dropna()</b> 되지 않을 것이라 생각해요.'
        '</div>'
        '<div style="border-top: 1px solid rgba(255,255,255,0.3); margin: 18px 0;"></div>'
        '<div style="font-size:17px; line-height:2.2; font-weight:400;">'
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
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════
# 오늘의 과제
# ══════════════════════════════════════════════════
elif st.session_state.intro_page == "오늘의 과제":
    st.subheader("📝 오늘의 과제")
    st.divider()

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e0f7fa,#e8f5e9);'
            ' border-radius:14px; padding:24px; height:100%;'
            ' border-top: 5px solid #26a69a;">'
            '<div style="font-size:16px; font-weight:800; margin-bottom:14px; color:#00695c;">🎯 프로젝트 목표</div>'
            '<div style="font-size:14px; line-height:2.0; color:#333;">'
            '연구 주제를 자유롭게 설정한 뒤<br>'
            '<b>다중선형 회귀분석</b> 또는<br>'
            '<b>로지스틱 회귀분석</b>을 적용하여<br>'
            '교육 데이터 분석을 수행합니다.'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#f3e5f5,#ede7f6);'
            ' border-radius:14px; padding:24px; height:100%;'
            ' border-top: 5px solid #8e24aa;">'
            '<div style="font-size:16px; font-weight:800; margin-bottom:14px; color:#6a1b9a;">🔬 프로젝트 진행</div>'
            '<div style="display:flex; flex-direction:column; gap:10px;">'

            '<div style="display:flex; align-items:flex-start; gap:8px; font-size:14px; line-height:1.7; color:#333;">'
            '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:22px; height:22px;'
            ' display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; margin-top:1px;">1</span>'
            '<span>활용 가능한 데이터에서 <b>연구 문제 설정</b></span>'
            '</div>'

            '<div style="display:flex; align-items:flex-start; gap:8px; font-size:14px; line-height:1.7; color:#333;">'
            '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:22px; height:22px;'
            ' display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; margin-top:1px;">2</span>'
            '<span><b>종속변수 · 독립변수</b> 설정</span>'
            '</div>'

            '<div style="display:flex; align-items:flex-start; gap:8px; font-size:14px; line-height:1.7; color:#333;">'
            '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:22px; height:22px;'
            ' display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; margin-top:1px;">3</span>'
            '<span>탐색적 데이터 분석 및 회귀분석 진행 <b>(ipynb)</b></span>'
            '</div>'

            '<div style="display:flex; align-items:flex-start; gap:8px; font-size:14px; line-height:1.7; color:#333;">'
            '<span style="background:#8e24aa; color:white; border-radius:50%; min-width:22px; height:22px;'
            ' display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; margin-top:1px;">4</span>'
            '<span><b>Streamlit URL</b>로 공유 및 발표<br><small>(PPT 없이 발표 권장)</small></span>'
            '</div>'

            '</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with col_c:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#fff8e1,#fff3e0);'
            ' border-radius:14px; padding:24px; height:100%;'
            ' border-top: 5px solid #f9a825;">'
            '<div style="font-size:16px; font-weight:800; margin-bottom:14px; color:#e65100;">🎤 발표 내용</div>'
            '<div style="display:flex; flex-direction:column; gap:8px;">'
            '<div style="background:#f9a825; color:white; border-radius:10px;'
            ' padding:8px 14px; font-size:14px; font-weight:600;">📂 활용한 데이터</div>'
            '<div style="background:#fb8c00; color:white; border-radius:10px;'
            ' padding:8px 14px; font-size:14px; font-weight:600;">🔍 연구주제</div>'
            '<div style="background:#f4511e; color:white; border-radius:10px;'
            ' padding:8px 14px; font-size:14px; font-weight:600;">⚙️ 분석 방법 및 과정</div>'
            '<div style="background:#e53935; color:white; border-radius:10px;'
            ' padding:8px 14px; font-size:14px; font-weight:600;">📊 분석 결과</div>'
            '<div style="background:#8e24aa; color:white; border-radius:10px;'
            ' padding:8px 14px; font-size:14px; font-weight:600;">💡 결과 해석 및 논의</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )