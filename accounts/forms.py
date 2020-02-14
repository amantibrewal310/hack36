from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Username",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Username'",
            'required':"",
            'type':"text"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'name':"email",
        'placeholder':"Enter email address",
        'pattern':"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$",'onfocus':"this.placeholder = ''", 
        'onblur':"this.placeholder = 'Enter email address'", 'class':"common-input mb-20 form-control",
        'required':"",
        'type':"email"

    }),required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your First Name",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter your First Name'",
            'required':"",
            'type':"text"
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your last name",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter your last name'",
            'required':"",
            'type':"text"
        }
    ))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter password",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter password'",
            'required':"",
            'type':"password"
        }
    ))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter password again",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter password again'",
            'required':"",
            'type':"password"
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields =(
            'email',
            'first_name',
            'last_name',
            # 'password',
        )
        # exclude = ()
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Username",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Username'",
            'required':"",
            'type':"text"
    }))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter password",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter password'",
            'required':"",
            'type':"password"
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

class EditProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Username",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Username'",
            'required':"",
            'type':"text"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'name':"email",
        'placeholder':"Enter email address",
        'pattern':"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$",'onfocus':"this.placeholder = ''", 
        'onblur':"this.placeholder = 'Enter email address'", 'class':"common-input mb-20 form-control",
        'required':"",
        'type':"email"

    }),required=True)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your First Name",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter your First Name'",
            'required':"",
            'type':"text"
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your last name",
            'class':"common-input mb-20 form-control",
            'onfocus':"this.placeholder = ''",
            'onblur':"this.placeholder = 'Enter your last name'",
            'required':"",
            'type':"text"
        }
    ))
    # password = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'placeholder':"Enter password",
    #         'class':"common-input mb-20 form-control",
    #         'onfocus':"this.placeholder = ''",
    #         'onblur':"this.placeholder = 'Enter password'",
    #         'required':"",
    #         'type':"password"
    #     }
    # ))

    class Meta:
        model = User
        fields =(
            'username',
            'email',
            'first_name',
            'last_name',
            # 'password',
        )
        # exclude = ()