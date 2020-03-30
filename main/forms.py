from django import forms
from django.contrib.auth import authenticate, get_user_model
from .models import Message

User = get_user_model()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email Address'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Password'
    }))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placholder' : 'Password'
    }))
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Incorrect Username or Password")
        return super(LoginForm, self).clean(*args, **kwargs)


class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Write Your Message'
    }))
    sent_by = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Your Name (Optional)'
    }))
    class Meta:
        model = Message
        fields = ['text', 'sent_by']
    




