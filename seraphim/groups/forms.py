from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import FormActions

from .models import Group


class GroupForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Group
        fields = '__all__'
