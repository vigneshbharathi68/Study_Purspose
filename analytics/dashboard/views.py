from django.shortcuts import render

# Create your views here.

def dashboard_home(request):
    return render(request, "download_home.html")