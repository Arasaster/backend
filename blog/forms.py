from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']  # Fields to display in the form
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }
