from allauth.account.forms import LoginForm, SignupForm
from django import forms

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'placeholder': 'Nhập địa chỉ email của bạn',
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Nhập mật khẩu',
        })
        self.fields['remember'].label = "Lưu đăng nhập"
        self.fields['password'].help_text = "Bạn quên mật khẩu? <a href='{% url 'account_reset_password' %}'>Ấn vào đây</a>"
        
class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Thay đổi placeholder cho các trường
        self.fields['email'].widget = forms.TextInput(attrs={
            'placeholder': 'Nhập địa chỉ email của bạn',
            'class': 'form-control'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Nhập mật khẩu',
            'class': 'form-control'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Nhập lại mật khẩu',
            'class': 'form-control'
        })