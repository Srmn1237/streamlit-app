import streamlit as st
import random

num=st.number_input("cpp",min_value=0)
if st.button("app"):
    for i in range(num):
        st.write(random.randint(0,100))