from django import forms
from .models import MyPost


class PostCreatForm(forms.ModelForm):
    """Форма"""

    class Meta:
        model = MyPost
        fields = '__all__'  # все поля