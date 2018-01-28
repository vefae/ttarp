from django.shortcuts import render, redirect
from inventory.forms import inventory_form

# Create your views here.

def inventory (request):
    return render(request, 'inventory/inventory.html')

def save_inv (request):
    if request.method == 'POST':
        form = inventory_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ttarp/inventory')

    else:
        form = inventory_form()

        args = {'form' : form}
        return render(request, 'inventory/create_inventory.html', args)
