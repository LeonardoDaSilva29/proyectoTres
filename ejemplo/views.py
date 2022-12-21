from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render (request, 'ejemplo/saludar_a.html',
    {"nombre": nombre}
    )