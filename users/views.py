from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy 
from .forms import UserCreateForm, CustomAuthenticationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pets:register')
    else:
        form = UserCreateForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pets:my_page') 

def logout_view(request):
    logout(request)
    return redirect('pages:index')
