from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    print(request.method)
    if request.method=="GET":
        return render(request,'base/login.html')
    else:
        post= request.POST
        loginname= post.get("loginname",'')
        password= post.get("password",'')
        return redirect('/index')

def index(request):
    if request.method=='GET':
        return render(request, "base/index.html", {'username': ''})
    else:
        post=request.POST
        username=post.get('username')
        return render(request, "base/index.html", {"username":username})

def homes(requset):
    return render(requset,"base/homes.html",{"username","Admin"})
