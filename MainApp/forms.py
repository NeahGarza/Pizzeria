from django import forms 
from .models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        label = {'Pizza Type': ':'}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['pizza', 'name']
        label = {'Topping:': ':'}

        widgets = {'text': forms.Textarea(attrs={'cols':50})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        label = {'Comment': ':'}

        widgets = {'text': forms.Textarea(attrs={'cols':80})}