from mysql.connector import (connection);

def connect():
    conn = connection.MySQLConnection(
        user        = "",
        password    = "",
        database    = '',
        host        = "",
        port        = ,
        auth_plugin = 'mysql_native_password'
    ); 
    return conn;
