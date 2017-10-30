from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from .models import Combat, Heal, StatusEffect, StatusEffectType, Wound


class WoundForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WoundForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Wound
        fields = '__all__'


class HealForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

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
