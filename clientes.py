import conexion

class clientes:
    dni = ''

    #CONSULTA PROPIA
    def consultaRegistro(sql_query, numRegistr):
        cursor = conexion.conecta()        
        try :
            cursor.execute( sql_query )
            data = cursor.fetchall()
            return ''.join(data[numRegistr])     
        except Exception as e :
            print("Exception : ", e)


    


        
