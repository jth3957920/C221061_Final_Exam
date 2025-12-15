from datetime import datetime
import json
import random
import re
from collections import Counter
from itertools import combinations
import urllib.parse
import urllib.request

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

import seaborn as sns
import plotly.express as px
import altair as alt

from wordcloud import WordCloud, STOPWORDS
from PIL import Image

import networkx as nx

import streamlit as st


st.set_page_config(
    page_title="데이터 시각화 기말고사",
    page_icon="📌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.streamlit.io/help",
        "Report a bug": "https://streamlit.io/bug",
        "About": "전태환 - Hello Streamlit 앱입니다."
    }
)


st.title('▪️C221061 전태환 ')
st.write("""# 데이터 시각화 기말고사 프로젝트""")
st.write("""### 키워드를 선택하세요.""")


keyword_list = ["Golden 케이팝 데몬 헌터스_sim", "K팝 데몬 헌터스_date", "Takedown 케이팝 데몬 헌터스_sim", "통합 데이터"]
selected_keyword = st.selectbox("키워드를 선택하세요", keyword_list)
st.header(f"선택된 키워드: {selected_keyword}")


#선택한 키워드에 따라 이미지 출력
if selected_keyword == "Golden 케이팝 데몬 헌터스_sim":
    st.write("# wordCloud 시각화 결과")
    st.image("Golden 케이팝 데몬 헌터스_sim word Cloud 시각화.png", caption="Golden 케이팝 데몬 헌터스_sim Word Cloud", use_container_width=True)
    st.write("# Networkx 시각화 결과")
    st.image("Golden 케이팝 데몬 헌터스_sim 네트워크 시각화.png", caption="Golden 케이팝 데몬 헌터스_sim Network Visualization", use_container_width=True)
    st.write("# Seaborn 히스토그램 시각화 결과")
    st.image("Golden 케이팝 데몬 헌터스_sim키워드_히스토그램.png", caption="Golden 케이팝 데몬 헌터스_sim Keyword Histogram", use_container_width=True)
    st.write("# 관련 뉴스 사진")
    st.image("Golden 케이팝 데몬 헌터스_뉴스.png", caption="Golden 케이팝 데몬 헌터스_sim 관련 뉴스", use_container_width=True)
    # 설명 추가
elif selected_keyword == "K팝 데몬 헌터스_date":
    st.write("# wordCloud 시각화 결과")
    st.image("K팝 데몬 헌터스_date word Cloud 시각화.png", caption="K팝 데몬 헌터스_date Word Cloud", use_container_width=True)
    st.write("# Networkx 시각화 결과")
    st.image("K팝 데몬 헌터스_date 네트워크 시각화.png", caption="K팝 데몬 헌터스_date Network Visualization", use_container_width=True)
    st.write("# Seaborn 히스토그램 시각화 결과")
    st.image("K팝 데몬 헌터스_date키워드_히스토그램.png", caption="K팝 데몬 헌터스_date Keyword Histogram", use_container_width=True)
    st.write("# 관련 뉴스 사진")
    st.image("K팝 데몬 헌터스_뉴스.png", caption   ="K팝 데몬 헌터스_date 관련 뉴스", use_container_width=True)
    # 설명 추가

elif selected_keyword == "Takedown 케이팝 데몬 헌터스_sim":
    st.write("# wordCloud 시각화 결과")
    st.image("Takedown 케이팝 데몬 헌터스_sim word Cloud 시각화.png", caption="Takedown 케이팝 데몬 헌터스_sim Word Cloud", use_container_width=True)
    st.write("# Networkx 시각화 결과")
    st.image("Takedown 케이팝 데몬 헌터스_sim 네트워크 시각화.png", caption="Takedown 케이팝 데몬 헌터스_sim Network Visualization", use_container_width=True)
    st.write("# Seaborn 히스토그램 시각화 결과")
    st.image("Takedown 케이팝 데몬 헌터스_sim키워드_히스토그램.png", caption="Takedown 케이팝 데몬 헌터스_sim Keyword Histogram", use_container_width=True)
    st.write("# 관련 뉴스 사진")
    st.image("Takedown 케이팝 데몬 헌터스_뉴스.png", caption="Takedown 케이팝 데몬 헌터스_sim 관련 뉴스", use_container_width=True)
    # 설명 추가

elif selected_keyword == "통합 데이터":
    st.write("# wordCloud 시각화 결과")
    st.image("통합 데이터 word Cloud 시각화.png", caption="통합 데이터 Word Cloud", use_container_width=True)
    st.write("# Networkx 시각화 결과")
    st.image("통합 데이터 네트워크 시각화.png", caption="통합 데이터 Network Visualization", use_container_width=True)
    st.write("# Seaborn 히스토그램 시각화 결과")
    st.image("통합 데이터키워드_히스토그램.png", caption="통합 데이터 Keyword Histogram", use_container_width=True)
    # 설명 추가
else:
    st.write("유효하지 않은 선택입니다.")

"""
---
---
# 통합 데이터프레임 불러오기
"""

combined_df = pd.read_json('combined_df.json', encoding='utf-8')

# combined_df 출력
st.subheader("통합 데이터프레임 미리보기")
st.dataframe(combined_df.head())

"""
---
"""
def edge_counts(token_list, n=2): 
    edge_list = []
    for nouns in token_list:
        if len(nouns) >= n :
            edge_list.extend(combinations(sorted(nouns),n))
    edge_counts = Counter(edge_list)
    return edge_counts

def counter_to_word_freq(counter):
    return {
        word_tuple[0]: freq
        for word_tuple, freq in counter.items()
    }

def draw_altair_bar_plot_with_slider(combined_df, file_name, top_k=15):

    # search_keyword 별 단어 빈도 집계
    data = []
    for keyword in combined_df['search_keyword'].unique():
        subset_df = combined_df[combined_df['search_keyword'] == keyword]
        term_dict = counter_to_word_freq(edge_counts(subset_df["title_token"], 1))
        word_freq = dict(
            sorted(term_dict.items(), key=lambda x: x[1], reverse=True)[:top_k]
        )
        for word, freq in word_freq.items():
            data.append({
                'word': word,
                'search_keyword': keyword,
                'frequency': freq
            })

    df_altair = pd.DataFrame(data)

    # ✅ Altair v5 방식 selection
    selector = alt.selection_point(
        fields=['search_keyword'],
        bind=alt.binding_select(
            options=combined_df['search_keyword'].unique().tolist(),
            name='검색 키워드: '
        )
    )

    chart = (
        alt.Chart(df_altair)
        .mark_bar()
        .encode(
            x=alt.X('word:N', sort='-y', title='단어'),
            y=alt.Y('frequency:Q', title='빈도수'),
            color=alt.Color('word:N', legend=None)
        )
        .add_params(selector)
        .transform_filter(selector)
        .properties(
            width=800,
            height=400,
            title=file_name + " 키워드 히스토그램 (Altair)"
        )
    )
    st.altair_chart(chart, use_container_width=True)
    # 그래프 시각화
    

# k 선택 위젯 만들기
st.write("### 상위 k개 단어를 선택하세요.")
top_k = st.slider("상위 k개 단어 선택", min_value=5, max_value=30, value=15, step=1)

draw_altair_bar_plot_with_slider(combined_df, "통합 데이터", top_k=top_k)

"""
# 결과 해석
---
#### 케이팝 데몬 헌터스의 노래 'Golden'과 'Takedown'이 뉴스 기사에서 많이 언급되고 있음을 알 수 있습니다.
#### Golden 은 특히 goldenGlove의 수상 후보로 오르며 많은 기사가 쏟아져 나왔고, 
#### Takedown은 빌보드 차트에서 좋은 성적을 거두며 여러 기사가 작성된 것으로 보입니다.
#### 이러한 기사를 보아 OST 가 케이팝 데몬 헌터스의 인기와 성공에 중요한 역할을 한 것으로 해석할 수 있습니다.
#### 케이팝 데몬 헌터스의 해외 반응은 넷플릭스에서 열풍이었다는 기사를 통해 알 수 있었습니다.
#### 또한 리뷰로 한국의 문화에 대해 잘 알게되었다는 리뷰가 많으며, 다양한 기업(농심 등)과의 협업 관련된 기사를 발견 할 수 있었습니다.
#### 이를 통해 케이팝 데몬 헌터스가 단순한 애니메이션을 넘어 한국 문화와 산업 전반에 긍정적인 영향을 미치고 있음을 알 수 있습니다.

"""

