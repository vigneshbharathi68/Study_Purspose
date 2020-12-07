from django.shortcuts import render

def all_practices(request):
    return render(request, 'all_practices.html')