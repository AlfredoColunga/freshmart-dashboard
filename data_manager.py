import pandas as pd
from datetime import timedelta

class DataManager:

    def load_csv(csv_file):
        df = pd.read_csv(csv_file)
        try:
            df['Fecha'] = pd.to_datetime(df['Fecha'])
        except:
            pass
        return df


    def load_options(df, column):
        return sorted(df[column].unique())


    def load_options_condition(df, column_condition, condition, column):
        if condition:
            return sorted(df[df[column_condition].isin(condition)][column].unique())
        else:
            return sorted(df[column].unique())


    def load_dates(df, column):
        max_date = df[column].max()
        return df[column].min(), max_date, max_date - timedelta(days=15)


    def filter_sales_data(df, sucursales, fecha_inicio, fecha_fin):
        filtered_df = df.copy()

        if sucursales:
            filtered_df = df[df["Sucursal"].isin(sucursales)]
        else:
            filtered_df = df

        filtered_df = filtered_df[
            (filtered_df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
            (filtered_df["Fecha"] <= pd.to_datetime(fecha_fin))
        ]
        return filtered_df.groupby(["Sucursal", "Fecha"])["Total Venta"].sum().reset_index()


    def percent_sales_sucursal(df, sucursales, fecha_inicio, fecha_fin):
        filtered_df = df.copy()

        if sucursales:
            filtered_df = df[df["Sucursal"].isin(sucursales)]
        else:
            filtered_df = df

        filtered_df = filtered_df[
            (filtered_df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
            (filtered_df["Fecha"] <= pd.to_datetime(fecha_fin))
        ]

        filtered_df = filtered_df.groupby("Sucursal")["Total Venta"].sum().reset_index()
        filtered_df["Porcentaje"] = (filtered_df["Total Venta"] / filtered_df["Total Venta"].sum() * 100)
        return filtered_df


    def group_metodo_pago(df, sucursales, fecha_inicio, fecha_fin):
        filtered_df = df.copy()

        if sucursales:
            filtered_df = df[df["Sucursal"].isin(sucursales)]
        else:
            filtered_df = df

        filtered_df = filtered_df[
            (filtered_df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
            (filtered_df["Fecha"] <= pd.to_datetime(fecha_fin))
        ]

        new_df = filtered_df.groupby('Método de Pago')['Total Venta'].sum().reset_index()
        return new_df.sort_values('Total Venta', ascending=True)


    def group_cant_producto(df, sucursales, fecha_inicio, fecha_fin):
        filtered_df = df.copy()

        if sucursales:
            filtered_df = df[df["Sucursal"].isin(sucursales)]
        else:
            filtered_df = df

        filtered_df = filtered_df[
            (filtered_df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
            (filtered_df["Fecha"] <= pd.to_datetime(fecha_fin))
        ]

        new_df = filtered_df.groupby(["SKU", "Nombre del Producto"]).agg({
            "Cantidad Vendida": "sum",
            "Total Venta": "sum"
        }).reset_index()

        new_df.columns = ["SKU", "Producto", "Cantidad Total Vendida", "Ingresos Totales"]
        return new_df.sort_values("Cantidad Total Vendida", ascending=False).head(3)


    def group_tipo_cliente(df, tipo_cliente, id_cliente):
        filtered_df = df.copy()

        if tipo_cliente:
            filtered_df = df[df["Tipo Cliente"].isin(tipo_cliente)]
        else:
            filtered_df = df

        if id_cliente:
            filtered_df = filtered_df[filtered_df["ID Cliente"] == id_cliente]

        new_df = filtered_df.groupby("Tipo Cliente")["Total Gastado"].sum().reset_index()
        return new_df.sort_values("Total Gastado", ascending=False)


    def group_freq_compra(df, tipo_cliente, id_cliente):
        filtered_df = df.copy()

        if tipo_cliente:
            filtered_df = df[df["Tipo Cliente"].isin(tipo_cliente)]
        else:
            filtered_df = df

        if id_cliente:
            filtered_df = filtered_df[filtered_df["ID Cliente"] == id_cliente]

        new_df = filtered_df.groupby("Tipo Cliente")["Frecuencia de Compra"].sum().reset_index()

        data_dict = dict(zip(new_df["Tipo Cliente"], new_df["Frecuencia de Compra"]))
        for key in ["Nuevo", "Frecuente", "VIP"]:
            data_dict.setdefault(key, 0)
        return data_dict["Nuevo"], data_dict["Frecuente"], data_dict["VIP"]


    def filter_customer_data(df, tipo_cliente, id_cliente):
        filtered_df = df.copy()

        if tipo_cliente:
            filtered_df = df[df["Tipo Cliente"].isin(tipo_cliente)]
        else:
            filtered_df = df

        if id_cliente:
            filtered_df = filtered_df[filtered_df["ID Cliente"] == id_cliente]
        return filtered_df.sort_values("Total Gastado", ascending=False).head(5)


    def merge_data(df_1, df_2, tipo_cliente, id_cliente, fecha_inicio, fecha_fin):
        df_v = df_1.copy()
        df_c = df_2.copy()

        df_v = df_v.rename(columns={"Cliente ID": "ID Cliente"})
        df_unificado = df_v.merge(df_c, on="ID Cliente", how="left")

        columnas_finales = ["Fecha", "Total Venta", "ID Cliente", "Tipo Cliente"]
        df_unificado = df_unificado[columnas_finales]

        if tipo_cliente:
            filtered_df = df_unificado[df_unificado["Tipo Cliente"].isin(tipo_cliente)]
        else:
            filtered_df = df_unificado

        if id_cliente:
            filtered_df = filtered_df[filtered_df["ID Cliente"] == id_cliente]

        filtered_df = filtered_df[
            (filtered_df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
            (filtered_df["Fecha"] <= pd.to_datetime(fecha_fin))
        ]
        return filtered_df.groupby(["Tipo Cliente", "Fecha"])["Total Venta"].sum().reset_index()