import streamlit as st
import os
import base64

st.set_page_config(page_title="시작하기", page_icon="👩‍🏫", layout="wide")

st.markdown(
    "<style>"
    ":root { --label-color: #333; --hr-color: #e0e0e0; }"
    "@media (prefers-color-scheme: dark) {"
    "  :root { --label-color: #e8e8e8; --hr-color: #444444; }"
    "}"
    "[data-theme='dark'] { --label-color: #e8e8e8; --hr-color: #444444; }"
    ".title-name { margin: 0; font-size: 32px; font-weight: 800; color: var(--label-color); }"
    "</style>",
    unsafe_allow_html=True
)

if "intro_page" not in st.session_state:
    st.session_state.intro_page = "2ok"

project_root = os.path.dirname(os.path.abspath(__file__))
pages_folder = os.path.join(project_root, "pages")

def img_to_base64(img_path):
    ext  = img_path.split(".")[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return mime, b64

# ── 타이틀 ──────────────────────────────────────────
icon_path = os.path.join(pages_folder, "icon.PNG")
if os.path.exists(icon_path):
    mime, b64 = img_to_base64(icon_path)
    st.markdown(
        '<div style="display:flex; align-items:center; gap:16px; margin-bottom:8px;">'
        '<img src="data:' + mime + ';base64,' + b64 + '"'
        ' style="height:60px; width:auto; object-fit:contain;">'
        '<h1 class="title-name">안이옥 선생님</h1>'
        '</div>',
        unsafe_allow_html=True
    )
else:
    st.title("👩‍🏫 안이옥 선생님")

# ── 상단 메뉴 ──────────────────────────────────────
mc    = st.columns(2)
pages = ["2ok", "과제"]
icons = ["👩‍🏫", "📝"]
for col, page, icon in zip(mc, pages, icons):
    with col:
        if st.button(
            icon + " " + page,
            key="btn_" + page,
            use_container_width=True,
            type="primary" if st.session_state.intro_page == page else "secondary"
        ):
            st.session_state.intro_page = page

# ══════════════════════════════════════════════════
# 2ok
# ══════════════════════════════════════════════════
if st.session_state.intro_page == "2ok":
    intro_img = os.path.join(pages_folder, "intro.jpg")
    if os.path.exists(intro_img):
        st.image(intro_img, use_container_width=True)
    else:
        st.markdown(
            '<div style="background:linear-gradient(135deg,#a8edea 0%,#fed6e3 100%);'
            ' border-radius:16px; padding:60px; text-align:center; margin:20px 0;">'
            '<div style="font-size:80px;">👩‍🏫</div>'
            '</div>',
            unsafe_allow_html=True
        )

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
        '고민해 온 시간들은 결측치(NaN)로 <code style="background:rgba(255,255,255,0.2);'
        'padding:2px 8px; border-radius:4px; font-size:15px;">dropna()</code> 되지 않을 것이라 생각해요.'
        '</div>'
        '<div style="border-top: 1px solid rgba(255,255,255,0.3); margin: 18px 0;"></div>'
        '<div style="font-size:17px; line-height:2.2; font-weight:400;">'
        '체력 관리 잘하면서 마지막까지 각자의 완성 모델을 성공적으로 '
        '<code style="background:rgba(255,255,255,0.2); padding:2px 8px; border-radius:4px; font-size:15px;">'
        'Deploy()</code> 하며 함께 완주했으면 좋겠습니다.'
        '</div>'
        '<div style="margin-top:24px; display:flex; gap:12px; flex-wrap:wrap;">'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🔥 다들 파이팅!</span>'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🎓 교수님 올 PASS!!!</span>'
        '<span style="background:rgba(255,255,255,0.25); border-radius:20px;'
        ' padding:6px 16px; font-size:15px; font-weight:700;">🙏 감사해요</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.divider()
    st.caption("© 2026 안이옥 선생님 소개 페이지")

# ══════════════════════════════════════════════════
# 과제
# ══════════════════════════════════════════════════
elif st.session_state.intro_page == "과제":
    st.header("📝 과제")
    st.divider()
    st.info("과제 내용을 여기에 추가해 주세요.")