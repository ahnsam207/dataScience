
import streamlit as st

st.markdown(
    "<style>"
    ".block-container {"
    "  padding-top: 4rem !important;"
    "  padding-left: 2rem !important;"
    "  padding-right: 2rem !important;"
    "}"
    "</style>",
    unsafe_allow_html=True
)

st.markdown(
    '<div style="background:linear-gradient(135deg,#1a237e,#283593);'
    ' border-radius:20px; padding:48px 56px; margin-bottom:24px;">'

    '<div style="font-size:32px; font-weight:900; color:white; margin-bottom:8px;">🎓 소감</div>'
    '<div style="font-size:15px; color:rgba(255,255,255,0.5); margin-bottom:40px;">'
    'Streamlit 웹앱 발표를 마치며'
    '</div>'

    '<div style="border-left:4px solid #64b5f6; padding-left:28px; margin-bottom:36px;">'
    '<div style="font-size:19px; line-height:2.2; color:white;">'
    '스트림릿 웹앱 발표 자료를 준비하면서 그동안 생각만 하고 구현하지 못했던'
    ' <span style="color:#64b5f6; font-weight:700;">교과 학습 홈페이지</span>를 함께 개발하였습니다.<br>'
    '덕분에 수업이 원활하게 진행되고 있습니다.'
    '</div>'
    '<div style="margin-top:20px; display:flex; align-items:center; gap:12px;">'
    '<span style="font-size:22px;">🙏</span>'
    '<span style="font-size:19px; color:#ffeb3b; font-weight:700;">교수님께 먼저 감사를 전합니다.</span>'
    '</div>'
    '</div>'

    '<div style="background:rgba(255,255,255,0.07); border-radius:16px; padding:32px 36px;">'
    '<div style="font-size:17px; color:rgba(255,255,255,0.6); font-weight:700; margin-bottom:16px; letter-spacing:1px;">💡 이번 실습을 통해 느낀 것</div>'
    '<div style="display:flex; flex-direction:column; gap:20px;">'

    '<div style="display:flex; align-items:flex-start; gap:16px;">'
    '<span style="background:#42a5f5; color:white; border-radius:50%; min-width:32px; height:32px;'
    ' display:flex; align-items:center; justify-content:center; font-size:15px;'
    ' font-weight:700; flex-shrink:0; margin-top:2px;">1</span>'
    '<div style="font-size:18px; line-height:2.0; color:white;">'
    '코드를 통한 탐색적 데이터 분석도 중요하지만,'
    ' <span style="color:#69f0ae; font-weight:700;">분석가의 전문성</span>이 더욱 중요하다는 것을 느꼈습니다.'
    '</div>'
    '</div>'

    '<div style="display:flex; align-items:flex-start; gap:16px;">'
    '<span style="background:#42a5f5; color:white; border-radius:50%; min-width:32px; height:32px;'
    ' display:flex; align-items:center; justify-content:center; font-size:15px;'
    ' font-weight:700; flex-shrink:0; margin-top:2px;">2</span>'
    '<div style="font-size:18px; line-height:2.0; color:white;">'
    '그동안 여러 교육 자료나 강의 내용에서 파악하기 어려웠던'
    ' <span style="color:#ffd180; font-weight:700;">행간의 숨겨진 의미</span>를 경험하며,<br>'
    '놓치고 있던 내용과 의문을 가졌던 내용이 해소되고 정리되는 기회가 된 것 같습니다.'
    '</div>'
    '</div>'


    '<div style="margin-top:36px; text-align:right;">'
    '<span style="font-size:22px; color:#ffeb3b; font-weight:800;">감사합니다 🙏</span>'
    '</div>'

    '</div>',
    unsafe_allow_html=True
)
