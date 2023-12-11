from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth

# Create your views here.


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username can only contain alphanumeric characters'}, status = 400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Username is already in use, choose another one'}, status = 409)

        return JsonResponse({'username_valid': True})
    

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status = 400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email is exist.If you have a account,please login'}, status = 409)

        return JsonResponse({'email_valid': True})
    



class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):

        context = {
            'fieldValues': request.POST
        }

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():

            if not User.objects.filter(email=email).exists():

                if len(password) < 6:
                    messages.error(request, 'Password is too short !')

                    return render(request, 'authentication/register.html', context)
                
                user = User.objects.create_user(
                    username=username,
                    email=email
                )
                user.set_password(password)
                user.save()
                messages.success(request, 'Account created successfully. Please Login')
                return redirect('login')

        return render(request, 'authentication/register.html')
    


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                # messages.success(request, 'Welcome, '+user.username)
                return redirect('home')
            
            messages.error(request, 'Invalid username or password')
            return render(request, 'authentication/login.html')
        
        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html')
    


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')