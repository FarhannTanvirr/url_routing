from django.shortcuts import render

def index(request):
    return render(request,'poll.html')

# Create your views here.
