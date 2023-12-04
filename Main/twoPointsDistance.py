from math import radians, cos, sin, asin, sqrt

def calculate_distance(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    km = 6371* c # 6371 = earth radius in km

    return km

lat1 = 43.37012643
lon1 = -8.39114853
lat2 = 38.99588053
lon2 = -1.85574745

print(calculate_distance(lon1, lat1, lon2, lat2))
