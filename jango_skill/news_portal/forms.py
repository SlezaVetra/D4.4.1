from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    "Форма для работы с новостями."

    class Meta:
        model = News
        fields = ["name", "chapter"]