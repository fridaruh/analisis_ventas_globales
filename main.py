import streamlit as st
import pandas as pd
import plotly.express as px

# Título del Dashboard
st.title("Dashboard de Análisis de Ventas Globales")

# Carga y Visualización de Datos
st.header("Cargar Dataset")

# Instrucciones para cargar el archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Cargar los datos
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])  # Convertir la columna de fecha al formato correcto

    # Mostrar los primeros 10 registros del dataset
    st.subheader("Vista Previa de los Datos (Primeros 10 Registros)")
    st.write(df.head(10))

    # Filtros Interactivos
    st.sidebar.header("Filtros Interactivos")

    # Filtro por Región (multiselect)
    selected_regions = st.sidebar.multiselect(
        "Selecciona Región(es)", 
        options=df["Region"].unique(), 
        default=df["Region"].unique()
    )

    # Filtro por Producto (selectbox) con opción de "Todos los productos"
    product_options = ["Todos los productos"] + df["Product"].unique().tolist()  # Agregar la opción
    selected_product = st.sidebar.selectbox(
        "Selecciona un Producto", 
        options=product_options
    )

    # Convertir fechas a tipo date para que el slider pueda manejarlas
    min_date = df["Date"].min().date()  # Convertir a datetime.date
    max_date = df["Date"].max().date()  # Convertir a datetime.date

    # Filtro por rango de fechas (slider)
    selected_date_range = st.sidebar.slider(
        "Selecciona un Rango de Fechas", 
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date),
        format="YYYY-MM-DD"
    )

    # Checkbox para mostrar solo ventas con beneficio positivo
    benefit_filter = st.sidebar.checkbox("Mostrar solo ventas con beneficio positivo")

    # Aplicar los filtros al dataframe
    df_filtered = df[
        (df["Region"].isin(selected_regions)) & 
        (df["Date"].between(pd.to_datetime(selected_date_range[0]), pd.to_datetime(selected_date_range[1])))
    ]

    # Si se selecciona un producto específico, filtrar por ese producto
    if selected_product != "Todos los productos":
        df_filtered = df_filtered[df_filtered["Product"] == selected_product]

    if benefit_filter:
        df_filtered = df_filtered[df_filtered["Profit"] > 0]

    # Indicadores Clave de Rendimiento (KPIs)
    st.header("Indicadores Clave de Rendimiento (KPIs)")
    total_sales = df_filtered["Sales"].sum()
    total_profit = df_filtered["Profit"].sum()
    total_quantity = df_filtered["Quantity"].sum()
    average_satisfaction = df_filtered["Customer_Satisfaction"].mean()

    st.metric("Ventas Totales (USD)", f"${total_sales:,.2f}")
    st.metric("Beneficio Total (USD)", f"${total_profit:,.2f}")
    st.metric("Cantidad Total de Productos Vendidos", total_quantity)
    st.metric("Promedio de Satisfacción del Cliente", f"{average_satisfaction:.2f}/5")

    # Gráfico de Barras - Ventas Totales por Región
    st.header("Gráfico de Barras: Ventas Totales por Región")
    df_sales_by_region = df_filtered.groupby("Region").agg({"Sales": "sum"}).reset_index()
    fig_sales_by_region = px.bar(df_sales_by_region, x="Region", y="Sales", title="Ventas Totales por Región")
    st.plotly_chart(fig_sales_by_region)

    # Gráfico de Línea - Tendencia de Ventas en el Tiempo
    st.header("Gráfico de Línea: Tendencia de Ventas en el Tiempo")
    df_sales_by_date = df_filtered.groupby("Date").agg({"Sales": "sum"}).reset_index()
    fig_sales_by_date = px.line(df_sales_by_date, x="Date", y="Sales", title="Tendencia de Ventas a lo Largo del Tiempo")
    st.plotly_chart(fig_sales_by_date)

    # Gráfico Circular - Distribución de Ventas por Producto
    st.header("Gráfico Circular: Distribución de Ventas por Producto")
    df_sales_by_product = df_filtered.groupby("Product").agg({"Sales": "sum"}).reset_index()
    fig_sales_by_product = px.pie(df_sales_by_product, values="Sales", names="Product", title="Distribución de Ventas por Producto")
    st.plotly_chart(fig_sales_by_product)

    # Exportar los resultados filtrados a CSV
    st.header("Exportar Resultados Filtrados")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar Datos Filtrados en CSV",
        data=csv,
        file_name='datos_filtrados.csv',
        mime='text/csv'
    )

else:
    st.write("Por favor, sube un archivo CSV para comenzar el análisis.")
