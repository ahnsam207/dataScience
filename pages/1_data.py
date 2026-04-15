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

if "data_page" not in st.session_state:
    st.session_state.data_page = "출처"

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
mc    = st.columns([1, 1, 1, 3])
tabs  = ["출처", "찾아보기", "미리보기"]
icons = ["📂", "🔍", "👀"]
for col, tab, icon in zip(mc[:3], tabs, icons):
    with col:
        if st.button(
            icon + "  " + tab,
            key="btn_data_" + tab,
            use_container_width=True,
            type="primary" if st.session_state.data_page == tab else "secondary"
        ):
            st.session_state.data_page = tab

st.markdown('<div style="margin-bottom:20px;"></div>', unsafe_allow_html=True)
st.divider()

if st.session_state.data_page == "출처":

    st.markdown(
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:24px; color:#1565c0;">📂 데이터 출처</div>'
        '<div style="display:flex; flex-direction:column; gap:16px;">'

        '<div style="display:flex; align-items:center; gap:16px;">'
        '<span style="font-size:15px; font-weight:700; color:#1976d2; min-width:80px;">📌 사이트명</span>'
        '<span style="font-size:17px; color:#222;">한국 아동·청소년·청년 데이터 아카이브</span>'
        '</div>'

        '<div style="display:flex; align-items:center; gap:16px;">'
        '<span style="font-size:15px; font-weight:700; color:#1976d2; min-width:80px;">🔗 URL</span>'
        '<a href="https://www.nypi.re.kr/archive/mps" target="_blank"'
        ' style="font-size:17px; color:#1976d2; text-decoration:underline;">'
        'https://www.nypi.re.kr/archive/mps'
        '</a>'
        '</div>'

        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div></div>', unsafe_allow_html=True)  # 기존 카드 닫기

    st.markdown('<div style="margin-bottom:24px;"></div>', unsafe_allow_html=True)

    st.link_button(
        "🌐  사이트 접속하기",
        "https://www.nypi.re.kr/archive/mps",
        use_container_width=False
    )

    cite_img = os.path.join(pages_folder, "cite.jpg")
    if os.path.exists(cite_img):
        mime, b64 = img_to_base64(cite_img)
        st.markdown(
            '<div style="margin-top:16px;">'
            '<img src="data:' + mime + ';base64,' + b64 + '"'
            ' style="width:100%; height:auto; border-radius:10px; display:block;">'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("cite.jpg 파일을 pages 폴더에 추가해 주세요.")

elif st.session_state.data_page == "찾아보기":

    images = [
        ("link.jpg",     "① 다운로드 메뉴"),
        ("agree.jpg",    "② 동의 및 선택"),
        ("download.jpg", "③ 다운로드"),
    ]

    for filename, title in images:
        img_path = os.path.join(pages_folder, filename)
        st.markdown(
            '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
            ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
            ' border-left:6px solid #1976d2;">'
            '<div style="font-size:22px; font-weight:800; margin-bottom:20px; color:#1565c0;">'
            + title +
            '</div>',
            unsafe_allow_html=True
        )
        if os.path.exists(img_path):
            mime, b64 = img_to_base64(img_path)
            st.markdown(
                '<img src="data:' + mime + ';base64,' + b64 + '"'
                ' style="width:100%; height:auto; border-radius:10px; display:block;">'
                '</div>',
                unsafe_allow_html=True
            )
        else:
            st.info(filename + " 파일을 pages 폴더에 추가해 주세요.")
            st.markdown('</div>', unsafe_allow_html=True)