import os

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.decorators.cache import never_cache


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('lgn_in')
    return render(request, "index.html",
                  {'ctgs': Category.objects.filter(user=request.user), "form": CategoryFileUploadForm()})


def lgn_in(request):
    if not request.user.is_authenticated:
        return render(request, "lgn_in.html")
    return redirect('index')


def new_ctg(request):
    title = request.POST['title']
    for c in Category.objects.all():
        if title == c.title:
            return JsonResponse({"name": "same"})
    form = CategoryFileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        # print(form.instance.id)
        return JsonResponse({"num": form.instance.id})


def lg_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('index')


def sign_in(request):
    username = request.POST['name']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"status": "ok"})

    return JsonResponse({"status": "error"})


def register(request):
    username = str(request.POST['name'])
    for n in User.objects.all():
        if username == n.username:
            return JsonResponse({"status": "name"})
    User.objects.create_user(username=username, email=str(request.POST['email']),
                             password=str(request.POST['password']))
    return JsonResponse({"status": "ok"})


@never_cache
def ctg(request, category):
    if not request.user.is_authenticated:
        return redirect('lgn_in')
    num = request.GET['num']
    ctg = get_object_or_404(Category, id=num)
    if category != ctg.title or ctg.user != request.user:
        return render(request, "not_exist_or_not_access.html")

    return render(request, "category.html", {"category": ctg, "nf": FileUploadForm()})


def add_file(request):
    form = FileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        itm = Item.objects.get(id=form.instance.id)
        Category.objects.get(id=request.POST['category']).items.add(itm)
        return JsonResponse({"id": form.instance.id})

@never_cache
def itm(request):
    if not request.user.is_authenticated:
        return redirect('lgn_in')
    num = request.GET['num']
    name = request.GET['name']
    i = get_object_or_404(Item, id=num)
    if name != i.name or request.user != i.user:
        return render(request, "not_exist_or_not_access.html")
    return render(request, 'item.html', {'item': i, "category":request.GET['category']})

def del_file(request):
    _id = request.GET['id']
    name = request.GET['name']
    category = request.GET['category']
    it = Item.objects.get(id=_id)
    if it.name == name:
        os.remove(it.file.path)
        it.delete()
    return redirect('categories/'+category+"?num="+str(Category.objects.get(title=category).id))

def del_catg(request):
    category = request.GET['category']
    _id = request.GET['id']
    c = Category.objects.get(id=_id)
    if c.title == category:
        for i in c.items.all():
            os.remove(i.file.path)
            i.delete()
        if c.photo:
            os.remove(c.photo.path)
        c.delete()

    return redirect('index')