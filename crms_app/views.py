from django.shortcuts import render,redirect
from .models import CustomerModel,IndustryModel,NoteModel,TaskModel
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

def search_by(request):
    search = request.GET.get('search')

    if search:
        customers = CustomerModel.objects.filter(
            Q(com_name__icontains=search) | 
            Q(cs_name__icontains=search) 
        )
        notes = NoteModel.objects.all()
        tasks = TaskModel.objects.all()
        return render(request, 'crms/index.html',{'customers':customers,'notes':notes,'tasks':tasks,'cls':customers})
    else:
        notes = NoteModel.objects.all()
        tasks = TaskModel.objects.all()
        customers = CustomerModel.objects.all().order_by('-created_date')
        return render(request, 'crms/index.html',{'customers':customers,'notes':notes,'tasks':tasks})
    


@login_required(login_url='/authentication/login')
def index(request):
    notes = NoteModel.objects.all()
    tasks = TaskModel.objects.all()
    customers = CustomerModel.objects.all().order_by('-created_date')

    paginator = Paginator(customers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'crms/index.html',{'customers':page_obj,'notes':notes,'tasks':tasks})


@login_required(login_url='/authentication/login')
def add_customer(request):

    notes = NoteModel.objects.all()
    tasks = TaskModel.objects.all()

    industries = IndustryModel.objects.all()
    context = {
        'industries':industries,
        'values':request.POST,
        'notes':notes,
        'tasks':tasks
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

    notes = NoteModel.objects.all()
    tasks = TaskModel.objects.all()
    
    customers = CustomerModel.objects.get(id=pk)
    industries = IndustryModel.objects.all()
    context = {
        'customers': customers,
        'industries': industries,
        'notes':notes,
        'tasks':tasks
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
    tasks = TaskModel.objects.all()
    return render(request, 'todo/note_list.html', {'notes': notes,'tasks':tasks})

@login_required(login_url='/authentication/login')
def noteBadge(request):
    notes = NoteModel.objects.all()
    return render(request, 'partials/_sidebar.html', {'notes': notes})


@login_required(login_url='/authentication/login')
def taskBadge(request):
    tasks = TaskModel.objects.all()
    return render(request, 'partials/_sidebar.html', {'tasks': tasks})



@login_required(login_url='/authentication/login')
def listTasks(request):
    tasks = TaskModel.objects.all()
    notes = NoteModel.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks,'notes':notes})


@login_required(login_url='/authentication/login')
def addToTask(request, note_id):
    note = NoteModel.objects.get(id=note_id)

    if request.method == "POST":

        if TaskModel.objects.filter(note=note).exists():
            messages.warning(request, 'Note is already in Tasks, Check Task-List')
        else:
            task = TaskModel.objects.create(
                note=note,

            )

            task.save()

            # Optionally, remove the note from the note list page
            # note.delete()

            messages.success(request, 'Note added to task successfully')
            return redirect('task_list')

    return render(request, 'todo/note_list.html', {'notes': NoteModel.objects.all(),'tasks': TaskModel.objects.all()})


@login_required(login_url='/authentication/login')
def delete_task(request,note_id):
    note = NoteModel.objects.get(id=note_id)

    note.delete()
    messages.success(request, 'Delete Task successfully')
    return redirect('task_list')


@login_required(login_url='/authentication/login')
def opportunity(request):
    notes = NoteModel.objects.all()
    tasks = TaskModel.objects.all()
    return render(request, 'crms/opportunity.html',{'notes':notes,'tasks':tasks})


@login_required(login_url='/authentication/login')
def customer_data(request):
    # Calculate the date 7 days ago
    seven_days_ago = timezone.now() - timedelta(days=7)

    # Filter customers created in the last 7 days
    customers = CustomerModel.objects.filter(created_date__gte=seven_days_ago)

    # Create a dictionary with 'created_date' and 'count' for each day
    data = {
        'labels': [customer.created_date.strftime('%Y-%m-%d') for customer in customers],
        'dataValues': [customers.filter(created_date=date).count() for date in set(c.created_date for c in customers)],
    }
    return JsonResponse(data)



@login_required(login_url='/authentication/login')
def dashboard(request):

    notes = NoteModel.objects.all()
    tasks = TaskModel.objects.all()
    
    customers = CustomerModel.objects.all()
    industries = IndustryModel.objects.all()
    context = {
        'customers': customers,
        'industries': industries,
        'notes':notes,
        'tasks':tasks
    }

    return render(request, 'crms/dashboard.html',context)