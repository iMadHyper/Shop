from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import User


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SignupUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
        
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username', 
            'first_name', 
            'last_name',
            'image',
            'email', 
            'phone_number'
        )