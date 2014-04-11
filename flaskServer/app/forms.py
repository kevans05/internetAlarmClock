from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.widgets import ListWidget
from wtforms.validators import Required

class creatAlarm(Form):
    day = TextField('day', validators = [Required()])
    mounth = TextField('mounth', validators = [Required()])
    year = TextField('year', validators = [Required()])
    hour = TextField('hour', validators = [Required()])
    min = TextField('min', validators = [Required()])
 #   selectingPreSet = ListWidget(html_tag = ,prefix_label=True)
    userSite = BooleanField('userSite', default = False)
    webaddress = TextField('webaddress', validators = [Required()])

class creatPresets(Form):
    presets1 = TextField('presets1', validators = [Required()])
    presets2 = TextField('presets2', validators = [Required()])
    presets3 = TextField('presets3', validators = [Required()])
    presets4 = TextField('presets4', validators = [Required()])
    presets5 = TextField('presets5', validators = [Required()])
    presets6 = TextField('presets6', validators = [Required()])

class setSetting(Form):
    location = TextField('location', validators = [Required()])