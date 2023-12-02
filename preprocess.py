# --- Script to preprocessing data ---

import json
import pandas as pd
from typing import Hashable


def rename_column(column: Hashable) -> Hashable:
    """
        Renames specific columns in the DataFrame.

        Parameters:
        - column (Hashable): The column name to be renamed.

        Returns:
        - Hashable: The renamed column name or a modified string based on the condition.
    """
    if column == 'Country Name':
        return 'Name'
    elif column == 'Country Code':
        return 'Code'
    else:
        return column[:4]


def preprocess_data(data: pd.DataFrame, selected_countries: list[str]) -> pd.DataFrame:
    """
        Performs data preprocessing on the provided DataFrame.

        Parameters:
        - data (pd.DataFrame): Input DataFrame containing country data.
        - selected_countries (list[str]): List of selected country codes.

        Returns:
        - pd.DataFrame: Processed DataFrame after dropping columns, renaming columns, and type conversion.
    """
    df = data.copy()

    df.drop(columns=['Series Name', 'Series Code'], inplace=True)
    df.rename(columns=rename_column, inplace=True)
    df = df[df['Code'].isin(selected_countries)]
    df.iloc[:, 2:] = df.iloc[:, 2:].astype(float)

    return df


def update_properties_in_geojson(world_geojson: json, data: pd.DataFrame, selected_countries: list[str]) -> json:
    """
        Updates properties in a GeoJSON file based on provided country data.

        Parameters:
        - world_geojson (json): Input GeoJSON containing world features.
        - data (pd.DataFrame): DataFrame containing country data.
        - selected_countries (list[str]): List of selected country codes.

        Returns:
        - json: Filtered GeoJSON with updated properties for selected countries.
    """
    filtered_geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

    for feature in world_geojson['features']:
        iso_a3 = feature['properties']['ISO_A3']

        if iso_a3 not in selected_countries:
            continue

        row = data[(data['Code'] == iso_a3)]
        if not row.empty:
            name = row.iloc[0]['Name']

            for year in range(1960, 2051):
                year_str = str(year)
                population_year = row.iloc[0][year_str]
                feature['properties'][year_str] = population_year

            feature['properties']['Name'] = name

            filtered_geojson['features'].append(feature)

    return filtered_geojson
