from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
        
        
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit','작성합시다'))

# class BoardForm(forms.Form):
#     title=forms.CharField(
#         label='제목',
#         widget=forms.TextInput(attrs={
#             'placeholder': 'The title!',
#         }))
#     content=forms.CharField(
#         label='내용',
#         widget=forms.Textarea(attrs={
#             'row':5
#             'cols':50
#             'placeholder': 'Fill the content!',
#         }))
    
