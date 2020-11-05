from django import forms
from .models import Comment
from django.forms import ModelForm, Textarea, CharField, EmailInput, TextInput


class EmailPostForm(forms.Form):
    name = forms.CharField(widget= TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Tên người gửi'}))
    email = forms.EmailField(widget= EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email người gửi'}))
    to = forms.EmailField(widget= EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email người nhận'}))
    comments = forms.CharField(required=False,
                               widget=TextInput(attrs={'class': 'form-control', 'id': 'body', 'placeholder': 'Bình luận của bạn', 'height': '129px'}))


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Tên của bạn'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email của bạn'}),
            'body': Textarea(attrs={'class': 'form-control', 'id': 'body', 'placeholder': 'Bình luận của bạn', 'height': '129px'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(widget=TextInput(attrs={'placeholder': 'Bạn đang tìm kiếm cái gì?'}))
