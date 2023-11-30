# Rutas de las APIs

from my_framework.app import app


@app.get("/users")
def get_users():
    # Obtener la lista de usuarios
    users = app.database.query("SELECT * FROM users").all()

    return users
