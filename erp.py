#!/usr/bin/python3
import conexion

def consultas():
    cursor = conexion.conecta()
    
    sql_query = "SELECT Nombre from Clientes";
    
    try :
        cursor.execute( sql_query );
        data = cursor.fetchone();
        print( "Database Version: %s" %data );
       
    except Exception as e :
        print("Exception : ", e);
        

consultas()