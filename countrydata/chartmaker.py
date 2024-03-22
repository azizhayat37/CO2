from .models import Data
import plotly.graph_objects as go

# Correctly formats the year for db query purposes
def year_in_db(year):
    return f'co2_{year}'

# you need to pass in the 3 years country codes as strings and the years as integers
def create_double_bar_chart(country1, country2, start_year, end_year):

    # Establish list of years
    years = [str(year) for year in range(start_year, end_year+1)]

    # Create a figure
    fig = go.Figure()

    # Create lists to store the y values for each country
    country1_y = []
    country2_y = []

    # Get the data for each country by querying the database and appending to the lists
    for year in years:
        data_country1 = Data.objects.filter(countryCode=country1).values_list(year_in_db(year), flat=True)
        country1_y.append(float(data_country1[0]) if data_country1 else 0.0)

        data_country2 = Data.objects.filter(countryCode=country2).values_list(year_in_db(year), flat=True)
        country2_y.append(float(data_country2[0]) if data_country2 else 0.0)
    
    # Add the traces to the figure
    fig.add_trace(go.Bar(
        x=years,
        y=country1_y,
        name=country1
    ))
    fig.add_trace(go.Bar(
        x=years,
        y=country2_y,
        name=country2
    ))

    # Update the layout with axis titles
    fig.update_layout(
        barmode='group', 
        xaxis_tickangle=-45,
        xaxis_title='Duration',  # Set x-axis title
        yaxis_title='Emission Rate'  # Set y-axis title
    )

    return fig.to_html(full_html=False)
