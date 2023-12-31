from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.form_utils import add_placeholder, strong_password




class RegisterForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    add_placeholder(self.fields['username'], 'Your username')
    add_placeholder(self.fields['email'], 'Your E-mail')
    add_placeholder(self.fields['first_name'], 'Ex.: John')
    add_placeholder(self.fields['last_name'], 'Ex.: Staviasz')
    add_placeholder(self.fields['password'], 'Your password')

  username = forms.CharField(
    label='Username',
    help_text='Required. the length should  be between 4 and 150 characters. '
              'Letters, digits and @/./+/-/_ only.',
    required=True,
    min_length=4,
    max_length=150,
    error_messages={
      'required': 'This field is required',
      'min_length': 'Username must have at least 4 characters',
      'max_length': 'Username must have less than 150 characters'
    },
  )

  first_name = forms.CharField(
    required=True,
    error_messages={ 'required': 'write your first name'},
    label='First name'
  )

  last_name = forms.CharField(
    required=True,
    error_messages={ 'required': 'write your last name'},
    label='Last name'
  )

  password = forms.CharField(
    required=True,
    error_messages={
      'required': 'Password must not be empty'
    },
    help_text=(
      'Password must have at least one uppercase letter. '
      'One lowercase letter and one number. '
      'At least 8 characters'
    ),
    validators=[strong_password],
    widget=forms.PasswordInput(),
    label='Password'
  )

  password2 = forms.CharField(
    required=True,
    error_messages={
      'required': 'Please, repeat your password'
    },
    widget=forms.PasswordInput(attrs={
      'placeholder': 'Repeat your password'
    }),
    label='Password confirmation'
  )

  email = forms.EmailField(
    required=True,
    error_messages={ 'required': 'Email is required'},
    label='Email address'
  )

  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      'password',
      'password2'
    ]

  def clean_email(self):
    email = self.cleaned_data.get('email', '')
    exists = User.objects.filter(email=email).exists()

    if exists:
      raise ValidationError(
        'User e-mail is already in use', code='invalid'
      )
    return email

  def clean(self):
    clean_data = super().clean()

    password = clean_data.get('password')
    password2 = clean_data.get('password2')

    if password != password2:
      raise ValidationError({
        'password': 'password and password confirmation must be equal',
        'password2': 'password and password confirmation must be equal'
      })

    return clean_data
