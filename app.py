import streamlit as st

st.set_page_config(layout="wide")

pages = [
    st.Page("pages/0_home.py", title="소개하기", icon="👩‍🏫"),
    st.Page("pages/1_data.py", title="활용한 데이터", icon="📂"),
    st.Page("pages/2_subject.py", title="연구 주제", icon="🔍"),
    st.Page("pages/3_linear.py", title="다중 선형 회귀분석", icon="📈"),
    st.Page("pages/4_logistic.py", title="로지스틱 회귀분석", icon="📉"),
]
pg = st.navigation(pages)

if "current_page" not in st.session_state:
    st.session_state.current_page = pg.title
if st.session_state.current_page != pg.title:
    st.session_state.current_page = pg.title
    st.session_state.intro_page = "2ok"

pg.run()