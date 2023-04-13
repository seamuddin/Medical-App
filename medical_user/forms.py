from django import forms
from medical_user.models import CustomUser
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
