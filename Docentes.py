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
    color='Campus', title='<b>Docentes do IFPA por campus/área</b>', template='plotly_dark')
fig.update_traces(hovertemplate='%{label}<br>Docentes=%{value}<extra></extra>')
fig.update_layout(width=1000, height=1000, font_color='white',uniformtext_minsize=12, uniformtext_mode='hide', title_x = 0.5, title_font_size=24 )
fig.update_traces(textfont_color='white')
fig.add_layout_image(dict(source=Logo,
           xref="paper", yref="paper",
        x=0.2, y=1.08,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="top"))
st.plotly_chart(fig)
