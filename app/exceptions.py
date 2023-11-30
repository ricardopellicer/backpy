# Excepciones

class AppException(Exception):

    """
    Excepcion general del framework.
    """

    pass


class DatabaseException(AppException):

    """
    Excepcion de la base de datos.
    """

    pass


class AuthenticationException(AppException):

    """
    Excepcion de autenticación.
    """

    pass
