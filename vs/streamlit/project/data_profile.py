import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

import sys 
import os



def get_filesize(file):
  size_bytes=sys.getsizeof(file)
  size_mb=size_bytes/(1024**2)
  return size_mb



def validation(file):
  filename=file.name
  name,ext=os.path.splitext(filename)
  if ext in ('.csv','.xlsx'):
    return ext
  else:
    return False

  

#sidebar
with st.sidebar:
    uploaded_file=st.file_uploader("upload.csv the filesize should not exceed 10mb")
    if uploaded_file is not None:
      st.write('modes of operation')
      minimal=st.checkbox('do you want minimal report')
      display_mode=st.radio('Display mode:',options=('Primary','Dark','Orange'))
      if display_mode=='Dark':
        dark_mode=True
        orange_mode=False
      elif display_mode=='Orange':
        dark_mode=False
        orange_mode=True
      else:
        dark_mode=False
        orange_mode=False
      


if uploaded_file is not None:
  ext=validation(uploaded_file)
  if ext:
    filesize=get_filesize(uploaded_file)
    if filesize <= 10:
      if ext=='.csv':
          # time being lets load csv file
        df=pd.read_csv(uploaded_file)
        st.dataframe(df.head())

      else:
          xl_file=pd.ExcelFile(uploaded_file)
          sheet_tuple=tuple(xl_file.sheet_names)
          sheet_name=st.sidebar.selectbox('select the sheet',sheet_tuple)
          df=xl_file.parse(sheet_name)

    else:
      st.error('maximum filesize uploaded size is 10mb')   


    with st.spinner('Generating report'):
      pr =df.profile_report(minimal=minimal,dark_mode=dark_mode,orange_mode=orange_mode)


    st_profile_report(pr)


 

      
    


    
