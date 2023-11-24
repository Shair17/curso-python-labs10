from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm, AuthenticationForm

class LoginView(LoginView):
  def get(self, request):
    is_authenticated = request.user.is_authenticated

    if is_authenticated:
      return redirect('index')

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

class RegisterView(View):
<<<<<<< HEAD
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'users/register.html', {'form': form})
=======
  def get(self, request):
    is_authenticated = request.user.is_authenticated

    if is_authenticated:
      return redirect('index')

    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
>>>>>>> main

	def post(self, request):
		form = UserRegisterForm(request.POST)

<<<<<<< HEAD
		if form.is_valid():
			form.save()
			return redirect('index')
=======
    if form.is_valid():
      form.save()
      return redirect('index')
>>>>>>> main
