from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pets.forms import PetForm


@login_required(login_url='users:login')
def create_pet(request):
    """ペット登録ビュー"""
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pages:index')
    else:
        form = PetForm()
    return render(request, 'pets/register.html', {'form': form})
