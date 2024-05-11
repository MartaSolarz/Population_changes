# --- Script to create map ---

import json
import folium
import pandas as pd

LEGEND_BINS = [0, 5000000, 10000000, 15000000, 20000000, 25000000, 30000000, 35000000, 40000000, 45000000, 50000000, 55000000, 60000000, 65000000, 70000000, 75000000, 80000000, 85000000, 90000000]


def create_population_map(year: int, data: pd.DataFrame, selected_countries_geojson: json) -> folium.Map:
    """
        Creates a population map using Folium based on provided data.

        Parameters:
        - year (int): The year for which population data will be displayed.
        - data (pd.DataFrame): DataFrame containing population data for selected countries.
        - selected_countries_geojson (json): GeoJSON data for selected countries.

        Returns:
        - folium.Map: Folium map displaying population distribution.
    """
    map_center = [54.5260, 15.2551]
    my_map = folium.Map(location=map_center, zoom_start=3.5)

    folium.TileLayer('stamenwatercolor').add_to(my_map)

    year_str = str(year)

    # Add choropleth map to display the population data
    folium.Choropleth(
        geo_data=selected_countries_geojson,
        name=year_str,
        data=data,
        columns=['Code', year_str],
        key_on='feature.properties.ISO_A3',
        fill_opacity=0.7,
        line_opacity=0.1,
        legend_name=f'Population by Country ({year_str})',
        highlight=True,
        nan_fill_color='grey',
        nan_fill_opacity=0.4,
        bins=LEGEND_BINS,
        fill_color='Reds',
    ).add_to(my_map)

    # Add population labels
    folium.GeoJson(
        selected_countries_geojson,
        style_function=lambda feature: {
            'color': 'rgba(128,128,128,0.3)',
            'weight': 0.5,
            'fillOpacity': 0,
        },
        tooltip=folium.features.GeoJsonTooltip(
            fields=['Name', year_str],
            aliases=['Country', f'Population {year_str}'],
            labels=True,
            sticky=True
        ),
        highlight_function=lambda x: {'weight': 3, 'fillOpacity': 0},
        name='Population Labels',
    ).add_to(my_map)

    folium.LayerControl().add_to(my_map)

    return my_map

def test():
    print("test")