import streamlit as st
from style_manager import StyleManager
from data_manager import DataManager
from chart_creator import ChartCreator


styles = StyleManager("images/FreshMart-logo.png")


ventas_df = DataManager.load_csv("data/ventas_freshmart.csv")

sucursales_disponibles = DataManager.load_options(ventas_df, "Sucursal")
fecha_min, fecha_max, fecha_min_default = DataManager.load_dates(ventas_df, "Fecha")


styles.display_header("Dashboard de Ventas")


sucursales = st.sidebar.multiselect(
    "Sucursales:",
    options=sucursales_disponibles,
    default=sucursales_disponibles,
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


line_chart_col, _, pie_chart_col = st.columns([2, .2, 1])

with line_chart_col:
    st.altair_chart(
        ChartCreator.line_ventas_fecha_sucursal(
            DataManager.filter_sales_data(ventas_df, sucursales, fecha_inicio, fecha_fin)
        ), use_container_width=True
    )

with pie_chart_col:
    st.altair_chart(
        ChartCreator.pie_ventas_por_sucursal(
            DataManager.percent_sales_sucursal(ventas_df, sucursales, fecha_inicio, fecha_fin)
        ), use_container_width=True
    )

st.write("")

bar1_chart_col, _, bar2_chart_col = st.columns([1, .2, 2])

bar1_chart_col.altair_chart(
    ChartCreator.bar_top_productos(
        DataManager.group_cant_producto(ventas_df, sucursales, fecha_inicio, fecha_fin)
    ), use_container_width=True
)

bar2_chart_col.altair_chart(
    ChartCreator.bar_ventas_por_metodo(
        DataManager.group_metodo_pago(ventas_df, sucursales, fecha_inicio, fecha_fin)
    ), use_container_width=True
)