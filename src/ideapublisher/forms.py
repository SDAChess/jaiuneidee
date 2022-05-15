from django.apps import apps
from django import forms

Idea = apps.get_model('ideacrawler', 'Idea')


class IdeaForm(forms.ModelForm):
    title = forms.CharField(
        label='Mon idée',
        max_length='80'
    )
    description = forms.CharField(
        widget=forms.Textarea,
        label='Description',
        max_length='1024',
        required=False
    )

    class Meta:
        model = Idea
        fields = ('title', 'description')
