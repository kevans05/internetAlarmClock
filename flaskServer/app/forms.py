from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.widgets import ListWidget
from wtforms.validators import Required

class LoginForm(Form):
    selectingPreSet = ListWidget(html_tag = ,prefix_label=True)
    userSite = BooleanField('userSite', default = False)
    webaddress = TextField('webaddress', validators = [Required()])
