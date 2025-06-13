import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.title("Streamlit :red[tutorial]")
st.sidebar.header(" :blue[Introduction to Databases]")
st.side.subheader("WEB APPLICATION")

df=pd.DataFrame(
  np.random.randn(100,2)/[50,50]+[37.76,-122.4],
  columns=['lat','lon'])
st.map(df)
