import pytest

from tests.base_functional_test import BaseFunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.functional_test
class AuthorRegisterTest(BaseFunctionalTest):
  def fill_form_dummy_data(self, form):
    fields = form.find_elements(By.TAG_NAME, 'input')
    for field in fields:
      if field.is_displayed():
        field.send_keys(' ' * 20)

  def get_form(self):
    return self.browser.find_element(
      By.XPATH,
      '/html/body/main/div[2]/form'
    )

  def form_field_test_with_callback(self, callback, email='test@test.com'):
    self.browser.get(self.live_server_url + '/authors/register/')
    form = self.get_form()
    self.fill_form_dummy_data(form)
    email_field = self.get_by_input_name(form, 'email').send_keys(email)


    callback(form)
    return form

  def parent_element(self, element):
      return element.find_element( By.XPATH, '..')

  def form_fields(self, form, field_name):
    field = self.get_by_input_name(form, field_name)
    field.send_keys(Keys.ENTER)
    form = self.get_form()
    return self.get_by_input_name(form, field_name)

  def test_username_fields_empty(self):
    def callback(form):
      username_field = self.form_fields(form, 'username')
      div_parent_field = self.parent_element(username_field)
      self.assertIn('This field is required', div_parent_field.text)
    self.form_field_test_with_callback(callback)

  def test_first_name_fields_empty(self):
    def callback(form):
      first_name_field = self.form_fields(form, 'first_name')
      div_parent_field = self.parent_element(first_name_field)
      self.assertIn('write your first name', div_parent_field.text)
    self.form_field_test_with_callback(callback)

  def test_last_name_fields_empty(self):
    def callback(form):
      last_name_field = self.form_fields(form, 'last_name')
      div_parent_field = self.parent_element(last_name_field)
      self.assertIn('write your last name', div_parent_field.text)
    self.form_field_test_with_callback(callback)

  def test_password_fields_empty(self):
    def callback(form):
      password_field = self.form_fields(form, 'password')
      div_parent_field = self.parent_element(password_field)
      self.assertIn('Password must not be empty', div_parent_field.text)

    self.form_field_test_with_callback(callback)

  def test_password2_fields_empty(self):
    def callback(form):
      password2_field = self.form_fields(form, 'password2')
      div_parent_field = self.parent_element(password2_field)
      self.assertIn('Please, repeat your password', div_parent_field.text)
    self.form_field_test_with_callback(callback)

  def test_invalid_email(self):
    def callback(form):
      email_field = self.form_fields(form, 'email')
      div_parent_field = self.parent_element(email_field)
      self.assertIn('Enter a valid email address.', div_parent_field.text)
    self.form_field_test_with_callback(callback, email='invalid@email')

  def test_user_valid_register_successfully(self):
    self.browser.get(self.live_server_url + '/authors/register/')
    form = self.get_form()

    self.get_by_input_name(form, 'username').send_keys('username')
    self.get_by_input_name(form, 'first_name').send_keys('first_name')
    self.get_by_input_name(form, 'last_name').send_keys('last_name')
    self.get_by_input_name(form, 'email').send_keys('email@test.com')
    self.get_by_input_name(form, 'password').send_keys('@Password1234')
    self.get_by_input_name(form, 'password2').send_keys('@Password1234')

    form.submit()

    self.assertIn(
      'Your user is created, please log in',
      self.browser.find_element(By.TAG_NAME, 'body').text
    )


