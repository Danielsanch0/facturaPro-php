import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
uploaded_file = st.file_uploader("Cargar archivo 'facturasPro1.csv'", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("static/datasets/facturasPro1.csv")  # Asegúrate de que exista un archivo de respaldo

# Título de la app
st.title("Análisis de Datos de Ventas")

# Mostrar el dataframe
st.dataframe(df)

# Sidebar para filtros
st.sidebar.header("Filtros")
categoria = st.sidebar.multiselect("Categoría", df["Categoria"].unique())
ciudad = st.sidebar.multiselect("Ciudad", df["Ciudad"].unique())
vendedor = st.sidebar.multiselect("Vendedor", df["Vendedor"].unique())

# Filtrar el dataframe según los filtros seleccionados
df_filtrado = df.copy()
if categoria:
    df_filtrado = df_filtrado[df_filtrado["Categoria"].isin(categoria)]
if ciudad:
    df_filtrado = df_filtrado[df_filtrado["Ciudad"].isin(ciudad)]
if vendedor:
    df_filtrado = df_filtrado[df_filtrado["Vendedor"].isin(vendedor)]

# Mostrar los datos filtrados
st.dataframe(df_filtrado)

# Mostrar estadísticas descriptivas si hay datos filtrados
if not df_filtrado.empty:
    st.subheader("Estadísticas Descriptivas")
    st.write(df_filtrado.describe())

    # Conteo de facturas por categoría
    st.subheader("Conteo de Facturas por Categoría")
    st.bar_chart(df_filtrado["Categoria"].value_counts())

    # Distribución de los montos de las ventas
    st.subheader("Distribución de los Montos de Ventas")
    plt.figure(figsize=(8, 4))
    plt.hist(df_filtrado["Monto"], bins=10, alpha=0.7)
    plt.xlabel("Monto")
    plt.ylabel("Frecuencia")
    plt.title("Distribución de los Montos de Ventas")
    st.pyplot(plt)
else:
    st.write("No hay datos para mostrar con los filtros seleccionados.")
