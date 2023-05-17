import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd
import pydeck as pdk
import plotly.express as px
import seaborn as sns
import os

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('지하철 정보')

list1 = ['승강장_유형', '승강장연결_여부', '안전발판_유무']
select1 = st.selectbox('페이지 선택', list1)

folder = os.path.dirname(os.path.abspath(__file__))+'/../../data/'

df2 = pd.read_csv(folder +'file2.csv', encoding='cp949')
df3 = pd.DataFrame(df2)
df3 = df3.drop_duplicates(subset=['역명'],keep='first')
df3 = df3.reset_index()
del df3['index']
df3.지상구분 = df3.지상구분.replace({'지상':1,'지하':0})
df3.승강장연결_여부 = df3.승강장연결_여부.replace({'Y':1,'N':0})
df3.스크린도어_유무 = df3.스크린도어_유무.replace({'Y':1,'N':0})
df3.안전발판_유무 = df3.안전발판_유무.replace({'Y':1,'N':0})

if select1 == '승강장_유형':
    a1 = (df3['지상구분']==1).sum()
    a2 = (df3['지상구분']!=1).sum()

    labels = 'UP','DOWN'
    sections = [a1, a2]
    colors = ['c', 'r']

    plt.pie(sections, labels=labels, colors=colors,
            startangle=0,
            explode = (0, 0), # 틈새 
            autopct = '%1.2f%%' # autopercent - 소수점 둘째짜리까지 비율을 계산해 출력해다오 
            )

    plt.axis('equal') # Try commenting this out.
    plt.title('Platform Location')
    plt.legend()
    plt.show()

    st.pyplot(fig=df3['지상구분'].all(), use_container_width=True)
    
elif select1 == '승강장연결_여부':
    b1 = (df3['승강장연결_여부']==1).sum()
    b2 = (df3['승강장연결_여부']!=1).sum()

    labels = 'Y','N'
    sections = [b1, b2]
    colors = ['r', 'g']

    plt.pie(sections, labels=labels, colors=colors,
            startangle=0,
            explode = (0, 0), # 틈새 
            autopct = '%1.2f%%' # autopercent - 소수점 둘째짜리까지 비율을 계산해 출력해다오 
            )

    plt.axis('equal') # Try commenting this out.
    plt.title('Platform_connected')
    plt.legend()
    plt.show()

    st.pyplot(fig=df3['승강장연결_여부'].all(), use_container_width=True)
else:
    c1 = (df3['안전발판_유무']==1).sum()
    c2 = (df3['안전발판_유무']!=1).sum()

    labels = 'Y','N'
    sections = [c1, c2]
    colors = ['g', 'r']

    plt.pie(sections, labels=labels, colors=colors,
            startangle=0,
            explode = (0, 0), # 틈새 
            autopct = '%1.2f%%' # autopercent - 소수점 둘째짜리까지 비율을 계산해 출력해다오 
            ,
            )

    plt.axis('equal') # Try commenting this out.
    plt.title('Safety_foothold')
    plt.show()

    st.pyplot(fig=df3['안전발판_유무'].all(), use_container_width=True)
