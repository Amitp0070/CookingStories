# from ckeditor.widgets import CKEditorWidget
# from django import forms
# from .models import Article

# class ArticleForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
    
#     class Meta:
#         model = Article
#         fields = ['title', 'content', 'image', 'topic']


from django import forms
from .models import Article  # Assuming you have an Article model
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # Use CKEditor for rich text editing

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter the title of the article'})
    )
    content = forms.CharField(
        widget=CKEditorUploadingWidget()  # Rich text editor for the content field using CKEditor
    )
    image = forms.ImageField(required=False)  # Optional image field
    publication_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget
    )
    city = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter the city related to the article'})
    )

    class Meta:
        model = Article  # Assuming the model name is Article
        fields = ['title', 'content', 'image', 'publication_date', 'city']
