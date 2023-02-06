import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.title("matplotlib and seaborn visualizations in streamlit")

data=pd.read_csv('tips.csv')

st.dataframe(data.head())

# Quetions

st.markdown('___')

st.write('male female distribution')

col1,col2=st.columns(2)

data_type=data.dtypes
cat_cols=tuple(data_type[data_type=='object'].index)
with col1:
    st.write('find the number of male and female count')
    feature=st.selectbox('select the categories to disply',cat_cols)
    count=data[feature].value_counts()
    # count=pd.DataFrame(count)
    fig,ax=plt.subplots()
    ax.pie(count,autopct='%0.2f%%',labels=count.index)
    st.pyplot(fig)
     
with col2:   
    st.write('male female count on bar chart')
    fig,ax=plt.subplots()
    ax.bar(count.index,count)
    st.pyplot(fig)

  
with st.expander("click here to display acutal count"):
    st.dataframe(count)

