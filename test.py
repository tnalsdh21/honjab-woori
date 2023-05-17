import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from datetime import datetime, timedelta 

timeline = st.sidebar.slider('시간대를 골라주세요', value=datetime(2020,1,1,5,30), min_value=datetime(2020,1,1,5,30), max_value=datetime(2020,1,1,23,59), step=timedelta(minutes=30), format='hh:mm')

st.write(timeline, pd.__version__)
position_cols = ['name', 'position', 'lat', 'lon','line']
position_9 = pd.read_csv('./data/9_position.csv', index_col=0, names=position_cols)
position_9['name'] = position_9['name'].str.replace(pat='역',repl='', regex=True)

honjab_2020 = pd.read_csv('./data/9_honjab2020.csv', index_col=0, header =0)

hon = pd.DataFrame()
temp = honjab_2020.loc[: , ['구분','05:30~05:59']]

i = 37
while i>=0:
  #temp의 시간혼잡도 = j
  j = round(temp.iloc[i][1])
  while j>0:
    # hon.append(pd.DataFrame(position_9.loc[i,['lat','lon']]), ignore_indx=True)

    hon =hon.append(position_9.loc[i,['lat','lon']])
    j-=1
  i -= 1

# chart_data = pd.DataFrame(position_9.loc[:,['lat', 'lon']],columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.51,
        longitude=126.99,
        zoom=10.5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
          'HexagonLayer',
          data=hon,
          get_position='[lon, lat]',
          radius=200,
          elevation_scale=4,
          elevation_range=[0, 300],
          pickable=True,
          extruded=True,
          
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=hon,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
            
        ),
    ],
))