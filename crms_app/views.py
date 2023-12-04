from django.shortcuts import render,redirect
from .models import CustomerModel,IndustryModel,NoteModel,TaskModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.



@login_required(login_url='/authentication/login')
def index(request):
    if request.method == "GET":
        customers = CustomerModel.objects.all().order_by('-created_date')
        notes = NoteModel.objects.all()
        return render(request, 'crms/index.html',{'customers':customers,'notes':notes})


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
            messages.warning(request, 'Company Name is required')
            return render(request, 'crms/update.html',context)

        if not cs_name:
            messages.warning(request, 'Customer Name is required')
            return render(request, 'crms/update.html',context)
        
        if not email:
            messages.warning(request, 'Email is required')
            return render(request, 'crms/update.html',context)
        
        if not phone:
            messages.warning(request, 'Phone number is required')
            return render(request, 'crms/update.html',context)
        
        if not address:
            messages.warning(request, 'Address is required')
            return render(request, 'crms/update.html',context)

        if not industry:
            messages.warning(request, 'Choose one industry')
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
    

@login_required(login_url='/authentication/login')
def delete_customer(request,pk):

    customers = CustomerModel.objects.get(id=pk)
    customers.delete()

    messages.success(request, 'Customer deleted successfully')
    return redirect('crms')



@login_required(login_url='/authentication/login')
def addNote(request, pk):
    customer = CustomerModel.objects.get(id=pk)

    if request.method == "POST":
        note_text = request.POST['note']

        # Create a new note associated with the customer
        new_note = NoteModel.objects.create(
            note=note_text,
            customer=customer,
            assigned_by = request.user
        )

        new_note.save()  # Save the new note

        messages.success(request, 'Note added successfully')
        return redirect('note_list')

    return render(request, 'crms/update.html', {'customers': customer})


@login_required(login_url='/authentication/login')
def listNotes(request):
    notes = NoteModel.objects.all()
    return render(request, 'todo/note_list.html', {'notes': notes})



@login_required(login_url='/authentication/login')
def listTasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


@login_required(login_url='/authentication/login')
def addToTask(request, note_id):
    note = NoteModel.objects.get(id=note_id)

    if request.method == "POST":
        if TaskModel.objects.filter(note=note).exists():
            messages.warning(request, 'Note is already in Tasks-List')
        else:
            task = TaskModel.objects.create(
                note=note,

            )

            task.save()

            # Optionally, remove the note from the note list page
            # note.delete()

            messages.success(request, 'Note added to task successfully')
            return redirect('task_list')

    return render(request, 'todo/note_list.html', {'notes': NoteModel.objects.all()})


@login_required(login_url='/authentication/login')
def delete_task(request,note_id):
    note = NoteModel.objects.get(id=note_id)

    note.delete()
    messages.success(request, 'Delete Task successfully')
    return redirect('task_list')


def opportunity(request):

    return render(request, 'crms/opportunity.html')