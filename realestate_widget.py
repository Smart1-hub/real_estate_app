import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Average Growth of Real Estate in the US')

#run the app
#streamlit run realestate.py

@st.cache_data
def load_data():
    raw_data = pd.read_excel("real_estate_us.xlsx")
    lowercase = lambda x: str(x).lower()
    return raw_data

#Create a text element and let the reader know the data is loading
data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache_data)") #indicate loading progress

#Displaying the raw data, let add a subheader
if st.checkbox('Show raw data'):
    st.subheader('Real Estate Sales Data')
    st.write(data)

data.drop_duplicates()
real_estate = data.fillna(0)

with st.expander('Average sales price by Region for home size'):
    column1, column2 = st.columns([3, 2])

    #Allow user to select an home size
    select_home_size = st.selectbox('Select home size', real_estate.Home_size.unique(), index = 0)
    #Apply home size filter
    home_size = real_estate[real_estate['Home_size'] == select_home_size]
    #Allow user to select a region
    select_region = column2.selectbox('Select a region', real_estate.Region.unique())
    #Apply region filter
    region_home_size = home_size[home_size['Region'] == select_region]

    #Use the region dataframe
    fig = px.bar(region_home_size.sort_values('Average_sales_price'), x='Year', y='Average_sales_price', color='Region')

    if select_home_size == 'Double':
        st.write('Home size type is double')
    if select_home_size == 'Single':
        st.write('Home size type is single')
    if select_home_size == 'Total1':
        st.write('Home type is total')

    st.plotly_chart(fig, use_container_width=True)









