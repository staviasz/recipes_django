from unittest import TestCase
from django.test import TestCase as DjangoTest
from django.urls import reverse
from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterFormUnitTest(TestCase):

  @parameterized.expand([
    ('username','Your username'),
    ('email','Your E-mail'),
    ('first_name','Ex.: John'),
    ('last_name','Ex.: Staviasz'),
    ('password','Your password'),
    ('password2','Repeat your password')
  ])
  def test_fields_placeholder(self, field, placeholder):
    form = RegisterForm()
    current_placeholder = form[field].field.widget.attrs['placeholder']
    self.assertEqual(placeholder, current_placeholder)

  @parameterized.expand([
    ('username','Required. the length should  be between 4 and 150 characters. '
                'Letters, digits and @/./+/-/_ only.'),
    ('password',(
      'Password must have at least one uppercase letter. '
      'One lowercase letter and one number. '
      'At least 8 characters'
    ))

  ])
  def test_fields_help_text(self, field, needed):
    form = RegisterForm()
    current = form[field].field.help_text
    self.assertEqual(needed, current)

  @parameterized.expand([
    ('username','Username'),
    ('email','Email address'),
    ('first_name','First name'),
    ('last_name','Last name'),
    ('password','Password'),
    ('password2','Password confirmation')
  ])
  def test_fields_label(self, field, needed):
    form = RegisterForm()
    current = form[field].field.label
    self.assertEqual(needed, current)


class AuthorRegisterFormIntegrationTest(DjangoTest):
  def setUp(self, *args, **kwargs):
    self.form_data = {
      'username':'user',
      'email':'email@anytest.com',
      'first_name':'First name',
      'last_name':'Last name',
      'password':'Str0ngP@ssword',
      'password2':'Str0ngP@ssword',
    }
    return super().setUp(*args, **kwargs)

  @parameterized.expand([
    ('username', 'This field is required'),
    ('first_name', 'write your first name'),
    ('last_name', 'write your last name'),
    ('password', 'Password must not be empty'),
    ('password2', 'Please, repeat your password'),
    ('email', 'Email is required')
  ])
  def test_fields_cannot_be_empty(self, field, msg):
    self.form_data[field] = ''
    url = reverse('author:create')
    response = self.client.post(url, data=self.form_data, follow=True)

    self.assertIn(msg, response.content.decode('utf-8'))

  def test_username_field_min_length_should_be_4(self):
    self.form_data['username'] = 'tes'
    url = reverse('author:create')
    response = self.client.post(url, data=self.form_data, follow=True)
    msg = 'Username must have at least 4 characters'

    self.assertIn(msg , response.content.decode('utf-8'))
    # self.assertIn(msg, response.context['form'].errors.get('username'))

  def test_username_field_max_length_should_be_150(self):
    self.form_data['username'] = 'A' * 151
    url = reverse('author:create')
    response = self.client.post(url, data=self.form_data, follow=True)
    msg = 'Username must have less than 150 characters'

    self.assertIn(msg , response.content.decode('utf-8'))
    # self.assertIn(msg, response.context['form'].errors.get('username'))

  def test_password_field_have_lower_upper_case_letters_and_numbers(self):
    self.form_data['password'] = 'abc123'
    url = reverse('author:create')
    response = self.client.post(url, data=self.form_data, follow=True)
    msg = (
      'Password must have at least one uppercase letter. '
      'One lowercase letter and one number. '
      'At least 8 characters'
    )

    # self.assertIn(msg , response.content.decode('utf-8'))
    self.assertIn(msg, response.context['form'].errors.get('password'))

  def test_password_and_password_confirmation_are_equal(self):
    self.form_data['password'] = '@AAabc123'
    self.form_data['password2'] = '@AAabc1234'
    url = reverse('author:create')
    response = self.client.post(url, data=self.form_data, follow=True)
    msg = 'password and password confirmation must be equal'

    # self.assertIn(msg , response.content.decode('utf-8'))
    self.assertIn(msg, response.context['form'].errors.get('password'))

    self.form_data['password'] = '@AAabc123'
    self.form_data['password2'] = '@AAabc123'

    self.assertIn(msg , response.content.decode('utf-8'))

  def test_send_get_request_to_register_create_view_returns_404(self):
    url = reverse('author:create')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_email_must_be_unique(self):
    url = reverse('author:create')
    self.client.post(url, data=self.form_data, follow=True)
    response = self.client.post(url, data=self.form_data, follow=True)
    msg = 'User e-mail is already in use'

    self.assertIn(msg, response.context['form'].errors.get('email'))
    self.assertIn(msg , response.content.decode('utf-8'))

  def test_author_created_can_login(self):
    url = reverse('author:create')

    self.form_data.update({
      'username': 'usertest',
      'password': '@Abc12345',
      'password2': '@Abc12345'
    })

    self.client.post(url, data=self.form_data, follow=True)
    is_authenticated = self.client.login(
      username = 'usertest',
      password = '@Abc12345'
    )

    self.assertTrue(is_authenticated)


