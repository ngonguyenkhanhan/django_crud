from django.shortcuts import render, redirect, get_object_or_404

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}
    
    # add the dictionary during initialization
    form  = GeeksForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('createview')
        
    context['form'] = form
    return render(request, 'create_view.html', context)

def list_view(request):
    # dictionary for initial data with fields names as keys
    context = {}
    
    # add the dictionary during initialization
    context['dataset'] = GeeksModel.objects.all()
    return render(request, 'list_view.html', context)

def detail_view(request, id):
    context = {}
    
    context['data'] = GeeksModel.objects.get(id=id)
    return render(request, 'detail_view.html', context)

def update_view(request, id):
    context = {}
    
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id =id)
    
    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance=obj)
    
    # save the data form the form and redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('/'+id)
    
    # add form dictionary to context
    context['form'] = form
    
    return render(request,'update_view.html', context)

def delete_view(request, id):
    context = {}
    
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id=id)
    
    if request.method == 'POST':
        # delete object
        obj.delete()
        
        # after deleting redirect to homepage
        return redirect('/')
    return render(request,'delete_view.html', context)
    
    