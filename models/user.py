# Modelo de usuario

from my_framework.orm import ORM


class User(ORM):

    __tablename__ = "users"

    id = ORM.Column(ORM.Integer, primary_key=True)
    name = ORM.Column(ORM.String)
    email = ORM.Column(ORM.String)
