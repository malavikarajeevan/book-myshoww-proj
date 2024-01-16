from django.shortcuts import render,redirect
from .models import Tour
from .forms import TodoForm


# Create your views here.
def Home(req):
    tours=Tour.objects.all()
    if req.method=="POST": 
        place=req.POST.get('place','')
        priority=req.POST.get('priority','')
        date=req.POST.get('date','')
        img=req.FILES['image']        
        todo=Tour(place=place,priority=priority,date=date,image=img)
        todo.save()
    return render(req,'index.html',{"tours":tours})


def Update(req,id):
    tours=Tour.objects.get(id=id)
    # if req.method=="POST":
    #     task=req.POST.get('task','')
    #     priority=req.POST.get('priority','')
    #     Task.objects.filter(id=id).update(task=task,priority=priority)
    #     return redirect("home")
    # ==================================================================
    # django forms
    f=TodoForm(req.POST or None,instance=tours)
    if f.is_valid():
        f.save()
        return redirect("home")
    # return render(req,'update.html',{"task":tasks})
    return render(req,'formUpdate.html',{"tours":tours,'f':f})


def Delete(req,id):
    tours=Tour.objects.get(id=id)
    if req.method=="POST":
        Tour.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"tour":tours})




