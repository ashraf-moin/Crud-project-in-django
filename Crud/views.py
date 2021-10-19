from django.shortcuts import render
from Crud.models import crudst
from django.contrib import messages
from Crud.forms import stform

def stdisplay(request):
    result= crudst.objects.all()
    return render(request,"Index.html",{"crudst":result})


def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('staddress') and request.POST.get('stmobile'):
            savest = crudst()
            savest.stname = request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.save()
            messages.success(request, "New Record of "+savest.stname+" is Added")
            return render(request, "Create.html")
    else:
            return render(request, "Create.html")

def stedit(request,id):
    getstudentdetails=crudst.objects.get(id=id)
    return render(request,'edit.html',{"crudst":getstudentdetails})

def stupdate(request,id):
    stupdate = crudst.objects.get(id=id)
    form = stform(request.POST,instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request, "New Record of  is Added")
        return render(request,"edit.html",{"crudst":stupdate})

def stdel(request,id):
    delstudent=crudst.objects.get(id=id)
    delstudent.delete()
    result= crudst.objects.all()
    return render(request,"Index.html",{"crudst":result})