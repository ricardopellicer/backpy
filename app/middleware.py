# Middleware

from my_framework.app import app


class AuthMiddleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, request, response):
        # Verificar la autenticación
        if not request.user.is_authenticated:
            # Devolver un error de autorización
            response.status_code = 401
            return response

        return self.app(request, response)


app.middlewares.append(AuthMiddleware())
