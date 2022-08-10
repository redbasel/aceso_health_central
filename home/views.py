from django.shortcuts import render

# Create your views here.

def index(request):
    """ a view  to return to index page """
    
    return render(request, 'home/index.html')