from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import filesUpload
from .models import workFrom


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(request.user)
            login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'loginUser.html')
    return render(request, 'loginUser.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/loginUser')
    else:
        if request.method =='POST':
            name=request.POST.get("name")
            team=request.POST.get("team")
            extra=request.POST.get("extra")
            topic=request.POST.get("topic")
            zipFile = request.FILES.get("zipFile")
            document = filesUpload.objects.create(name=name,team=team,extra=extra,topic=topic,file=zipFile)
            document.save()
        return render(request, 'dashboard.html')
   


def staff(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/nostaff')
    else:
        return render(request, 'staff.html')


def loginFirst(request):
    return render(request, 'loginFirst.html')

def nostaff(request):
    return render(request, 'nostaff.html')


def logoutUser(request):
    print(request)
    params = {"user": request.user}
    logout(request)
    return render(request, 'logoutUser.html', params)


def work(request):
    wrk = workFrom.objects.all()
    l=  (len(wrk))
    print(l)
    print(wrk)
    params = {"work":wrk, "length":l}
    return render(request, 'work.html',params)
