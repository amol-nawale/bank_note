import streamlit as st
import pandas as pd
import numpy as np
import os

data=pd.read_csv('tips.csv')


def display_random_five(df):
    sample=df.sample(5)
    return sample


button=st.button('display random 5 rows')

if button:
    sample=st.dataframe(display_random_five(data))
    
st.header("checkbox")
st.markdown("___")
agree=st.checkbox("I agree to term and conditions")
st.write('checkbox status',agree)


##create multiple checkboxes

with st.container():
    st.info("which technologies you know")
    data_science=st.checkbox("Data science")
    web_developement=st.checkbox("Web development")
    ai_ml=st.checkbox('artificial intelligence and machine learning')

    button=st.button('submit')
    if button:
        dict={"Data science":data_science,"Web developement":web_developement,"artificial intelligence and machine learning":ai_ml}

        st.json(dict)

st.markdown("___")

radio_button=st.radio("what is youre gender",("male","female","others"))
st.write("this is my geneder: ",radio_button)

st.markdown("___")
st.subheader("st.selectbox")
selectbox=st.selectbox("what skills your want to learn: ",("android","java","css","html","data science"))
st.write("this skill i want to learn: ",selectbox)

st.markdown("___")
st.header("multiselect")
options=st.multiselect("what kind of movies you like",['comedy','action','scify','drama'])
st.write('my options',options)


st.markdown("___")
st.subheader('st.slider()')

loan=st.slider("how much loan do you want" , 0,100000,1000,1000)
st.write("i want this much:",loan)

st.markdown("___")
st.header("various inputs")

with st.container():
    st.subheader("text_input(),st.number_input,st.text_area,st.date_input")

    name=st.text_input("please enter your name")
    age=st.number_input('what is your age',min_value=0,max_value=150,value=25,step=1)
    describe=st.text_area('description',height=150)
    date=st.date_input('select date of birth')

    button=st.button('submit',button)
    if button:
        dict={'name':name,'age':age,'describe':describe,'date':date}

        st.json(dict)


st.markdown("___")
st.subheader('st.file_uploder()')

upload_file=st.file_uploader('choose file')
save_file=st.button('save_file')

if save_file:
    if upload_file is not None:
        with open(os.path.join('vs\streamlit\save_folder',upload_file.name),mode='wb') as f:
            f.write(upload_file.getbuffer())

            st.success('the file is uploaded')

    else:
        st.write('please select file')






