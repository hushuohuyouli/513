from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import ValidationError,DataRequired,Length,Email,EqualTo

class SearchForm(FlaskForm):
    content = StringField('',render_kw={'style':'resize:none;','rows':4,'placeholder':'请输入查询内容...'})
    submit = SubmitField('查询')

