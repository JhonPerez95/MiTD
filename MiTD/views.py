from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login , logout

from .forms import LoginForm

def login_page(request):
	message = None
	if request.method == "POST": # Si hay una solicitud POST
		form = LoginForm(request.POST)
		if form.is_valid(): # Si el nombre de usr y psw estan incluidos en el formulario
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password) # Autentica usr y psw
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has identificado de modo correcto"
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Tu usuario o password incorrectos"
	else:
		form = LoginForm()
	return render(request,'login.html',{'message': message,'form': form})

def home_page(request):
	return render(request,'home_page.html')

def logout_view(request):
	logout(request)
	return redirect('home_page')