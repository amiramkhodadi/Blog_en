from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def user_login(request):

	# code zir braye inke karbari k login karde dg natone vared safe log in beshe
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			pass
	return render(request, 'account/login.html')

def user_logout(request):
	logout(request)
	return redirect('home')


def user_register(request):
	context = {'error':[]}
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		username = request.POST["username"]
		email = request.POST["email"]
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]

		if not(password1 == password2):
			context['error'].append("Passwords do not match")
			return render(request, 'account/register.html', context)
		if User.objects.filter(username=username).exists():
			context['error'].append("Username is taken")
			return render(request, 'account/register.html', context)

		user = User.objects.create_user(username, email, password2)
		user.save()
		login(request, user)
		return redirect('home')


	return render(request, 'account/register.html',context)