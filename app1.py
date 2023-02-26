import streamlit  as st
import os
from matplotlib import image


with st.container():
    st.header("WELCOME TO DATA SCIENCE INTERNSHIP")

    image_path = os.path.join('resources','data-science-analysis.jpg')
    st.image(image_path)

    st.subheader('Welcome to the India Biggest Free Internship Program by :red[Innomatics Research Labs]')
    p1='I would like to congratulations to everyone here for being top 10 percentage in'
    st.text(p1)
    st.text('the hackathon conducted by us.')
    st.text(' Let us look into the road map to become a data scientist')
    st.title(":blue[RoadMap to Become a Data Scientist]")
    image_path2 = os.path.join('resources','Roadmap.jpg')
    st.image(image_path2)