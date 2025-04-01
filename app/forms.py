from django import forms
from .models import ArticleImage
from .widgets import MultipleFileInput

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='Фото',
        widget=MultipleFileInput())
    class Meta:
        model = ArticleImage
        fields = '__all__'
