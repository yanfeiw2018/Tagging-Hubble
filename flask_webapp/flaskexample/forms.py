from wtforms import Form, StringField, SelectField
 
class SearchForm(Form):
    choices = [('Keyword', 'Keyword')]
    select = SelectField( choices=choices)
    search = StringField('')