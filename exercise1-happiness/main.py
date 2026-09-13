import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

data_x = st.selectbox("Select the data for the X-axis",
                        ("GDP", "Happiness", "Generosity"))

data_y = st.selectbox("Select the data for the Y-axis",
                        ("GDP", "Happiness", "Generosity"))

st.subheader(f"{data_x} and {data_y}")

df = pd.read_csv("happy.csv")
x_values = df[data_x.lower()]
y_values = df[data_y.lower()]


figure = px.scatter(x=x_values, y=y_values,
                    labels={"x": data_x, "y": data_y})
correlation = x_values.corr(y_values)
st.write(f"Correlation:", correlation)
st.plotly_chart(figure)
