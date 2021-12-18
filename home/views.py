from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


# def home(request):
#     if request.user.is_authenticated:
#         user = request.user
#         form = TODOForm()
#         todos = TODO.objects.filter(user=user).order_by('priority')
#         return render(request, 'index.html', context={'form': form, 'todos': todos})


def loginn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            ctx = {
                'form': form
            }
            return render(request, 'login.html', ctx)

    form = AuthenticationForm()
    ctx = {
        'form': form
    }
    return render(request, 'login.html', ctx)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            ctx = {
                'form': form
            }
            return render(request, 'signup.html', ctx)
    form = UserCreationForm(label_suffix='')
    ctx = {
        'form': form
    }
    return render(request, 'signup.html', ctx)


login_required(login_url='login/')


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u = request.user
            form = TODOForm(request.POST)
            if form.is_valid():
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
    return redirect('login')


# def delete_todo(request, id):
#     TODO.objects.get(pk=id).delete()
#     return redirect('home')


# def change_todo(request, id, status):
#     todo = TODO.objects.get(pk=id)
#     todo.status = status
#     todo.save()
#     return redirect('home')


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
