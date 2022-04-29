import datetime


def obtener_datos(data,desde,hasta,timezone,id_bus,tipo_dato):
    datos = []
    f_desde = datetime.datetime.strptime(desde,"%Y-%m-%d")
    f_hasta =  datetime.datetime.strptime(hasta,"%Y-%m-%d")
    
    if tipo_dato == 70:
        bus_data = [x for x in data if x['equipos_id'] == id_bus]
        for dato in bus_data:
            f_actual = datetime.datetime.strptime(dato['created_at'],"%Y-%m-%d %H:%M:%S" )
            hora_fecha= f_actual.hour
            dt= hora_fecha - timezone
            f_actual= f_actual.replace(hour=dt)
            if f_actual>= f_desde and f_actual <= f_hasta:
                 datos.append(dato)

    else:
        bus_data = [x for x in data if x['id_bus'] == id_bus]
        for dato in bus_data:
            f_actual = datetime.datetime.strptime(dato['inicio_de_carga'],"%Y-%m-%d %H:%M:%S" )
            hora_fecha= f_actual.hour
            dt = hora_fecha - timezone
            f_actual= f_actual.replace(hour=dt)
            if f_desde <= f_actual and f_actual <= f_hasta:
                dato.append(dato)
    
    return datos


data_list = [{'id': 224495167, 'valor': '85387.42', 'tipos_datos_id': 70, 'created_at': '2022-01-04 04:10:58', 'equipos_id': 85, 'nombre': 'BUS 32'}, {'id': 224494680, 'tipos_datos_id': 70, 'created_at': '2022-01-05 04:57:11', 'equipos_id': 92, 'nombre': 'BUS 64'}, {'id': 224494502, 'valor': '85387.42', 'tipos_datos_id': 70, 'created_at': '2022-01-05 04:53:37', 'equipos_id': 85, 'nombre': 'BUS 32'}]

# desde = "2022-01-04" 
# hasta= "2022-01-05"
# timezone=4
# bus=85
# tipo_dato=70  

print(obtener_datos(data_list,desde='2022-01-04',hasta='2022-01-05',timezone=4,id_bus=85,tipo_dato=70)) 
