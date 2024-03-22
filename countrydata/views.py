from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'countrydata/home.html')

def comparison(request):
    return render(request, 'countrydata/comparison.html')