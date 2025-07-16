import streamlit as st 
import plotly.express as px
import pandas as pd

# st.set_page_config(layout= "wide") 
st.title("Weather Forecast for next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: " , 1,5,1)
options = st.selectbox("Select data to view: " , ["Temperature","Sky"])
st.subheader(f"{options} for the next {days} days in {place}: ")
def get_data(days) :
    dates = ["1","2","3"]
    temp = [31,29,30]
    return dates,temp 
d,t = get_data(days)
figure = px.line(x = d, y= t, labels= {"x" : "Date" , "y" : "Temperature (C)"})
st.plotly_chart(figure)