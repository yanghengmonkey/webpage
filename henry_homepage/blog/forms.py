from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-area', 'placeholder': 'Enter your name'}
        ),
        required=True
    )
    class Meta:
        widgets = {'title': forms.TextInput(attrs={'size':100})}

class PostAdminForm(forms.ModelForm):
    class Meta:
        widgets = {'title': forms.TextInput(attrs={'size':10})}
