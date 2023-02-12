import numpy as np
import pandas as pd
import streamlit as st
import pickle



pickel_in=open('steamlit\project\classifier.pkl','rb')
classifier=pickle.load(pickel_in)

def bank_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return prediction


st.title('**Bank Note Authentication**')
with st.container():

    
    variance=st.text_input('varience')
    skewness=st.text_input('sckewness')
    curtosis=st.text_input('curtosis')
    entropy=st.text_input('entropy')
    button=st.button('submit')

    if button:
        try:
             result=bank_note_authentication(variance,skewness,curtosis,entropy)

             st.success(f'the result is :{result}')

             

        except:
            st.error('please enter valid input here')

        
        
        
        
        





