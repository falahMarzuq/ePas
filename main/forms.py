from django.forms import ModelForm
from main.models import Products
from main.models import Accounts

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description"]

class Signup(ModelForm):
    class Meta:
        model = Accounts
        fields = ["first_name", "last_name", "username", "email", "password"]