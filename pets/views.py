from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from pets.forms import PetForm
from pets.models import Pet

@login_required(login_url='users:login')
def create_pet(request):
    """ペット登録ビュー"""
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pets:my_page')
    else:
        form = PetForm()
    return render(request, 'pets/register.html', {'form': form})

@login_required(login_url='users:login')
def my_page(request):
    """マイページ"""
    pets = Pet.objects.filter(owner=request.user)
    return render(request, 'pets/my_page.html', {'pets': pets})

@login_required(login_url='users:login')
def pet_edit(request, pet_id):
    """ペット編集ビュー"""
    pet = Pet.objects.get(id=pet_id)
    
    # 権限チェック：owner が本人か確認
    if pet.owner != request.user:
        return redirect('pets:my_page')
    
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets:my_page')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/edit.html', {'form': form, 'pet': pet})