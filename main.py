import streamlit as st 
import plotly.express as px
import pandas as pd
from backend import get_data

# st.set_page_config(layout= "wide") 
st.title("Weather Forecast for next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days: " , 1,5,1)
options = st.selectbox("Select data to view: " , ["Temperature","Sky"])
st.subheader(f"{options} for the next {days} days in {place}: ")
if place:
    try :
        filtered_data = get_data(place,days)

        if options == "Temperature" :
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x = dates, y= temperatures, labels= {"x" : "Date" , "y" : "Temperature (C)"})
            st.plotly_chart(figure)

        elif options == "Sky" :
            sky_conditions = [dict["weather"][0]["main"].lower() for dict in filtered_data]
            image_paths = [f"images/{codn}.png" for codn in sky_conditions] 
            st.image(image_paths, width= 115) 

    except KeyError:
        st.warning("Place does not exist !!")