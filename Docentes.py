import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")

Logo = Image.open("logo.png")
docentes = pd.read_excel('Docentes IFPA 2024.xlsx')
docentes['Área de ingresso']=docentes['Área de ingresso'].str.capitalize()
docentes_por_area=docentes.groupby(['Campus','Área de ingresso'])['Docente'].count().reset_index()
fig=px.sunburst(docentes_por_area, path=['Campus', 'Área de ingresso'], values='Docente',
    color='Campus', title=' ', template='plotly_dark')
fig.update_traces(hovertemplate='%{label}<br>Docentes=%{value}<extra></extra>')
fig.update_layout(width=1000, height=1000, font_color='white',uniformtext_minsize=12, uniformtext_mode='hide', title_x = 0.5, title_font_size=24 )
fig.update_traces(textfont_color='white')
col1,col2,col3 = st.columns(3)
col2.image('logo.png')
st.title('Docentes do IFPA por campus/área')
title_alignment="""
<style>
#the-title {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)
st.plotly_chart(fig, theme=None)
