"""from django import forms 
from .models import Pizza, Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        #fields = ['text']
        #label = {'Pizza Type': ':'}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        #fields = ['text']
        #label = {'Topping:': ':'}

        #widgets = {'text': forms.Textarea(attrs={'cols':50})}
    """