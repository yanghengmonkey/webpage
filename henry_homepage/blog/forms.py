from django import forms

class PostCharForm(forms.ModelForm):
    class Meta:
        widgets = { 'caption': forms.TextInput(attrs={'size': 80})}
