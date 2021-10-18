from math import radians, cos, sin, asin, sqrt
t = input("Enter latitude and longitude for first city separated by a space ")
a = tuple(float(x) for x in t.split())
t1 = input("Enter latitude and longitude for second city separated by a space ")
a1 = tuple(float(x) for x in t1.split())

print("City1: "+str(a[0])+" N"+", "+str(a[1])+" W")
print("City2: "+str(a1[0])+" N"+", "+str(a1[1])+" W")
def haversine(lon1, lat1, lon2, lat2):
    
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    print("City 1 and City 2 are ",round(c * r)," km apart")



haversine(a[1],a[0],a1[1],a1[0])