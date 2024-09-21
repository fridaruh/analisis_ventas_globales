# Dashboard de Análisis de Ventas Globales

Este dashboard, desarrollado con Streamlit, proporciona un análisis interactivo de datos de ventas globales.

## Funcionalidades

1. **Carga de Datos**: 
   - Permite subir un archivo CSV con datos de ventas.

2. **Vista Previa de Datos**:
   - Muestra los primeros 10 registros del dataset cargado.

3. **Filtros Interactivos**:
   - Región: Selección múltiple de regiones.
   - Producto: Selección de un producto específico o todos.
   - Rango de Fechas: Selección del período de análisis.
   - Beneficio: Opción para mostrar solo ventas con beneficio positivo.

4. **KPIs (Indicadores Clave de Rendimiento)**:
   - Ventas Totales
   - Beneficio Total
   - Cantidad Total de Productos Vendidos
   - Promedio de Satisfacción del Cliente

5. **Visualizaciones**:
   - Gráfico de Barras: Ventas Totales por Región
   - Gráfico de Línea: Tendencia de Ventas en el Tiempo
   - Gráfico Circular: Distribución de Ventas por Producto

6. **Exportación de Datos**:
   - Permite descargar los datos filtrados en formato CSV.

## Uso

1. Ejecute la aplicación Streamlit.
2. Suba un archivo CSV con los datos de ventas.
3. Utilice los filtros en la barra lateral para ajustar el análisis.
4. Explore los KPIs y gráficos generados.
5. Descargue los datos filtrados si es necesario.

## Requisitos

- Python 3.10+
- Streamlit
- Pandas
- Plotly Express

## Instalación

`pip install streamlit pandas plotly`

## Ejecución

`streamlit run main.py`