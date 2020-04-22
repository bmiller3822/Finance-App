from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    user = request.user
    
    return render(request, "core/dashboard.html")