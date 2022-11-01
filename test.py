import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
import base64



st.title('Beykoz calculator')


x = st.number_input("number of people" , key="x" , value=1)
d = {}
for i in range(x):
    d[f"person{i}"] =  st.number_input(f"person number {int(i)}",  value=0,key=f"{i} ")
    #d[st.text_input(label=" ", value=f"person number {int(i)}" )] = st.number_input("",  value=0,key=f"{i} ")
  



df = pd.DataFrame({ "name":[k for k,v in d.items()],"orignal price":[v for k,v in d.items()],"indirmli":[v - v*0.25 for k,v in d.items()]})


if x != 1:

    st.write(pd.DataFrame({"total price":[df[df.columns[1]].sum()],"indirmli":[df[df.columns[2]].sum()]}))


    st.write(df)


    agree = st.checkbox('show chart')

    if agree:
        st.bar_chart(df[df.columns[1]])


import base64

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.ibb.co/BsL7KYv/20210303-135022.jpg");
             background-attachment: fixed;
             opacity: 1;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
