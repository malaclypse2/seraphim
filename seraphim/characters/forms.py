from django.forms import ModelForm, Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div
from crispy_forms.bootstrap import FormActions

from .models import Character

class CharacterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['icon'].choices.queryset.order_by('sort_key')
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        # Hide the owner.  
        self.helper['owner'].wrap(Div, css_class="d-none")

    class Meta:
        model = Character
        fields = '__all__'
