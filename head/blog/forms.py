from django import forms
from .models import Post

class CommentForm(forms.ModelForm):
    author = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Ваше имя'
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш комментарий'
        })
    )
    class Meta:
        model = Post
        fields = ['author','body',]

