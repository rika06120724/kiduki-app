from django.shortcuts import render, redirect
from .forms import UserCreateForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('pages:index')
    else:
        form = UserCreateForm()
    return render(request, 'users/register.html', {'form': form})