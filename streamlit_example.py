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

gif_url = 'https://tenor.com/es/view/porquinho-polidance-gif-26422948'

st.image(gif_url)

st.image(gif_url, use_column_width=True)