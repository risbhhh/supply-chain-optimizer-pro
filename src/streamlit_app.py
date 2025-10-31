import streamlit as st
import pandas as pd
from src.inventory import inventory_recommendation

st.set_page_config(page_title='Supply Chain Optimizer')
st.title('Supply Chain Optimizer - Demo')

df = pd.read_csv('data/sample_sales.csv', parse_dates=['date'])
sku = st.selectbox('Select SKU', df['item_id'].unique())
loc = st.selectbox('Select Location', ['WH-A','WH-B'])

st.subheader('Inventory Recommendation')
params = inventory_recommendation(mean_demand=200, std_demand=40, lead_time=2)
st.write(params)

st.subheader('Sample Demand (first 10 rows)')
st.dataframe(df.head(10))
