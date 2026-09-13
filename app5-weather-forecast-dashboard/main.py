import streamlit as st
import plotly.express as px

st.title("Weather Forecast Dashboard")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",
                 min_value=1, max_value=5)
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-05-10", "2022-07-01", "2022-12-03"]
    temperatures = [15, 32, 8]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)