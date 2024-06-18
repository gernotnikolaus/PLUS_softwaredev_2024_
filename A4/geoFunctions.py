""" Calculation of mean, EVI for a time frame and area of interest
This script calculates the EVI for Sentinel-2 for an area of interest and generates a time series plot.

The script contains the following functions:
    * select_bands(image, index_name): Selects the specific bands
    * aggregate_image_collection(collection_name, start_date, end_date, aggregation_method): Aggregates an using the input methode
    * calculateEVI(image, blue, red, nir): Calculation of the EVI
    * calculate_time_series_EVI(collection_name, start_date, end_date, aoi): Calculation of the times series
    * plot_time_series_EVI(time_series): Plotting the EVI

Example code:
    # Define aoi
    aoi = ee.Geometry.Rectangle([17.22, 49.61, 17.26, 49.63])
    # Define Sentinel-2 collletion
    collection_name = 'COPERNICUS/S2'
    # Define time frame
    start_date = '2023-01-01'
    end_date = '2023-12-31'
    # Calculate time series
    evi_time_series = calculate_time_series_EVI(collection_name, start_date, end_date, aoi)
    # Plot EVI
    plot_time_series_EVI(evi_time_series)
"""

import ee
import pandas as pd
import matplotlib.pyplot as plt

def select_bands(image, index_name):
    """Selects specific bands from a Sentinel-2 image

    Parameters
    ----------
    image : ee.Image
        The satellite image
    index_name : str
        The name of the band to select ('RED', 'GREEN', 'BLUE', 'NIR')

    Returns
    -------
    Image
        with the selected band.
    """
    
    band_mapping = {
        'RED': 'B4',
        'GREEN': 'B3',
        'BLUE': 'B2',
        'NIR': 'B8'
    }

    if index_name in band_mapping:
        return image.select(band_mapping[index_name])
    else:
        raise ValueError("Unsupported index! Available: RED, GREEN, BLUE, NIR")

def aggregate_image_collection(collection_name, start_date, end_date, aggregation_method):
    """Aggregates an image collection using the input method and time frame

    Parameters
    ----------
    collection_name : str
        The name of the image collection.
    start_date : str
        The start date of the period (in YYYY-MM-DD format)
    end_date : str
        The end date of the period (in YYYY-MM-DD format)
    aggregation_method : str
        The method of aggregation ('mean', 'median', 'sum', 'min', 'max')

    Returns
    -------
    image
        aggregated
    """
    
    ee.Initialize()
    
    collection = ee.ImageCollection(collection_name).filterDate(start_date, end_date)
    
    if aggregation_method == 'mean':
        return collection.mean()
    elif aggregation_method == 'median':
        return collection.median()
    elif aggregation_method == 'sum':
        return collection.sum()
    elif aggregation_method == 'min':
        return collection.min()
    elif aggregation_method == 'max':
        return collection.max()
    else:
        raise ValueError("Wrong aggregation method! Available: mean, median, sum, min, max")

def calculateEVI(image, blue, red, nir):
    """Calculates the EVI
    
    Parameters
    ----------
    image : ee.Image
    blue : str
        The name of the blue band
    red : str
        The name of the red band
    nir : str
        The name of the near-infrared band

    Returns
    -------
    Image
        with the EVI band
    """

    evi = image.expression(
        '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))',
        {
            'NIR': nir,
            'RED': red,
            'BLUE': blue
        })
    return evi.rename('EVI')

def calculate_time_series_EVI(collection_name, start_date, end_date, aoi):
    """Calculates a time series of the EVI

    Parameters
    ----------
    collection_name : str
        The name of the Sentinel-2 image collection
    start_date : str
        The start date of the period
    end_date : str
        The end date of the period
    aoi : ee.Geometry
        The area of interest

    Returns
    -------
    DataFrame with the time series of EVI.
    """
  
    ee.Initialize()
    
    collection = ee.ImageCollection(collection_name).filterDate(start_date, end_date).filterBounds(aoi)
    
    def calc_evi(image):
        blue_band = select_bands(image, 'BLUE')
        red_band = select_bands(image, 'RED')
        nir_band = select_bands(image, 'NIR')
        evi = calculateEVI(image, blue_band, red_band, nir_band)
        return evi.set('system:time_start', image.get('system:time_start'))

    evi_collection = collection.map(calc_evi)

    def reduce_region(image):
        mean_value = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=aoi,
            scale=30
        )
        return ee.Feature(None, {
            'date': ee.Date(image.get('system:time_start')).format('YYYY-MM-dd'),
            'EVI': mean_value.get('EVI')
        })

    features = evi_collection.map(reduce_region).getInfo()['features']

    dates = [f['properties']['date'] for f in features]
    values = [f['properties']['EVI'] for f in features]

    time_series = pd.DataFrame({
        'Date': pd.to_datetime(dates),
        'EVI': values
    }).set_index('Date')
    
    return time_series

def plot_time_series_EVI(time_series):
    """Plotting the time series of the EVI

    Parameters
    ----------
    time_series : DataFrame
        The time series data
    """
    
    plt.figure(figsize=(10, 5))
    plt.plot(time_series.index, time_series['EVI'], marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('EVI')
    plt.title('Time Series of EVI')
    plt.grid(True)
    plt.show()
