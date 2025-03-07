import streamlit as st

def sqr (num):
    return num * num


## Take some input ffrom the user 


number = st.number_input("Insert a number")

button = st.button("Click if you want the square")

if button:
    result = sqr(number)
    st.write("The square of the number is ", result)