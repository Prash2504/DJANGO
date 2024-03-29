from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'namma_pandit_app/home.html')

def register(request):
	if request.method == 'POST':
		import pdb;pdb.set_trace()
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'namma_pandit_app/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'namma_pandit_app/profile.html')
