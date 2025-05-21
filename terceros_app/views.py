from django.shortcuts import render

# terceros_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ThirdParty, City
from .forms import ThirdPartyForm, BranchForm

def third_party_create(request):
    if request.method == 'POST':
        form = ThirdPartyForm(request.POST)
        if form.is_valid():
            third_party = form.save()
            print(f"Redirigiendo a branch_create con ID: {third_party.id}") #Prueba
            return redirect('branch_create', third_party_id=third_party.id)
    else:
        form = ThirdPartyForm()
    return render(request, 'terceros_app/third_party_form.html', {'form': form})

def branch_create(request, third_party_id):
    third_party = get_object_or_404(ThirdParty, id=third_party_id)
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.third_party = third_party
            branch.save()
            return redirect('branch_create', third_party_id=third_party.id)
    else:
        last_branch = third_party.branches.order_by('-branch_number').first()
        next_number = (last_branch.branch_number + 1) if last_branch else 1
        form = BranchForm(initial={
            'branch_number': next_number,
            'main_address': third_party.address,
            'delivery_address': third_party.address,
        })
    return render(request, 'terceros_app/branch_form.html', {'form': form, 'third_party': third_party})

def get_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(cities), safe=False)