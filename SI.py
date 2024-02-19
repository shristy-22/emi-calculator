import streamlit as st
def calculate_emi(p,n,r):
  result= p*r*n/100
  st.write(result)
p=st.slider('loan amt.',1000,100000)
n=st.slider('tenure',5,25)
r=st.slider('interest',12,30)
if st.button('calculate'):
  calculate_emi(p,n,r)