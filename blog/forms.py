from attr import fields
from django import forms
from blog.models import Post,Comment,UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('title', 'text', 'post_image')
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
        
class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')
        
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }