import conexion

class clientes:
    dni = ''    
    def getDni():
        cursor = conexion.conecta()        
        sql_query = "SELECT DNI from Clientes";       
        try :
            cursor.execute( sql_query );
            data = cursor.fetchone();
            print( "Database Version: %s" %data );
        
        except Exception as e :
            print("Exception : ", e);

    def getNombre():
        cursor = conexion.conecta()        
        sql_query = "SELECT nombre from Clientes";       
        try :
            cursor.execute( sql_query );
            data = cursor.fetchone();
            print( "Database Version: %s" %data );
        
        except Exception as e :
            print("Exception : ", e);

    def getApellidos():
        cursor = conexion.conecta()        
        sql_query = "SELECT apellidos from Clientes";       
        try :
            cursor.execute( sql_query );
            data = cursor.fetchone();
            print( "Database Version: %s" %data );
        
        except Exception as e :
            print("Exception : ", e);
            
    def getGenero():
        cursor = conexion.conecta()        
        sql_query = "SELECT apellidos from Clientes";       
        try :
            cursor.execute( sql_query );
            data = cursor.fetchone();
            print( "Database Version: %s" %data );
        
        except Exception as e :
            print("Exception : ", e);

        
