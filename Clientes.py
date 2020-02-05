import conexion

class Clientes:
    
    def getDNI():
    cursor = conexion.conecta()
    
    sql_query = "SELECT DNI from Clientes";
    
    try :
        cursor.execute( sql_query );
        data = cursor.fetchone();
        print( "DNI: %s" %data );
       
    except Exception as e :
        print("Exception : ", e);
