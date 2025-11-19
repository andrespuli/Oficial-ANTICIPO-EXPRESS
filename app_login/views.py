from django.shortcuts import render

def inicio_view(request):
    return render(request, 'login/inicio.html')

def contraseña_view(request):
    return render(request, 'login/contraseña.html')
