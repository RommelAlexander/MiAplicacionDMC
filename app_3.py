import streamlit as st
import libreria_funciones as lf

st.title("Clase 5 funciones")
st.image("logo.png", width=200)
st.sidebar.image("demon.png", width=300)

p= st.number_input("Ingres el monto principal",value=12000)
t= st.number_input("Ingrese la tasa anual", value=0.05)
a= st.slider("Seleccione el numero de años",min_value=1,max_value=12)
pa=st.number_input("Cantidad de pagos por años",value=12)
cuota=lf.cuota_prestamo(p,t,a,pa)
st.write(cuota)











