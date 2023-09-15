from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class fooditemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = "__all__"

class addUserFooditem(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = "__all__"

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']