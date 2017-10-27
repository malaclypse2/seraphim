from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Character

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-CharacterForm'
        self.helper.form_class = 'Bootstrap4'
        self.helper.form_method = 'post'
        self.helper.form_action = 'characters:list'

        self.helper.add_input(Submit('submit', 'Submit'))
