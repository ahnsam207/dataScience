import streamlit as st
import streamlit.components.v1 as components
import os
import base64
import re
import subprocess

st.set_page_config(
    page_title="소개하기",
    page_icon="👩‍🏫",
    layout="wide"
)

st.markdown("""
<style>
:root {
    --label-color: #333;
    --date-color:  #666;
    --sub-color:   #555;
    --hr-color:    #e0e0e0;
}
@media (prefers-color-scheme: dark) {
    :root {
        --label-color: #e8e8e8;
        --date-color:  #aaaaaa;
        --sub-color:   #cccccc;
        --hr-color:    #444444;
    }
}
[data-theme="dark"] {
    --label-color: #e8e8e8;
    --date-color:  #aaaaaa;
    --sub-color:   #cccccc;
    --hr-color:    #444444;
}
.section-label-box {
    font-size: 14px;
    font-weight: 700;
    color: var(--label-color);
    line-height: 1.6;
    padding-top: 6px;
}
.section-subtitle {
    font-size: 12px;
    font-weight: 400;
    color: var(--sub-color);
    display: block;
    margin-top: 2px;
}
.section-date {
    font-size: 12px;
    font-weight: 400;
    color: var(--date-color);
    display: block;
    margin-top: 2px;
}
.section-hr {
    border: none;
    border-top: 1px solid var(--hr-color);
    margin: 4px 0 12px 0;
}
.title-name {
    margin: 0;
    font-size: 32px;
    font-weight: 800;
    color: var(--label-color);
}
</style>
""", unsafe_allow_html=True)

if "intro_page" not in st.session_state:
    st.session_state.intro_page = "2ok"

project_root   = os.path.dirname(os.path.abspath(__file__))
intro_folder   = os.path.join(project_root, "sam", "intro")


def img_to_base64(img_path):
    ext  = img_path.split(".")[-1].lower()
    mime = "image/png" if ext == "png" else "image/jpeg"
    with open(img_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return mime, b64


# ── 타이틀 ──────────────────────────────────────────
icon_path = os.path.join(intro_folder, "icon.PNG")
if os.path.exists(icon_path):
    mime, b64 = img_to_base64(icon_path)
    st.markdown(f"""
<div style="display:flex; align-items:center; gap:16px; margin-bottom:8px;">
    <img src="data:{mime};base64,{b64}"
         style="height:60px; width:auto; object-fit:contain;">
    <h1 class="title-name">안이옥 선생님</h1>
</div>""", unsafe_allow_html=True)
else:
    st.title("👩‍🏫 안이옥 선생님")

# ── 상단 메뉴 ──────────────────────────────────────
mc    = st.columns(2)
pages = ["2ok", "과제"]
icons = ["👩‍🏫", "📝"]
for col, page, icon in zip(mc, pages, icons):
    with col:
        if st.button(f"{icon} {page}", key=f"btn_{page}",
                     use_container_width=True,
                     type="primary" if st.session_state.intro_page == page else "secondary"):
            st.session_state.intro_page = page


# ══════════════════════════════════════════════════
# 2ok (기존 소개 내용)
# ══════════════════════════════════════════════════
if st.session_state.intro_page == "2ok":
    intro_img = os.path.join(intro_folder, "intro.jpg")
    if os.path.exists(intro_img):
        st.image(intro_img, use_container_width=True)
    else:
        st.markdown("""
<div style="background:linear-gradient(135deg,#a8edea 0%,#fed6e3 100%);
     border-radius:16px; padding:60px; text-align:center; margin:20px 0;">
    <div style="font-size:80px;">👩‍🏫</div>
</div>""", unsafe_allow_html=True)

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📋 기본 정보")
        st.markdown("""
| | |
|---|---|
| 👩‍🏫 | 안이옥 선생님 |
| 📚 | 정보 · 컴퓨터 교과 |
| 🏫 | 경복비즈니스고등학교 |
| 📧 | 2ok25@daum.net |
| ⏰ | 월-금 08:20 ~ 16:20 |
""")
    with col2:
        st.subheader("🏆 담당 교과")
        st.markdown("""
| | 교과명 |
|---|---|
| 🖨️ | 3D프린터제품제작 |
| 💻 | 프로그래밍 |
| 🔌 | 디지털논리회로 |
| 📱 | 스마트문화앱콘텐츠제작 |
| 📊 | 비즈니스엑셀 |
| 🗂️ | 기타 정보관련 교과 |
""")
    st.divider()
    st.subheader("💬 한마디")
    st.success("""
💡 ** 각자의 자리에서 치열하게 하루를 보내고, 밤늦게까지 데이터와 수식을 들여다보며 연구를 이어가는 동기 선생님들을 볼 때마다 큰 자극과 위로를 동시에 받습니다. 가끔은 정체기처럼 느껴져 답답할 때도 있지만, 우리가 지금까지 끈기 있게 분석하고 고민해 온 시간들은 결측치(NaN)로 dropna() 되지 않을 것이라 생각해요. 체력 관리 잘하면서 마지막까지 각자의 완성 모델을 성공적으로 배포(Deploy)하며 함께 완주했으면 좋겠습니다. 다들 파이팅입니다! 교수님, 올 PASS !!! 감사해요**

함께 새로운 기술을 배우고 멋진 결과물을 만들어 봐요.
궁금한 점이 있으면 언제든지 질문하세요. 언제나 응원합니다! 😊
""")
    st.divider()
    st.caption("© 2026 안이옥 선생님 소개 페이지")


# ══════════════════════════════════════════════════
# 과제
# ══════════════════════════════════════════════════
elif st.session_state.intro_page =