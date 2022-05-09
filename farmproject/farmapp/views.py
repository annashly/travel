from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from farmapp.models import Farm
from . forms import FarmForm

def fun(request):
    farm=Farm.objects.all()
    context={
        'farm_list':farm
    }
    return render(request,'index.html',context)
def detail(request,farm_id):
    farm=Farm.objects.get(id=farm_id)
    return render(request,"detail.html",{'farm':farm})
def add_farm(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        price= request.POST.get('price',)
        img = request.FILES['img']
        farm=Farm(name=name,desc=desc,price=price,img=img)
        farm.save()
    return render(request,'add.html')
def update(request,id):
    farm=Farm.objects.get(id=id)
    form=FarmForm(request.POST or None,request.FILES,instance=farm)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'farm':farm})
def delete(request,id):
    if request.method == "POST":
        farm = Farm.objects.get(id=id)
        farm.delete()
        return redirect('/')
    return render(request, 'delete.html')