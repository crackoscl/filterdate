async obtenerDatosDia(data, desde, hasta, timeZone, id_bus, tipo_dato) {

        try {

            let f_desde = new Date(desde);
            let f_hasta = new Date(hasta);

            console.log("f_desde: ",  f_desde )
            console.log("f_hasta: " , f_hasta)
            // f_desde = new Date(f_desde.setHours(f_desde.getHours() - 4));
            // f_hasta = new Date(f_hasta.setHours(f_hasta.getHours() - 4));

            if (tipo_dato == 70) {
                                             
                let bus_data = data.filter(d => d.equipos_id == id_bus);
                 //console.log("bus_data 70", bus_data)
                 
                let bus_fecha_data = bus_data.filter(d => {
                    
                    let f_actual = new Date(d.created_at);
                    
                    console.log("f_actualsss: ", f_actual)
                    // f_actual.setHours(f_actual.getHours() - 4);
                    f_actual.setHours(f_actual.getHours() - timeZone);
                    console.log("f_actual xxx", f_actual)
                    console.log("f_desde: ",  f_desde )
                    console.log("resultado: ", (f_actual >= f_desde && f_actual <= f_hasta))
                    return (f_actual >= f_desde && f_actual <= f_hasta)
                        
                });
                //console.log("bus_fecha_data: ", bus_fecha_data)               
                return bus_fecha_data;
                

            } else { //TIPO: 73, 78, 80

                // Pequeña optimización. Se cambia el forof y se utiliza el filter
                let bus_data = data.filter(d => d.id_bus == id_bus);

                let bus_fecha_data = bus_data.filter(d => {

                    let f_actual = new Date(d.inicio_de_carga);
                    console.log("f_actualccc: ", f_actual)
                   
                    f_actual.setHours(f_actual.getHours() - timeZone);
                    console.log("f_actual else", f_actual)
                    console.log("f_desde: ",  f_desde )
                    console.log("resultado: ", (f_actual >= f_desde && f_actual <= f_hasta))
                    return (f_desde <= f_actual && f_actual <= f_hasta);
                });

                return bus_fecha_data;
            }

        } catch (error) {

            console.log('obtenerDatosDia() =>', error);

            return [];
        }
    }