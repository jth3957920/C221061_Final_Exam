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
