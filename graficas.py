import pandas as pd
import streamlit as st
from PIL import Image

st.header('Graficas utilizando Pandas', divider='rainbow')
st.title("Resultados del Grand Prix de Paises Bajos")

image= Image.open('ruta de imagen')
st.image(image, caption='descripcion de imagen')

st.text_imput("¿Cual es tu nombre?", key="name")
st.session_state.name

st.text('¡Hola ' +st.session_state.name+' !')
'Hola como estas?' , st.session_state.name

df= pd.read_csv('ruta de raw de los datos')

if st.checkbox('Mostrar dataframe'):
  df

option = st.selectbox(
    'Selecciona tu corredor favorito:  ' , 
    df['DRIVER'])

'Tu seleccion: ', option

df.loc[df['DRIVER'] == option]

st.line_chart(
    df,
    x = 'AVG SPEED' , 
    y = 'LAP'
)
