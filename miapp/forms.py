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

    public_options = [
        (1, "Sí"),
        (0, "No")
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
