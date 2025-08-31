import altair as alt

class ChartCreator:

    def line_ventas_fecha_sucursal(data):
        chart = alt.Chart(data).mark_line(point=True, strokeWidth=2).encode(
            x=alt.X('Fecha:T',
                    title='Fecha',
                    axis=alt.Axis(format='%d/%m/%Y', titleFontSize=14, labelFontSize=13, labelAngle=-45)),
            y=alt.Y('Total Venta:Q',
                    title='Total de Ventas ($)',
                    axis=alt.Axis(format='$,.0f', titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Sucursal:N',
                            title='Sucursal',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=alt.Legend(
                                orient='top',
                                direction='horizontal',
                                title=None,
                                labelLimit=0,
                                padding=0
                            )),
            tooltip=['Sucursal:N',
                    alt.Tooltip('Fecha:T', format='%d/%m/%Y', title='Fecha'),
                    alt.Tooltip('Total Venta:Q', format='$,.0f', title='Total Ventas')]
        ).properties(
            width=700,
            height=400,
            title=alt.TitleParams(
                text='Ventas a lo Largo del Tiempo por Sucursal',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def pie_ventas_por_sucursal(data):
        chart = alt.Chart(data).mark_arc(
            innerRadius=50
        ).encode(
            theta=alt.Theta('Total Venta:Q', title='Total de Ventas'),
            color=alt.Color('Sucursal:N',
                            title='Sucursal',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=alt.Legend(
                                orient='right',
                                #direction='horizontal',
                                title=None,
                                labelLimit=0,
                                #symbolOffset=75,
                                #padding=50,
                            )),
            tooltip=[
                alt.Tooltip('Sucursal:N', title='Sucursal'),
                alt.Tooltip('Total Venta:Q', format='$,.0f', title='Total Ventas'),
                alt.Tooltip('Porcentaje:Q', format='.2f', title='Porcentaje (%)')
            ]
        ).properties(
            title=alt.TitleParams(
                text='Participación por Sucursal',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def bar_top_productos(data):
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('Producto:N',
                    title='Producto',
                    sort=alt.EncodingSortField(field='Cantidad Total Vendida', order='descending'),
                    axis=alt.Axis(labelAngle=-45, titleFontSize=14, labelFontSize=13)),
            y=alt.Y('Cantidad Total Vendida:Q',
                    title='Cantidad Total Vendida',
                    axis=alt.Axis(titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Producto:N',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=None),
            tooltip=['Producto:N', 'Cantidad Total Vendida:Q', alt.Tooltip('Ingresos Totales:Q', format='$,.0f', title='Total Ventas')],
            stroke=alt.value('white'),
            strokeWidth=alt.value(1)
        ).properties(
            title=alt.TitleParams(
                text='Top 3 Productos más Vendidos',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def bar_ventas_por_metodo(data):
        chart = alt.Chart(data).mark_bar(size=35).encode(
            x=alt.X('Total Venta:Q',
                    title='Total de Ventas ($)',
                    axis=alt.Axis(format='$,.0f', titleFontSize=14, labelFontSize=13)),
            y=alt.Y('Método de Pago:N',
                    title='Método de Pago',
                    sort=alt.EncodingSortField(field='Total Venta', order='descending'),
                    axis=alt.Axis(titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Total Venta:Q',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=None),
            tooltip=['Método de Pago:N', alt.Tooltip('Total Venta:Q', format='$,.0f', title='Total Ventas')],
            stroke=alt.value('white'),
            strokeWidth=alt.value(1)
        ).properties(
            height=345,
            title=alt.TitleParams(
                text='Ventas por Método de Pago',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def bar_ingreso_tipo_cliente(data):
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('Tipo Cliente:N',
                    title='Tipo de Cliente',
                    sort=alt.EncodingSortField(field='Total Gastado', order='descending'),
                    axis=alt.Axis(labelAngle=-45, titleFontSize=14, labelFontSize=13)),
            y=alt.Y('Total Gastado:Q',
                    title='Total Gastado ($)',
                    axis=alt.Axis(format='$,.0f', titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Tipo Cliente:N',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=None),
            tooltip=['Tipo Cliente:N', alt.Tooltip('Total Gastado:Q', format='$,.0f', title='Total Gastado')],
            stroke=alt.value('white'),
            strokeWidth=alt.value(1)
        ).properties(
            title=alt.TitleParams(
                text='Ingresos por Tipo de Cliente',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def bar_ingresos_por_cliente(data):
        chart = alt.Chart(data).mark_bar().encode(
            x=alt.X('Total Gastado:Q',
                    title='Total de Gastado ($)',
                    axis=alt.Axis(format='$,.0f', titleFontSize=14, labelFontSize=13)),
            y=alt.Y('ID Cliente:N',
                    title='ID Cliente',
                    sort=alt.EncodingSortField(field='Total Gastado', order='descending'),
                    axis=alt.Axis(titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Total Gastado:Q',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=None),
            tooltip=['ID Cliente:N', 'Nombre:N', alt.Tooltip('Total Gastado:Q', format='$,.0f', title='Total Gastado')],
            stroke=alt.value('white'),
            strokeWidth=alt.value(1)
        ).properties(
            height=345,
            title=alt.TitleParams(
                text='Top 5 Clientes que Generan más Ingresos',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart


    def line_ventas_tipo_cliente(data):
        chart = alt.Chart(data).mark_line(point=True, strokeWidth=2).encode(
            x=alt.X('Fecha:T',
                    title='Fecha',
                    axis=alt.Axis(format='%d/%m/%Y', titleFontSize=14, labelFontSize=13, labelAngle=-45)),
            y=alt.Y('Total Venta:Q',
                    title='Total de Ventas ($)',
                    axis=alt.Axis(format='$,.0f', titleFontSize=14, labelFontSize=13)),
            color=alt.Color('Tipo Cliente:N',
                            scale=alt.Scale(scheme='yellowgreen'),
                            legend=alt.Legend(
                                orient='top',
                                direction='horizontal',
                                title=None,
                                labelLimit=0,
                                padding=0
                            )),
            tooltip=['Tipo Cliente:N',
                    alt.Tooltip('Fecha:T', format='%d/%m/%Y', title='Fecha'),
                    alt.Tooltip('Total Venta:Q', format='$,.0f', title='Total Ventas')]
        ).properties(
            width=700,
            height=400,
            title=alt.TitleParams(
                text='Ventas a lo Largo del Tiempo por Tipo de Cliente',
                fontSize=16,
                anchor='middle',
                offset=10
            )
        )
        return chart