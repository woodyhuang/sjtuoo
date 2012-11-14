#coding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from account.models import ContactAddress


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactAddress
        exclude = ('user', 'is_default') 
    
    def save(self, user, commit=True):
        contact = super(ContactForm, self).save(commit=False)
        contact.user = user
        
        if commit:
            contact.save()
            
        return contact


class LoginForm(AuthenticationForm):
    """ Just change label name for username, cause we use email as username.
    """
    username = forms.EmailField(label=u'用户名（邮箱）')


class RegisterForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    Use email as username.
    """
    error_messages = {
        'duplicate_email': u'该邮箱已经被注册，请换一个试试吧~~',
        'password_mismatch': u'两次输入的密码不一致，请注意密码大小写敏感。',
    }
    email = forms.EmailField(label=u'邮箱')
    password1 = forms.CharField(label=u'密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'再次输入密码', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("email",)

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            User.objects.get(username=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])
        
        print 'to create user %s', user.email
        
        if commit:
            user.save()
        
        return user
