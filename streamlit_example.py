import streamlit as st
from sklearn.datasets import load_wine

data = load_wine(as_frame = True)
df = data.frame


st.title("HOLA AMOR")
st.header("Esta es mi primera aplicación web...URRAAAA")
st.header('Te dedico mi primer página web amor')
st.subheader("Como estás?")
st.write("Adios amor")

st.dataframe(df)

st.image('porquinho-polidance.gif', width=200)