import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd




st.title('Beykoz calculator')


buff, col, buff2 = st.columns([1,3,1])




x = col.number_input("number of people" , key="x" , value=1 , step=0)
d = {}
for i in range(x):
    d[f"person{i}"] =  col.number_input(f"person number {int(i)}",  value=0,key=f"{i} " , step=5)
    #d[st.text_input(label=" ", value=f"person number {int(i)}" )] = st.number_input("",  value=0,key=f"{i} ")
  



df = pd.DataFrame({ "name":[k for k,v in d.items()],"orignal price":[v for k,v in d.items()],"indirmli":[v - v*0.25 for k,v in d.items()]})


if  list(d.values())[0] !=0:

    col.write(pd.DataFrame({"total price":[df[df.columns[1]].sum()],"indirmli":[df[df.columns[2]].sum()]}))


    col.write(df)


    agree = col.checkbox('show chart')

    if agree:
        col.bar_chart(df[df.columns[1]])


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

m = st.markdown(""" <style> div.stCheckbox > checkbox { 
                    background-color: rgb(204, 49, 49); } 
                    </style>""", unsafe_allow_html=True)

b = st.checkbox("ghj")
