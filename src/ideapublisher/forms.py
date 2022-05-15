from django import forms


class IdeaForm(forms.Form):
    idea = forms.CharField(
        label='Mon idée',
        max_length='80'
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='Description',
        max_length='1024',
        required=False
    )
