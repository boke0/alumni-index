from mitama.app import Controller
from mitama.app.http import Response
from mitama.app.forms import ValidationError

from .model import Profile,Tag
from .forms import ProfileForm

class ProfileController(Controller):
    def handle(self, request):
        template = self.view.get_template("index.html")
        print(template.__dict__)
        profs = Profile.list()
        return Response.render(template, {
            "title": "一覧",
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
                for tag_ in [tag.strip() for tag in form["tags"].split(",")]:
                    tag = Tag(tag_)
                    Tag.query.session.add(tag)
                    prof.tags.append(tag)
                Tag.query.session.commit()
                prof.lcm = form["lcm"] == "on"
                prof.mentor = form["mentor"] == "on"
                prof.alumnight = form["alumnight"] == "on"
                prof.create()
                template = self.view.get_template("thanks.html")
                return Response.render(template, {
                    "title": "図鑑登録",
                })
            except ValidationError as err:
                return Response.render(template, {
                    "title": "図鑑登録",
                    "error": err.message,
                })
        return Response.render(template)
    def retrieve(self, request):
        template = self.view.get_template("retrieve.html")
        prof = Profile.retrieve(request.params['id'])
        return Response.render(template, {
            "title": prof.name,
            "prof": prof
        })
    def search(self, request):
        template = self.view.get_template("search.html")
        wordsets = [wordset.split(' ') for wordset in request.query['words'][0].split(',')]
        return Response.render(template, {
            "title": "「" + request.query + "」の検索結果",
            "profs": profs
        })
