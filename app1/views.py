from django.shortcuts import render

# Create your views here.
def genric_static(request):
    return render(request,'genric_static.html')
