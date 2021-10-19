from django import forms
from django.forms.widgets import Textarea

class FormArticle(forms.Form):


    title = forms.CharField(
         label = "Título",
         max_length=40,
         # required=False,
         widget=forms.TextInput(
             attrs={
                 "placeholder": "Ingresá el título",
                 "class": "titulo_form_article"
             }
         )
    )
     
    content = forms.CharField(
         label = "Contenido",
         widget=forms.Textarea(
             attrs={
                 "placeholder": "Ingresá el contenido",
                 "class": "contenido_form_article"
             }
         )
    )

    # Esta es otra forma de configurar el Widget
    content.widget.attrs.update({
        "placeholder": "Ingresá el contenido",
        "class": "contenido_form_article",
        "id": "contenido_form"
    })

    public_options = [
        (1, "Sí"),
        (0, "No")
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options
    )
