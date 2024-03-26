from django.shortcuts import render
from .models import Data, Metadata
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from .chartmaker import create_double_bar_chart

def home(request):
    years = range(1990, 2021)
    selected_year = request.GET.get('year', '2020')  # Set default year here if not provided
    co2_field = f'co2_{selected_year}' if selected_year else 'co2_2020'  # Default to 2020 data if no year is selected
    
    # Ensure countries always has data by querying the default or selected year
    countries = Data.objects.all().annotate(co2_emissions=F(co2_field)).order_by('-co2_emissions')[:10]
    
    context = {
        'years': years,
        'selected_year': selected_year,
        'countries': countries,
    }
    return render(request, 'countrydata/home.html', context)

def comparison(request):
    countries = Data.objects.all()
    country1_id = request.GET.get('country1')
    country2_id = request.GET.get('country2')

    country1_data = None
    country2_data = None
    graph_html = None
    country1_details = None
    country2_details = None

    if country1_id and country2_id:
        country1_data = get_object_or_404(Data, countryCode=country1_id)
        country2_data = get_object_or_404(Data, countryCode=country2_id)
        graph_html = create_double_bar_chart(country1_id, country2_id, 1990, 2020)

        # Fetch country details from Metadata model
        country1_metadata = get_object_or_404(Metadata, countryCode=country1_data)
        country2_metadata = get_object_or_404(Metadata, countryCode=country2_data)

        # Construct country details dictionary
        country1_details = {
            'name': country1_data.countryName,
            'income_level': country1_metadata.incomeGroup,
            'region': country1_metadata.region,
            'notes': country1_metadata.specialNotes
        }

        country2_details = {
            'name': country2_data.countryName,
            'income_level': country2_metadata.incomeGroup,
            'region': country2_metadata.region,
            'notes': country2_metadata.specialNotes
        }

    context = {
        'countries': countries,
        'country1_data': country1_data,
        'country2_data': country2_data,
        'graph_html': graph_html,
        'country1_details': country1_details,
        'country2_details': country2_details,
    }
    return render(request, 'countrydata/comparison.html', context)

def compare_emissions(request):
    if request.method == 'POST':
        country1_id = request.POST.get('country1')
        country2_id = request.POST.get('country2')

        try:
            country1_data = Data.objects.get(countryCode=country1_id)
            country2_data = Data.objects.get(countryCode=country2_id)
        except Data.DoesNotExist:
            return render(request, 'countrydata/comparison.html', {'error_message': 'Country data not found'})

        graph_html = create_double_bar_chart(country1_id, country2_id, 1990, 2020)

        # Fetch country details
        country1_details = {
            'name': country1_data.countryName,
            'income_level': country1_data.incomeLevel,
            'region': country1_data.region,
            'notes': country1_data.notes
        }

        country2_details = {
            'name': country2_data.countryName,
            'income_level': country2_data.incomeLevel,
            'region': country2_data.region,
            'notes': country2_data.notes
        }

        context = {
            'countries': Data.objects.all(),
            'country1_name': country1_data.countryName,
            'country2_name': country2_data.countryName,
            'graph_html': graph_html,
            'country1_details': country1_details,
            'country2_details': country2_details
        }
        return render(request, 'countrydata/comparison.html', context)

    return render(request, 'countrydata/comparison.html')

def about(request):
    context = {}
    return render(request, 'countrydata/about.html', context)
