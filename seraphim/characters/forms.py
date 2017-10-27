from django.forms import ModelForm
from crispy_forms.helper import FormHelper
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