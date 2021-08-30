from django.shortcuts import render,redirect
from django.http import HttpResponse
from Imageapp.models import ImageUpload
from Imageapp.forms import ImageUploadForm

# Create your views here.

def get(request):
    return render(request,"index.html")

def ImgaeUpload(request):
    if request.method=="POST":
        form=ImageUploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/success")

    else:
        form=ImageUploadForm()
    return render(request, 'image_form.html', {'form' : form})


def success(request):
    return render(request,"success.html")
