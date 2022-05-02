from django import forms
from .models import *

#
# class AddComment(forms.ModelForm):
#     class Meta:
#         model = CompleteOrder
#         fields = [
#             'comments'
#         ]
#         widgets = {
#             'comments': forms.Textarea(attrs={'cols':60, 'rows':10})
#         }


class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск", widget=forms.TextInput())
