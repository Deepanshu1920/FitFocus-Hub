from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request, "myapp\home_page001.html", context)