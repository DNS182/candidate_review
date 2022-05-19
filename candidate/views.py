from django.shortcuts import get_object_or_404, render
from .models import Candidate
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def index(request):
    candis = Candidate.objects.all()
    return render(request , 'index.html' , {'candis' : candis})

@staff_member_required
def detail(request , pk):
    deta = get_object_or_404(Candidate , pk = pk)
    return render(request , 'detail.html' , {'deta' : deta})