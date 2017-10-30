from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Hidden, Div
from crispy_forms.bootstrap import FormActions

from .models import Combat, Heal, StatusEffect, StatusEffectType, Wound


class WoundForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WoundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        # Hide the Combat and Player inputs, if this is a bound form
        if self.is_bound:
            self.helper[0:2].wrap(Div, css_class="d-none")

    class Meta:
        model = Wound
        fields = '__all__'


class HealForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if self.is_bound:
            self.helper[0:2].wrap(Div, css_class="d-none")

    class Meta:
        model = Heal
        fields = '__all__'

class CombatForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CombatForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Combat
        fields = '__all__'
