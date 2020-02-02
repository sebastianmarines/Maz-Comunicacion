from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    email = forms.EmailField(label="Correo")
    phone = forms.CharField(max_length=15, label="Telefono")
    city = forms.CharField(max_length=50, label="Ciudad")
    message = forms.CharField(label='Mensaje',widget=forms.Textarea(
                        attrs={'placeholder': 'Escribe tu mensaje'}))
