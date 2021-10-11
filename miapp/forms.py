from django import forms
from django.forms.widgets import Textarea

class FormArticle(forms.Form):

     title = forms.CharField(
         label = "Título"
     )
     
     content = forms.CharField(
         label = "Contenido",
         widget=forms.Textarea
     )

     '''public = forms.BooleanField(
         label="public"
     )'''
