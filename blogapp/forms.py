from .models import Comment
from django import forms
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        foo = SummernoteTextField()
