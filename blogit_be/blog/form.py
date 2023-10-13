from django import forms
from .models import Post,Category,Comment


# cats = [('conding','coding'),('sports','sports'),('entertainment','entertainment')]
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body','snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Type your title"}),
            'author': forms.TextInput(attrs={'class':'form-control','id':'elder','type':'hidden'}),
            'category': forms.Select( choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your snippet title"}),
            'is_published': forms.BooleanField()
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Type your title"}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
            # 'is_published': forms.BooleanField()

        }
class AdminEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','snippet','is_published')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':"Type your title"}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
            'snippet': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
            # 'is_published': forms.BooleanField()

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':"Type your content"}),
        }

