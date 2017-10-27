from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Character

class CharacterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('save', 'save'))
    class Meta:
        model = Character
