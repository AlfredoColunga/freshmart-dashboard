import streamlit as st

st.set_page_config(
            page_title='FreshMart',
            layout='wide',
            initial_sidebar_state='expanded'
        )

pages = {
    "Dashboards": [
        st.Page("ventas.py", title="Ventas"),
        st.Page("clientes.py", title="Clientes"),
    ]
}


pg = st.navigation(pages)
pg.run()