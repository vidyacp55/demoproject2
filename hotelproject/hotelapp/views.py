from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from . models import Hotel
from . forms import HotelForm


def index(request):
    hotel=Hotel.objects.all()
    context={'hotel_list':hotel}
    return render(request,"index.html",context)

def detail(request,hotel_id):
    hotel= Hotel.objects.get(id=hotel_id)
    return render(request,"detail.html",{'hotel1':hotel})
    # return HttpResponse("this is hotel no %s" % hotel_id)
def add_hotel(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        hotel=Hotel(name=name,desc=desc,year=year,img=img)
        hotel.save()
    return render(request,'add.html')
def update(request,id):
    hotel=Hotel.objects.get(id=id)
    form=HotelForm(request.POST or None,request.FILES,instance=hotel)
    if form.is_valid():
        form.save()
        return redirect('/')
    return  render(request,'edit.html',{'form':form,'hotel':hotel})
def delete(request,id):
    if request.method=='POST':
        hotel=Hotel.objects.get(id=id)
        hotel.delete()
        return redirect('/')
    return render(request,'delete.html')
