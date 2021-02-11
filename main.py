from mitama.app import App, Router
from mitama.utils.controllers import static_files
from mitama.app.method import view

from .controller import ProfileController


class App(App):
    name = 'Alumni図鑑'
    description = ''
    router = Router(
        [
            view("/", ProfileController),
            view("/register", ProfileController, 'register'),
            view("/create", ProfileController, 'create'),
            view("/search", ProfileController, 'search'),
            view("/:id", ProfileController, 'retrieve'),
            view("/static/<path:path>", static_files()),
        ]
    )
