from django import forms
from orders.models import Order



class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше ИМЯ'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Ваша ФАМИЛИЯ'})
    )
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'YOUR@email.com'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7-***-***-**-**'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Ленинград, ул. Пушкина, дом 37-б кв. 9'})
    )

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone', 'address',)
