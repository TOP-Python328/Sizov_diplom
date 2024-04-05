from django import forms

class AddLaboratoryForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20,
    )
    img = forms.CharField(
        label='Картинка',
        max_length=20,
    )