from mitama.app import Controller
from mitama.app.http import Response

from .model import Profile, Invite
from .forms import ProfileForm

class ProfileController(Controller):
    def handle(self, request):
        template = self.view.get_template("index.html")
        profs = Profile.list()
        return Response.render(template, {
            "profs": profs
        })
    def create(self, request):
        template = self.view.get_template("create.html")
        if request.method == "POST":
            try:
                form = ProfileForm(request.post())
                prof = Profile()
                prof.name = form["name"]
                prof.epoch = form["epoch"]
                prof.description = form["description"]
                prof.image = form["image"]
                prof.tags = form["tags"]
                prof.create()
            except ValidationError as err:
                return Response.render(template, {
                    "error": err.message,
                    "form": form
                })
        return Response.render(template)
    def retrieve(self, request):
        template = self.view.get_template("retrieve.html")
        prof = Profile.retrieve(request.params['profile'])
        return Response.render(template, {
            "prof": prof
        })
    def search(self, request):
        template = self.view.get_template("search.html")
        wordsets = [wordset.split(' ') for wordset in request.query['words'][0].split(',')]
        return Response.render(template, {
            "profs": profs
        })
