from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# ajax
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.


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
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = u
                todo.save()
                return JsonResponse({"status": 1})
            else:
                return JsonResponse({"status": 0})

        else:
            u = request.user
            todos = TODO.objects.filter(user=u).exists()
            ctx = {
                'form': TODOForm(),
                "todo": todos,
            }
            return render(request, 'index.html', ctx)
    else:
        return redirect('login')


def alltodo(request):
    u = request.user
    todos = TODO.objects.filter(user=u).order_by('-priority').values()
    return JsonResponse({"data": list(todos)})


def signout(request):
    logout(request)
    messages.success(request, 'Logout Successfully.')
    return redirect('login')


def delete_todo(request):
    id = request.POST.get('sid')
    TODO.objects.get(pk=id).delete()
    return JsonResponse({"status": 1})


def change_todo(request):
    id = request.POST.get('sid')
    status = request.POST.get('sst')
    todo = TODO.objects.get(pk=id)
    if status == 'C':
        s = 'P'
    else:
        s = 'C'
    todo.status = s
    todo.save()
    return JsonResponse({"status": 1})


def graphdata(request):
    u = request.user
    complete = TODO.objects.filter(user=u, status='C').count()
    pending = TODO.objects.filter(user=u, status='P').count()

    data = {
        'complete': complete,
        'pending': pending
    }
    return JsonResponse(data)


def graph(request):
    u = request.user
    complete = TODO.objects.filter(user=u, status='C').count()
    pending = TODO.objects.filter(user=u, status='P').count()

    context = {
        'complete': complete,
        'pending': pending,
        "total": complete+pending,
    }
    return render(request, 'include/graph.html', context)

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
