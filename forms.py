from mitama.app.forms import Form, Field, FileField

class ProfileForm(Form):
    name = Field(required=True)
    epoch = Field(required=True)
    tags = Field(required=True)
    description = Field(required=True)
    image = FileField(required=True)

