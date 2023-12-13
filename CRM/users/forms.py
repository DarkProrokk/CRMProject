from django import forms

from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder':
            'Подтвердите пароль'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 3:
            raise forms.ValidationError('Имя пользователя должно содержать более 3 символов')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('Пароль должен содержать более 6 символов')
        if password.isdigit():
            raise forms.ValidationError('Пароль должен содержать хотя бы одну букву')
        if password.isalpha():
            raise forms.ValidationError('Пароль должен содержать хотя бы одну цифру')
        return password


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
