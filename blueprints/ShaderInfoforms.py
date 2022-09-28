import wtforms
from wtforms.validators import length, email, EqualTo
from models import EmailCaptchaModel,UserModel

class ShaderInfoForm(wtforms.Form):
    id = wtforms.IntegerField()
    Date = wtforms.DateTimeField()
    Describe = wtforms.StringField()
    FilePath = wtforms.StringField()
    Project = wtforms.SelectField()