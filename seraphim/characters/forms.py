from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Character

class CharacterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class='col-sm-4'
        self.helper.field_class='col-sm-8'
        self.helper.layout.append(Submit('save', 'save'))
    class Meta:
        model = Character
