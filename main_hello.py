import streamlit as st

st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.streamlit.io/help",
        "Report a bug": "https://streamlit.io/bug",
        "About": "전태환 - Hello Streamlit 앱입니다."
    }
)
st.sidebar.title('다양한 사이드바 위젯들')
st.sidebar.checkbox('외국인 포함')
st.sidebar.checkbox('고령인구 포함')
st.sidebar.divider()
st.sidebar.radio('데이터 타입', ['전체','남성','여성'])
st.slidebar.slider('나이 선택', 0, 100, (20, 50) )
st.slidebar.selectbox('지역 선택', ['서울','경기','인천','대전','대구','부산','광주'])
