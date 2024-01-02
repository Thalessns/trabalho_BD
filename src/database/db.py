from mysql.connector import (connection);

@staticmethod
def connect():
    conn = connection.MySQLConnection(
        user        = "thalao",
        password    = "123456",
        database    = 'trabalho_bd',
        host        = "localhost",
        port        = 3306,
        auth_plugin = 'mysql_native_password'
    ); 
    return conn;
