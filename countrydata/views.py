from django.shortcuts import render
from .models import Data
from django.db.models import F

# Create your views here.
def home(request):
    years = range(1990, 2021)  # Years range
    selected_year = request.GET.get('year')
    countries = None

    if selected_year:
        co2_field = f'co2_{selected_year}'
        countries = Data.objects.all().annotate(co2_emissions=F(co2_field)).order_by('-co2_emissions')[:10]

    context = {
        'years': years,
        'selected_year': selected_year,
        'countries': countries,
    }
    return render(request, 'countrydata/home.html', context)

def comparison(request):
    return render(request, 'countrydata/comparison.html')