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

"""
###마크다운 헤더3
- 마크다운 목록1. **굵게** 표시
- 마크다운 목록2. *기울임* 표시
	- 마크다운 목록2-1
	- 마크다운 목록2-2

### 마크다운 링크
- [네이버](https://naver.com)
- [구글](https://google.com)

### 마크다운 인용
> 인용문: "Streamlit은 데이터 앱을 쉽게 만들 수 있는 프레임워크입니다."

### 마크다운 표
|헤더1 | 헤더2 |
| ---- | ---|
데이터1 | 데이터2|

### 마크다운 코드 블록
''' python
def hello_world():
	print("Hello, World!")
'''
"""

st.info('This is a purely informational message', icon="ℹ️")
st.success('This is a success message!', icon="✅")
st.warning('This is a warning message', icon="⚠️")
st.error('This is an error message', icon="❌")

import pandas as pd
df = pd.DataFrame(
    {'id': [1, 2, 3],
     'name': ['Alice', 'Bob', 'Charlie'],
     'age': [24, 30, 22]
     }
)
df
'### :orange[Matplotlib : st.pyplot]'
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y )
st.pyplot(fig)

st.divider()

'### :orange[Altair : st.altair_chart]'
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

c= alt.Chart(chart_data).mark_circle().encode(
    x='a',
    y='b',
    size='c',
    color='c',
    tooltip=['a', 'b', 'c']
).interactive()

st.altair_chart(c, use_container_width=True)

'### :orange[Plotly : st.plotly_chart]'
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length',
                 color='species', size='petal_length',
                 hover_data=['petal_width'])
st.plotly_chart(fig, key = "iris",on_select="rerun")

'### :orange[컬럼: st.columns]'
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.write("## 컬럼 1")
    st.checkbox("체크박스1")
    st.checkbox("체크박스2")

with col2:
    st.write("## 컬럼 2")
    st.radio("라디오 선택", ['옵션1','옵션2','옵션3'])


col3.write("## 컬럼 3")
col3.selectbox("셀렉트박스", ['선택1','선택2','선택3'])

'### :orange[탭 : st.tabs]'
tab1, tab2, tab3 = st.tabs(['python','R','Julia'])
with tab1:
    st.write(
        '''
        ```python
        import pandas as pd
        df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
        print(df)
        ```
        '''
    )

with tab2:
    st.write(
        '''
        ```R
        df <- data.frame(A=c(1,2,3), B=c(4,5,6))
        print(df)
        ```
        '''
    )

with tab3:
    st.write(
        '''
        ```julia
        df = DataFrame(A=[1,2,3], B=[4,5,6])
        println(df)
        ```
        '''
    )

'### :orange[확장 레이아웃 : st.expander]'
with st.expander("확장 레이아웃 열기"):
    st.write("여기에 추가 정보를 넣을 수 있습니다.")
    st.code('print("Hello, Streamlit!")', language='python')

'# :blue[사용자 입력]'
'### :orange[텍스트 입력 : st.text_input]'
name = st.text_input("이름을 입력하세요:", "")
if name:
    st.write(f"안녕하세요, {name}님!")
'### :orange[숫자 입력 : st.number_input]'
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=120, value=25, step=1)
st.write(f"당신의 나이는 {age}세 입니다.")
'### :orange[날짜 입력 : st.date_input]'
birth_date = st.date_input("생일을 선택하세요:")
st.write(f"당신의 생일은 {birth_date}입니다.")
'### :orange[파일 업로드 : st.file_uploader]'
uploaded_file = st.file_uploader("파일을 업로드하세요:", type=["csv", "xlsx", "txt"])
if uploaded_file is not None:
    st.write(f"업로드된 파일: {uploaded_file.name}")
    # 파일 내용 읽기
    file_details = {"파일명": uploaded_file.name, "파일형식": uploaded_file.type, "파일크기(바이트)": uploaded_file.size}
    st.write(file_details)

import os
import streamlit as st

if uploaded_file is not None:
    save_path = uploaded_file.name  # 현재 디렉터리

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"파일이 {save_path} 경로에 저장되었습니다.")

'# :blue[버튼]'
'### :orange[일반 버튼 : st.button]'
button = st.button("일반 버튼 클릭")
if button:
    st.write("버튼이 클릭되었습니다!")
'### :orange[주요 버튼 : primary]'
primary_button = st.button("주요 버튼 클릭", type="primary")
if primary_button:
    st.write("주요 버튼이 클릭되었습니다!") 

'### :orange[다운로드버튼 : st.download_button]'
with open("python.jpg", "rb") as file:
    btn = st.download_button(
        label="파이썬 로고 다운로드",
        data=file,
        file_name="python_logo.jpg",
        mime="image/jpg"
    )

'### :orange[피드백 버튼 : st.feedback]'
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected:
    st.markdown (f"당신은 { sentiment_mapping[selected]} star(s)을 선택하였습니다.")
    
'### :orange[링크 버튼 : st.link_button]'
st.link_button("구글로 이동", "https://www.google.com")
