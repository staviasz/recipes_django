from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from authors.forms import RegisterForm, LoginForm


def register_view(request):
  register_form_data = request.session.get('register_form_data', None)
  form = RegisterForm(register_form_data)

  return render(request, 'authors/pages/index.html', {
    'form': form,
    'page_title': 'Register',
    'form_action': reverse('author:create')
  })

def register_create(request):
  if not request.POST:
    raise Http404

  POST = request.POST
  request.session['register_form_data'] = POST
  form = RegisterForm(POST)

  if form.is_valid():
    user = form.save(commit=False)
    user.set_password(user.password)
    user.save()
    messages.success(request, 'Your user is created, please log in')

    del(request.session['register_form_data'])
    return redirect(reverse('author:login'))

  return redirect('author:register')

def login_view(request):
  form = LoginForm()
  return render(request, 'authors/pages/index.html', {
    'page_title': 'Login',
    'form': form,
    'form_action': reverse('author:login_create')
   })

def login_create(request):
  if not request.POST:
    raise Http404

  login_url = reverse('author:login')

  form = LoginForm(request.POST)
  if form.is_valid():
    authenticated_user = authenticate(
      username=form.cleaned_data.get('username', ''),
      password=form.cleaned_data.get('password', '')
    )

    if authenticated_user is not None:
      messages.success(request, 'Your are logged in')
      login(request, authenticated_user)
    else:
      messages.error(request, 'Invalid credentials')
  else:
    messages.error(request, 'Invalid login')

  return redirect(login_url)

@login_required(login_url='author:login', redirect_field_name='next')
def logout_view(request):
  if not request.POST:
    messages.error(request, 'Invalid logout request')
    return redirect(reverse('author:login'))

  if request.POST.get('username') != request.user.username:
    messages.error(request, 'Invalid logout user')
    return redirect(reverse('author:login'))

  messages.success(request, 'Logged out successfully')
  logout(request)
  return redirect(reverse('author:login'))
