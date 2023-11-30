from django.shortcuts import render,redirect
from .models import CustomerModel,IndustryModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.



@login_required(login_url='/authentication/login')
def index(request):
    if request.method == "GET":
        customers = CustomerModel.objects.all().order_by('-created_date')
        return render(request, 'crms/index.html',{'customers':customers})


@login_required(login_url='/authentication/login')
def add_customer(request):

    industries = IndustryModel.objects.all()
    context = {
        'industries':industries,
        'values':request.POST
    }
    if request.method == "GET":
        return render(request, 'crms/add_customer.html',context)
    
    if request.method == "POST":

        com_name = request.POST['com_name']
        cs_name = request.POST['cs_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        industry = request.POST['industry']

        if not com_name:
            messages.error(request, 'Company Name is required')
            return render(request, 'crms/add_customer.html',context)

        if not cs_name:
            messages.error(request, 'Customer Name is required')
            return render(request, 'crms/add_customer.html',context)
        
        if not email:
            messages.error(request, 'Email is required')
            return render(request, 'crms/add_customer.html',context)
        
        if not phone:
            messages.error(request, 'Phone number is required')
            return render(request, 'crms/add_customer.html',context)
        
        if not address:
            messages.error(request, 'Address is required')
            return render(request, 'crms/add_customer.html',context)

        if not industry:
            messages.error(request, 'Choose one industry')
            return render(request, 'crms/add_customer.html',context)
        
        posts = CustomerModel.objects.create(
                com_name=com_name,
                cs_name=cs_name,
                email=email,
                phone=phone,
                address=address,
                industry=industry
            )
        posts.save()
        messages.success(request, 'Customer created successfully')

        return redirect('crms')
    


@login_required(login_url='/authentication/login')
def edit_customer(request, pk):
    
    customers = CustomerModel.objects.get(id=pk)
    industries = IndustryModel.objects.all()
    context = {
        'customers': customers,
        'industries': industries
    }
    if request.method == "GET":
        return render(request, 'crms/update.html', context)
    
    if request.method == "POST":

        com_name = request.POST['com_name']
        cs_name = request.POST['cs_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        industry = request.POST['industry']
        modified_date = request.POST['modified_date']

        if not com_name:
            messages.error(request, 'Company Name is required')
            return render(request, 'crms/update.html',context)

        if not cs_name:
            messages.error(request, 'Customer Name is required')
            return render(request, 'crms/update.html',context)
        
        if not email:
            messages.error(request, 'Email is required')
            return render(request, 'crms/update.html',context)
        
        if not phone:
            messages.error(request, 'Phone number is required')
            return render(request, 'crms/update.html',context)
        
        if not address:
            messages.error(request, 'Address is required')
            return render(request, 'crms/update.html',context)

        if not industry:
            messages.error(request, 'Choose one industry')
            return render(request, 'crms/update.html',context)
        
        
        customers.com_name=com_name
        customers.cs_name=cs_name
        customers.email=email
        customers.phone=phone
        customers.address=address
        customers.industry=industry
        customers.modified_date=modified_date
            
        customers.save()
        messages.success(request, 'Customer updated successfully')

        return redirect('crms')
    


def delete_customer(request,pk):

    customers = CustomerModel.objects.get(id=pk)
    customers.delete()

    messages.success(request, 'Customer deleted successfully')
    return redirect('crms')