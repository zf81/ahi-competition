import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title('What Factors Impact Patient No-Shows?')
st.header('This dashboard explores the factors that influence patients to show or no-show to appointments.')

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/competition/data/output_noshow1_balanced_2022-11-16.csv')
df

st.subheader('Patient Age vs Appointment Show Status')
age = px.bar(df, x= 'patient_age', y=['appointment_yosi_noshow1'], color= 'appointment_yosi_noshow1', barmode='group', height=400)
st.plotly_chart(age)

st.subheader("Weather Conditions vs Show Status")
weather = px.bar(df, x='weather_conditions', y=['appointment_yosi_noshow1'], barmode='group', height=400)
st.plotly_chart(weather) 

st.subheader('Appointment Type vs Appointment Show Status')
type = px.bar(df, x= 'appointment_type', y=['appointment_yosi_noshow1'], color= 'appointment_type', barmode='group', height=400)
st.plotly_chart(type)

st.subheader('Location vs Show Status')
location = px.bar(df, x='geocode_city', y=['appointment_yosi_noshow1'], barmode='group', height=400)
st.plotly_chart(location) 