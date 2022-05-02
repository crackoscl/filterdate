from datetime import datetime, timedelta
​
​
def obtener_datos(data, desde, hasta, timezone, id_bus, tipo_dato):
    f_desde = datetime.strptime(desde, "%Y-%m-%d")
    f_hasta = datetime.strptime(hasta, "%Y-%m-%d")
​
    if tipo_dato == 70:
        datos = [x for x in data if (f_actual := datetime.strptime(
            x['created_at'], "%Y-%m-%d %H:%M:%S") - timedelta(hours=timezone)) >= f_desde and f_actual <= f_hasta and x['equipos_id'] == id_bus]
​
    else:
        datos = [x for x in data if f_desde <= (f_actual := datetime.strptime(
            x['created_at'], "%Y-%m-%d %H:%M:%S") - timedelta(hours=timezone)) and f_actual <= f_hasta and x['id_bus'] == id_bus]
​
    return list(datos)
​
​
data_list = [{'id': 224495167, 'valor': '85387.42', 'tipos_datos_id': 70, 'created_at': '2022-01-04 04:10:58', 'equipos_id': 85, 'nombre': 'BUS 32'},{'id': 224495167, 'valor': '85387.42', 'tipos_datos_id': 70, 'created_at': '2022-01-04 04:10:58', 'equipos_id': 85, 'nombre': 'BUS 32'}, {'id': 224494680, 'tipos_datos_id': 70,
                                                                                                                                                       'created_at': '2022-01-05 04:57:11', 'equipos_id': 92, 'nombre': 'BUS 64'}, {'id': 224494502, 'valor': '85387.42', 'tipos_datos_id': 70, 'created_at': '2022-01-05 04:53:37', 'equipos_id': 85, 'nombre': 'BUS 32'}]
​
# desde = "2022-01-04"
# hasta= "2022-01-05"
# timezone=4
# bus=85
# tipo_dato=70
​
print(obtener_datos(data_list, desde='2022-01-04',
      hasta='2022-01-05', timezone=4, id_bus=85, tipo_dato=70))
