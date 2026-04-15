import streamlit as st

pages = [
    st.Page("pages/0_home.py", title="시작하기", icon="👩‍🏫"),
    st.Page("pages/1_data.py", title="데이터 수집", icon="📊"),
    st.Page("pages/2_linear.py", title="다중선형 회귀분석", icon="📈"),
    st.Page("pages/3_logistic.py", title="로지스틱 회귀분석", icon="📉"),
]
pg = st.navigation(pages)

if "current_page" not in st.session_state:
    st.session_state.current_page = pg.title
if st.session_state.current_page != pg.title:
    st.session_state.current_page = pg.title
    st.session_state.intro_page = "2ok"

pg.run()