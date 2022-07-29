import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [1000, 20, 3, 40]
})

st.dataframe(df)
