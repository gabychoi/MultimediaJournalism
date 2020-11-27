from django.contrib.auth.models import User
from django import forms

class SignUpForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta :
        model = User
        # fields 에는 해당 모델에 대해 입력 받을 필드들을 나열한다.
        # + 추가 필드도 포함될 수 있다.
        fields = ['username', 'password', 'first_name', 'last_name', 'email',]