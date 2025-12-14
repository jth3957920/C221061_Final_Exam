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
st.sidebar.slider('나이 선택', 0, 100, (20, 50))
st.sidebar.selectbox('지역 선택', ['서울','경기','인천','대전','대구','부산','광주'])

st.title('Hello Streamlit 👋')
st.header('Streamlit 소개')
st.subheader('빠르게 웹앱을 만들 수 있는 라이브러리')
st.text('파이썬 스크립트만으로도\n쉽게 웹앱을 만들 수 있습니다.')
st.markdown('''
# 마크다운 문법 지원 
- **굵은 글씨**
- *기울임 글씨*
- ***굵고 기울임 글씨***
- ~~취소선~~
- [링크](https://www.streamlit.io/)
''')
st.caption('그림 1. Streamlit 로고')
st.write('> Streamlit은 데이터 사이언티스트와 머신러닝 엔지니어가 빠르게 웹앱을 만들 수 있도록 도와주는 오픈소스 라이브러리입니다.' )
st.write("# 마크다운 H1 제목")
st.write("## 마크다운 H2 제목")
st.write("### 마크다운 H3 제목")
st.write('') #빈줄
st.write(":red[빨간색 글씨], :green[초록색 글씨], :blue[파란색 글씨]")

st.code('print("Hello, World!")', language='python', line_numbers=True)

with st.echo():
    name = "전태환"
    st.write(f"안녕하세요, {name}님!")

st.latex(r'''
    a^2 + b^2 = c^2
    e^{i\pi} + 1 = 0
''')    
st.divider()
st.image("python.jpg", caption="파이썬 로고", use_container_width=True)
'# Streamlit Magic'


