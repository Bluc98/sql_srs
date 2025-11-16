import streamlit as st
import pandas as pd
import duckdb as db
data = {'a':[1,2,3],'b':[4,5,6]}
df = pd.DataFrame(data)
st.write('Hello world')

tab1, = st.tabs(['Tab1'])
with tab1:
    query = st.text_area(label='entrez votre query')
    df_result = db.query(query).df()
    st.write(query)
    st.write(df)
    st.dataframe(df_result)


