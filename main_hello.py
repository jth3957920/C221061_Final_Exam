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

st.sidebar.title('파라미터 조정바')
st.sidebar.divider()

run_button = st.sidebar.button("일반 버튼 클릭")
if run_button:
    st.write("버튼이 클릭되었습니다!")

st.title('▪️C221061 전태환 ')

st.image("Golden 케이팝 데몬 헌터스_sim word Cloud 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("Golden 케이팝 데몬 헌터스_sim 네트워크 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("Golden 케이팝 데몬 헌터스_sim키워드_히스토그램.png", caption="파이썬 로고", use_container_width=True)
st.image("K팝 데몬 헌터스_date word Cloud 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("K팝 데몬 헌터스_date 네트워크 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("K팝 데몬 헌터스_date키워드_히스토그램.png", caption="파이썬 로고", use_container_width=True)
st.image("Takedown 케이팝 데몬 헌터스_sim word Cloud 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("Takedown 케이팝 데몬 헌터스_sim 네트워크 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("Takedown 케이팝 데몬 헌터스_sim키워드_히스토그램.png", caption="파이썬 로고", use_container_width=True)
st.image("통합 데이터 word Cloud 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("통합 데이터 네트워크 시각화.png", caption="파이썬 로고", use_container_width=True)
st.image("통합 데이터키워드_히스토그램.png", caption="파이썬 로고", use_container_width=True)



