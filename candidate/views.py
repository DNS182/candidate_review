from django.shortcuts import get_object_or_404, render
from .models import Candidate

# Create your views here.
def index(request):
    candis = Candidate.objects.all()
    return render(request , 'index.html' , {'candis' : candis})


def detail(request , pk):
    deta = get_object_or_404(Candidate , pk = pk)
    return render(request , 'detail.html' , {'deta' : deta})