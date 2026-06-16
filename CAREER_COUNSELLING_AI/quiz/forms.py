from django import forms 
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=['name','email','phone','secondary_marks','higher_Secondary_marks','stream']
