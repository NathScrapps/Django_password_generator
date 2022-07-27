from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_password = ''

    length = int(request.GET.get('length'))
    # Añadimos caracteres comunes(letras en mayusculas)
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    # Añadimos caracteres especiales
    if request.GET.get('special'):
        characters.extend(list('!#$%&()*+,-./{?¿}'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request,'generator/password.html',{
        'password':generated_password
        })

def about(request):
    return render(request,'generator/about.html')