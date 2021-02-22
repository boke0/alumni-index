from mitama.app import App, Router
from mitama.utils.controllers import static_files
from mitama.utils.middlewares import SessionMiddleware, CsrfMiddleware
from mitama.app.method import view

from .controller import ProfileController


class App(App):
    name = 'Alumni図鑑'
    description = ''
    router = Router(
        [
            view("/static/<path:path>", static_files()),
            view("/create", ProfileController, 'create'),
            Router([
                view("/", ProfileController),
                view("/register", ProfileController, 'register'),
                view("/search", ProfileController, 'search'),
                view("/<id>", ProfileController, 'retrieve'),
            ], middlewares = [SessionMiddleware]),
        ],
        middlewares = [CsrfMiddleware]
    )
    @property
    def view(self):
        view = super().view
        return view
