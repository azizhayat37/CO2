from .models import Data
import plotly.graph_objects as go

# Correctly formats the year for database query purposes
def year_in_db(year):
    return f'co2_{year}'

# You need to pass in the 3 years country codes as strings and the years as integers
def create_double_bar_chart(country1_code, country2_code, start_year, end_year, title="CO2 Emissions Comparison"):

    # Establish list of years
    years = [str(year) for year in range(start_year, end_year+1)]

    # Create a figure
    fig = go.Figure()

    # Create lists to store y values for each country
    country1_y = []
    country2_y = []
        
    # Get the country names for a more descriptive chart title and legend
    country1_name = Data.objects.filter(countryCode=country1_code).values_list('countryName', flat=True).first()
    country2_name = Data.objects.filter(countryCode=country2_code).values_list('countryName', flat=True).first()

    # Update the title to include country names if available
    if country1_name and country2_name:
        title = f"CO2 Emissions: {country1_name} vs {country2_name}"

    # Get the data for each country by querying the database and appending to the lists
    for year in years:
        data_country1 = Data.objects.filter(countryCode=country1_code).values_list(year_in_db(year), flat=True)
        country1_y.append(float(data_country1[0]) if data_country1 else 0.0)

        data_country2 = Data.objects.filter(countryCode=country2_code).values_list(year_in_db(year), flat=True)
        country2_y.append(float(data_country2[0]) if data_country2 else 0.0)
    
    # Add the traces to the figure
    fig.add_trace(go.Bar(
        x=years,
        y=country1_y,
        name=country1_name or country1_code  # Fallback to the code if the name is not available
    ))
    fig.add_trace(go.Bar(
        x=years,
        y=country2_y,
        name=country2_name or country2_code  # Fallback to the code if the name is not available
    ))

    # Update layout with axis titles
    fig.update_layout(
        title={
            'text': title,
            'y':0.9,  
            'x':0.5,  
            'xanchor': 'center',  
            'yanchor': 'top'  
        },
        barmode='group', 
        xaxis_tickangle=-45,
        xaxis_title='Year',  # Set x-axis title
        yaxis_title='CO2 Emissions (Metric Tons per Capita)'  # Set y-axis title
    )

    return fig.to_html(full_html=False)