from django.shortcuts import render,redirect
from .models import myupdate
# Create your views here.
def Home(request):
    if request.method=="POST":
        title=request.POST.get("title")
        if title!="":
            myupdate.objects.create(title=title)
        redirect('Home')
    all_data=myupdate.objects.all()
    data={'data':all_data}
    return render(request,'home.html',context=data)

def Delete(request,id=None):
    myupdate.objects.get(id=id).delete()
    return redirect('Home')

def Complete(request,id=None):
    data=myupdate.objects.get(id=id)
    data.complete=True
    data.save()
    return redirect("Home")

def Uncomplete(request,id=None):
    data=myupdate.objects.get(id=id)
    data.complete=False
    data.save()
    return redirect("Home")