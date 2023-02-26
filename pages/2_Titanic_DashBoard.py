import streamlit as st
import os
from matplotlib import image
import pandas as pd
import plotly.express as px

titanic_img_path = os.path.join('resources','titanic_image.webp')
titanic_csv_path = os.path.join('resources','titanic.csv')
df1 = pd.read_csv(titanic_csv_path)

with st.container():
    st.header('Part 2 :orange[Titanic]')
    st.image(titanic_img_path)
    st.subheader('Titanic Data')
    st.dataframe(df1)

    st.subheader(':blue[Class v/s Survived]')
    st.text('0 - dead, 1- live')
    ti_class = st.selectbox('Select the class',df1['class'].unique())
    fig1 = px.pie(df1[df1['class']==ti_class],names='survived')
    st.plotly_chart(fig1,use_container_width=True)

    st.subheader(':blue[survived v/s age]')
    ti_sur = st.selectbox('Select the survived 0-dead 1-live',df1['survived'].unique())
    fig2 = px.histogram(df1[df1['survived']==ti_sur],x='age')
    st.plotly_chart(fig2,use_container_width=True)

    st.subheader(':blue[gender v/s alive]')
    ti_gen = st.selectbox('Select the gender',df1['sex'].unique())
    fig3 = px.pie(df1[df1['sex']==ti_gen],names='alive')
    st.plotly_chart(fig3,use_container_width=True)
    