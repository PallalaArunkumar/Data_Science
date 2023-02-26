import streamlit as st
import os
from matplotlib import image
import pandas as pd
import plotly.express as px

with st.container():

    st.header('Module1 Working with :orange[IRIS DATASET]')

    iris_img_path = os.path.join('resources','iris_flowers.jpg')
    st.image(iris_img_path)

    iris_path=os.path.join('resources','iris.csv')
    df = pd.read_csv(iris_path)
    st.header(':red[Iris DataSet]')
    st.dataframe(df)

    st.subheader("Histogram of Sepalength v/s Count")
    species = st.selectbox("Select the Species",df['Species'].unique())

    fig1 = px.histogram(df[df['Species']==species],x='SepalLengthCm')
    st.plotly_chart(fig1,use_container_width=True)

    st.subheader(':red[Box plots of the selected Species]')

    fig2 = px.box(df[df['Species']==species],y='SepalLengthCm')
    st.plotly_chart(fig2,use_container_width=True)

