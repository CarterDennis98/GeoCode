import pandas as pd
from geopy.geocoders import Nominatim

geolocater = Nominatim(user_agent="osm_geocode")

df = pd.read_csv('places.csv')
addresses = df[['LPST ID', 'Regulated Entity Number', 'place']]

geocoded=pd.DataFrame(columns=['LPST ID', 'Regulated Entity Number', 'lat', 'long'], index=[0])
notFound=pd.DataFrame(columns=['LPST ID', 'Regulated Entity Number', 'address'], index=[0])

for index, address in enumerate(addresses['address']):
    location = geolocater.geocode(address)
    if(location):
        geocoded.loc[len(geocoded.index)] = [addresses['LPST ID'][index], addresses['Regulated Entity Number'][index], location.latitude, location.longitude]
    else:
        notFound.loc[len(notFound.index)] = [addresses['LPST ID'][index], addresses['Regulated Entity Number'][index], address]
        
geocoded.to_csv('geocoded_places.csv')
notFound.to_csv('notFound.csv')