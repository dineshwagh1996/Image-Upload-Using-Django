from django.shortcuts import render,redirect
from django.http import HttpResponse
from Regestrationapp.forms import regestrationForm
from Regestrationapp.models import regestration



# Create your views here.

def getregetration(request):
    return render(request,"index.html")

def home(request):
    form=regestrationForm()
    return render(request,"home.html",{'form':form})


def savedata(request):
    if request.method=="POST":
        form=regestrationForm(request.POST,request.FILES)
        # newdoc = regestration(docfile = request.FILES['docfile'])
        # newdoc.save()
        form.save()
        return redirect("/success")
    else:
        form=regestrationForm()
        return render(request,"index.html")

def success(request):
    return render(request,"success.html")

def showData(request):
    form=regestration.objects.all()
    return render(request,"show.html",{'form':form})

def edit(request, id):
    form= regestration.objects.get(id=id)
    return render(request,'edit.html', {'form':form})

def update(request, id):
    emp = regestration.objects.get(id=id)
    form = regestrationForm(request.POST, instance = emp)
    if form.is_valid():
        form.save()
        print("==========================")
        return redirect("/showData")
    return render(request, 'edit.html', {'form': emp})


def delete(request,id):
    form=regestration.objects.get(id=id)
    form.delete()
    return redirect("/showData")

def getlogin(request):
    return render(request,"login.html")


def login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        check_user = regestration.objects.filter(Email=Email, Password=Password)
        if check_user:
            request.session['Email'] = Email
            return HttpResponse("success")
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')
