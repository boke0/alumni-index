from mitama.app.forms import Form, Field, FileField

class ProfileForm(Form):
    name = Field(label='名前', required=True)
    epoch = Field(label='入会年度', required=True)
    tags = Field(label='ハッシュタグ', required=True)
    description = Field(label='自己紹介', required=True)
    image = FileField(label='写真', required=True)
    lcm = Field()
    mentor = Field()
    alumnight = Field()

