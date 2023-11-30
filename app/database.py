# Acceso a la base de datos

import pymysql
from my_framework.config import Config


def connect():
    # Conectarse a la base de datos
    return pymysql.connect(
        Config.database_uri,
        user=Config.database_user,
        password=Config.database_password,
    )


def close(connection):
    # Cerrar la conexión a la base de datos
    connection.close()
