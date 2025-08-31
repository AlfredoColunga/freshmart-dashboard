import streamlit as st
from style_manager import StyleManager
from data_manager import DataManager
from chart_creator import ChartCreator

styles = StyleManager("images/FreshMart-logo.png")


ventas_df = DataManager.load_csv("data/ventas_freshmart.csv")
clientes_df = DataManager.load_csv("data/clientes_freshmart.csv")


tipo_clientes_disponibles = DataManager.load_options(clientes_df, "Tipo Cliente")
fecha_min, fecha_max, fecha_min_default = DataManager.load_dates(ventas_df, "Fecha")


styles.display_header("Dashboard de Clientes")


tipo_cliente = st.sidebar.multiselect(
    "Tipo de Cliente:",
    options=tipo_clientes_disponibles,
    default=tipo_clientes_disponibles,
    placeholder="Selecciona"
)

clientes_disponibles = DataManager.load_options_condition(clientes_df, "Tipo Cliente", tipo_cliente, "ID Cliente")

cliente = st.sidebar.selectbox(
    "Id Cliente:",
    options=clientes_disponibles,
    index=None,
    placeholder="Selecciona"
)

fecha_inicio = st.sidebar.date_input(
    "Fecha inicio:",
    value=fecha_min_default,
    min_value=fecha_min,
    max_value=fecha_max
)

fecha_fin = st.sidebar.date_input(
    "Fecha fin:",
    value=fecha_max,
    min_value=fecha_min,
    max_value=fecha_max
)

freq_nuevo, freq_frecuente, freq_vip = DataManager.group_freq_compra(clientes_df, tipo_cliente, cliente)

col1, col2, col3 = st.columns(3)
col1.metric("Frecuencia de Compra de Clientes Nuevos", freq_nuevo, border=True)
col2.metric("Frecuencia de Compra de Clientes Frecuentes", freq_frecuente, border=True)
col3.metric("Frecuencia de Compra de Clientes VIP", freq_vip, border=True)

st.write("")


bar1_chart_col, _, bar2_chart_col = st.columns([1, .2, 2])

bar1_chart_col.altair_chart(
    ChartCreator.bar_ingreso_tipo_cliente(
        DataManager.group_tipo_cliente(clientes_df, tipo_cliente, cliente)
    ), use_container_width=True
)

bar2_chart_col.altair_chart(
    ChartCreator.bar_ingresos_por_cliente(
        DataManager.filter_customer_data(clientes_df, tipo_cliente, cliente)
    ), use_container_width=True
)

st.altair_chart(
    ChartCreator.line_ventas_tipo_cliente(
        DataManager.merge_data(ventas_df, clientes_df, tipo_cliente, cliente, fecha_inicio, fecha_fin)
    ), use_container_width=True
)