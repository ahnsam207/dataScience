import streamlit as st
import streamlit.components.v1 as components
import os
import base64

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

project_root = os.path.dirname(os.path.abspath(__file__))
intro_folder = os.path.join(project_root, "sam", "intro")


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
# 2ok
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
| 👩‍�