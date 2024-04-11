from django import forms

from laboratories.models import Laboratory


class AddLaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = "__all__"
#     title = forms.CharField(
#         label='Название',
#         max_length=20,
#     )
#     img = forms.CharField(
#         label='Картинка',
#         max_length=20,
#     )