import re

from django.core.exceptions import ValidationError



def add_attr(field, attr_name, attr_new_value):
  existing = field.widget.attrs.get(attr_name,'')
  field.widget.attrs[attr_name] = f'{existing} {attr_new_value}'.strip()

def add_placeholder(field, placeholder_val):
  add_attr(field, 'placeholder', placeholder_val)

def strong_password(password):
  regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

  if not regex.match(password):
    raise ValidationError((
      'Password must have at least one uppercase letter. '
      'One lowercase letter and one number. '
      'At least 8 characters'
    ),
      code = 'Invalid'
    )
