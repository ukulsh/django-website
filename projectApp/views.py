from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .models import Visitor
from django.http import HttpResponse
def contact_view(request):
    if request.method=='POST':
        visitor=Visitor()
        visitor.name=request.POST.get('name')
        visitor.save()
        print(visitor.name)
        name=visitor.name
        inTime=visitor.inTime
        content = '\nVisitor Details: \n'
        content += 'Checkin Time: '+str(inTime)+'\n'
        return redirect("http://stackoverflow.com/")
    else:
        return render(request,"index.html")

def index_call(request):
    return render(request, "index.html")

  