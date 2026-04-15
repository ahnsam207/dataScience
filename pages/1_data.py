# ══════════════════════════════════════════════════
# 출처
# ══════════════════════════════════════════════════
if st.session_state.data_page == "출처":
    import os, base64
    pages_folder = os.path.dirname(os.path.abspath(__file__))

    st.markdown(
        '<div style="max-width:680px;">'
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:32px 40px; margin-bottom:20px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="font-size:22px; font-weight:800; margin-bottom:24px; color:#1565c0;">📂 데이터 출처</div>'
        '<div style="display:flex; flex-direction:column; gap:24px;">'

        # 사이트명
        '<div>'
        '<div style="font-size:15px; font-weight:700; color:#1976d2; margin-bottom:6px;">📌 사이트명</div>'
        '<div style="font-size:17px; color:#222; line-height:1.8; padding-left:8px;">'
        'NγPi &nbsp; 한국 아동·청소년·청년 데이터 아카이브'
        '</div>'
        '</div>'

        # URL
        '<div>'
        '<div style="font-size:15px; font-weight:700; color:#1976d2; margin-bottom:6px;">🔗 URL</div>'
        '<div style="padding-left:8px;">'
        '<a href="https://www.nypi.re.kr/archive/mps" target="_blank"'
        ' style="font-size:17px; color:#1976d2; text-decoration:underline; line-height:1.8;">'
        'https://www.nypi.re.kr/archive/mps'
        '</a>'
        '</div>'
        '</div>'

        '</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    # 접속하기
    st.markdown(
        '<div style="max-width:680px; margin-bottom:20px;">'
        '<div style="background:linear-gradient(135deg,#e3f2fd,#e8f5e9);'
        ' border-radius:16px; padding:32px 40px;'
        ' border-left:6px solid #1976d2;">'
        '<div style="font-size:15px; font-weight:700; color:#1976d2; margin-bottom:16px;">🌐 접속하기</div>',
        unsafe_allow_html=True
    )

    st.link_button(
        "🌐  사이트 접속하기",
        "https://www.nypi.re.kr/archive/mps",
        use_container_width=False
    )

    # cite.jpg
    cite_img = os.path.join(pages_folder, "cite.jpg")
    if os.path.exists(cite_img):
        def img_to_base64(img_path):
            ext  = img_path.split(".")[-1].lower()
            mime = "image/png" if ext == "png" else "image/jpeg"
            with open(img_path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode()
            return mime, b64
        mime, b64 = img_to_base64(cite_img)
        st.markdown(
            '<div style="margin-top:20px;">'
            '<img src="data:' + mime + ';base64,' + b64 + '"'
            ' style="width:100%; height:auto; border-radius:10px; display:block;">'
            '</div>',
            unsafe_allow_html=True
        )
    else:
        st.info("cite.jpg 파일을 pages 폴더에 추가해 주세요.")

    st.markdown('</div></div>', unsafe_allow_html=True)