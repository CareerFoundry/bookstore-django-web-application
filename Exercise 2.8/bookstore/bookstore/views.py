from django.shortcuts import render, redirect	
#Django authentication libraries			
from django.contrib.auth import authenticate, login, logout	
#Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm	 

#define a function view called login_view that takes a request from user
def login_view(request):
	#initialize:
	#error_message to None									
	error_message = None	
	#form object with username and password fields								
	form = AuthenticationForm()								

	#when user hits "login" button, then POST request is generated
	if request.method == 'POST':		
		#read the data sent by the form via POST request					
		form =AuthenticationForm(data=request.POST)	

		#check if form is valid
		if form.is_valid():									
			username=form.cleaned_data.get('username')		#read username
			password = form.cleaned_data.get('password')	#read password

			#use Django authenticate function to validate the user
			user=authenticate(username=username, password=password)	
			if user is not None:					#if user is authenticated
				login(request, user)				#then use pre-defined Django function to login
				return redirect('sales:records')	#and send the user to desired page
		else:												#in case of error
		    error_message ='ooops.. something went wrong'	#print error message

	#prepare data to send from view to template
	context ={												
		'form': form,										#send the form data
		'error_message': error_message						#and the error_message
	}
	return render(request, 'auth/login.html', context)		#load the login page using "context" information

#define a function view called logout_view that takes a request from user
def logout_view(request):									
	logout(request)				#the use pre-defined Django function to logout 
	return redirect('login')	#after logging out go to login form (or whichever page you want)
