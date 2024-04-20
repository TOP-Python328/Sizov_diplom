from django import forms

from laboratories.models import Laboratory


class AddLaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = "__all__"
