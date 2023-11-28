from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'crms/index.html')

def add_customer(request):
    return render(request, 'crms/add_customer.html')