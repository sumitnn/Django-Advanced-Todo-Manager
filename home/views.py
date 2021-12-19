from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# def home(request):
#     if request.user.is_authenticated:
#         user = request.user
#         form = TODOForm()
#         todos = TODO.objects.filter(user=user).order_by('priority')
#         return render(request, 'index.html', context={'form': form, 'todos': todos})


def loginn(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully.')
            return redirect('home')
        else:
            form = AuthenticationForm()
            ctx = {
                'form': form
            }
            messages.error(request, 'Invalid Credential.')
            return render(request, 'login.html', ctx)
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        ctx = {
            'form': form
        }
        return render(request, 'login.html', ctx)
    else:
        return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Create Account Successfully.')
            return redirect('login')
        else:
            ctx = {
                'form': form
            }
            messages.error(request, 'Not created.')
            return render(request, 'signup.html', ctx)
    if not request.user.is_authenticated:
        form = UserCreationForm(label_suffix='')
        ctx = {
            'form': form
        }
        return render(request, 'signup.html', ctx)
    return redirect('home')


login_required(login_url='login/')


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u = request.user
            form = TODOForm(request.POST)
            if form.is_valid:
                todo = form.save(commit=False)
                todo.user = u
                todo.save()
                return redirect('home')
        else:
            u = request.user
            todos = TODO.objects.filter(user=u).order_by('-priority')
            ctx = {
                'form': TODOForm(),
                'todos': todos
            }

            return render(request, 'index.html', ctx)
    else:
        return redirect('login')


# def add_todo(request):
#     if request.user.is_authenticated:
#         user = request.user
#         print(user)
#         form = TODOForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             todo = form.save(commit=False)
#             todo.user = user
#             todo.save()
#             print(todo)
#             return redirect('home')
#         else:
#             return render(request, 'index.html', context={'form': form})


def signout(request):
    logout(request)
    messages.success(request, 'Logout Successfully.')
    return redirect('login')


def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')


def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    if status == 'C':
        s = 'P'
    else:
        s = 'C'
    todo.status = s
    todo.save()
    return redirect('home')


# def homepage(request):
#     query = Addpost.objects.all()
#     cont = {
#         'q': query
#     }
#     return render(request, 'index.html', cont)


# def addevent(request):
#     if request.method == 'POST':
#         f = AddForm(request.POST, request.FILES)
#         if f.is_valid():
#             f.save()
#             return redirect('home')
#     a = AddForm(label_suffix='')
#     context = {
#         'form': a
#     }
#     return render(request, 'addevent.html', context)


# def change(request, id):
#     todo = Addpost.objects.get(pk=id)
#     rev = todo.is_liked
#     if rev == True:
#         rev = False
#     else:
#         rev = True
#     todo.is_liked = rev
#     todo.save()
#     return redirect('home')


# def coments(request, id):
#     todo = Addpost.objects.get(pk=id)
#     rev = todo.is_comnt
#     if rev == True:
#         rev = False
#     else:
#         rev = True
#     todo.is_comnt = rev
#     todo.save()
#     return redirect('home')
