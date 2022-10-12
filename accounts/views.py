from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login (request):
    return render (request, 'accounts/login.html')

def logout (request):
    return render (request, 'accounts/logout.html')

def cadastro (request):
    if request.method !='POST':
        return render (request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
#validar campos vazios
    
#validar email
    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido')
        return render (request, 'accounts/cadastro.html')
    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais')
        return render (request, 'accounts/cadastro.html')
    
    
    
    if senha != senha2:
        messages.error(request, 'Senhas não conferem')
        return render (request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe')
        return render (request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já cadastrado')
        return render (request, 'accounts/cadastro.html')
    
    messages.success(request, 'Cadastrado com Sucesso!')

    user = User.objects.create_user(username=usuario, email=email, password=senha,
     first_name=nome, last_name=sobrenome)

    user.save()
    return redirect ('login')

def dashboard (request):
    return render (request, 'accounts/dashboard.html')