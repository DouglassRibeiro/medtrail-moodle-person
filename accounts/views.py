from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')

def login(login):
    return render(login, 'accounts/login.html')