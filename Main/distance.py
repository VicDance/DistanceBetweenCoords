from math import radians,cos,sin
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def get_distance(lat1, lon1, lat2, lon2):
    lat1_radians = radians(lat1)
    lon1_radians = radians(lon1)

    lat2_radians = radians(lat2)
    lon2_radians = radians(lon2)

    x1 = cos(lon1_radians)*cos(lat1_radians)*6371
    y1 = cos(lon1_radians)*sin(lat1_radians)*6371

    x1_y1 = [x1, y1]
    x1_y1 = np.asarray(x1_y1)
    print("x1_y1: ", x1_y1)

    x2 = cos(lon2_radians)*cos(lat2_radians)*6371
    y2 = cos(lon2_radians)*sin(lat2_radians)*6371

    x2_y2 = [x2, y2]
    x2_y2 = np.asarray(x2_y2)
    print("x2_y2: ", x2_y2)

    x_y_concatenate = [x1_y1, x2_y2]
    x_y_concatenate = np.asarray(x_y_concatenate)
    print("concatenate: ", x_y_concatenate)

    scaler = MinMaxScaler()
    scaled_df_x_y = scaler.fit_transform(x_y_concatenate)
    print("scaled_x_y: ", scaled_df_x_y)

    # x1_train, y1_train = train_test_split(x1_y1, test_size=0.2)
    # print("train_x1", x1_train)
    # print("train_y1", y1_train)
    # x2_train, y2_train = train_test_split(x2_y2, test_size=0.2)
    # print("train_x2", x2_train)
    # print("train_y2", y2_train)

    # x1_y1_train = [x1_train, y1_train]
    # x1_y1_train = np.asarray(x1_y1_train)
    # print("x1_y1_train", x1_y1_train)

    # x2_y2_train = [x2_train, y2_train]
    # x2_y2_train = np.asarray(x2_y2_train)
    # print("x2_y2_train", x2_y2_train)

    # x_y_concatenate = np.concatenate((x1_y1_train, x2_y2_train), axis = 1)
    # print("concatenate: ", x_y_concatenate)

    # scaler = MinMaxScaler(feature_range=(0, 100), copy=True)
    # scaled_df_x_y = scaler.fit_transform(x_y_concatenate)
    # print("scaled_x_y: ", scaled_df_x_y)

    # scaled_df_x2_y2 = scaler.fit_transform(x2_y2_train)
    # print("scaled_x2: ", scaled_df_x2_y2[0:5])


lat1 = 43.37012643
lon1 = -8.39114853
lat2 = 38.99588053
lon2 = -1.85574745

get_distance(lat1, lon1, lat2, lon2)
