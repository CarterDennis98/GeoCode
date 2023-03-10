import os

import pandas as pd
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3

load_dotenv()
GOOGLE_API_KEY = os.getenv('google_api_key')

geolocater = GoogleV3(api_key=GOOGLE_API_KEY)

df = pd.read_csv('places.csv')
addresses = df[['LPST ID', 'Regulated Entity Number', 'place']]

geocoded=pd.DataFrame(columns=['LPST ID', 'Regulated Entity Number', 'lat', 'long'], index=[0])
notFound=pd.DataFrame(columns=['LPST ID', 'Regulated Entity Number', 'address'], index=[0])

for index, address in enumerate(df['address']):
    location = geolocater.geocode(address)
    if(location):
        geocoded.loc[len(geocoded.index)] = [addresses['LPST_ID'][index], addresses['Regulated_Entity_Number'][index], location.latitude, location.longitude]
    else:
        notFound.loc[len(notFound.index)] = [addresses['LPST_ID'][index], addresses['Regulated_Entity_Number'][index], address]
        
geocoded.to_csv('geocoded_places.csv')
notFound.to_csv('notFound.csv')