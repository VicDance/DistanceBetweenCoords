from tkinter import filedialog
from math import radians,cos,sin
import pandas as pd
import numpy as np
#from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# To make this code work we need a CSV file with the coordinates

## This code only works if there are many coordinates ##

def read_csv():
    file = filedialog.askopenfilename()

    return pd.read_csv(file, encoding='unicode_escape', sep=";")

def get_distance():
    cities = read_csv()

    lat = cities["Latitude"].map(radians)
    lon = cities["Longitude"].map(radians)
    x = lon.map(cos)*lat.map(cos)*6371 #6371 = earth radius in km
    y= lon.map(cos)*lat.map(sin)*6371 

    cities["lat_radians"] = lat
    cities["lon_radians"] = lon
    cities["x"] = x
    cities["y"] = y
    cities.head()

    print("x: ", x)
    print("y: ", y)

    cities_drop = cities.drop(["Latitude", "Longitude", "lat_radians", "lon_radians"], axis = 1)
    cities_drop.head()

    print("cities: ", cities_drop)

    df = cities_drop.copy()

    scaler = MinMaxScaler(feature_range=(0, 2), copy=True)
    scaled_df = scaler.fit_transform(df)
    print("scaled_df_1: ", scaled_df)
    scaled_df = pd.DataFrame(scaled_df, columns=['x1', 'x2'])
    print("scaled_df: ", scaled_df)

get_distance()

# lat1 = 43.37012643
# lon1 = -8.39114853
# lat2 = 38.99588053
# lon2 = -1.85574745

# get_distance(lat1, lon1, lat2, lon2)
