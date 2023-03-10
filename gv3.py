import os

import pandas as pd
from dotenv import load_dotenv
from geopy.geocoders import GoogleV3

load_dotenv()
GOOGLE_API_KEY = os.getenv('google_api_key')

geolocater = GoogleV3(api_key=GOOGLE_API_KEY)

# Set the columns you want to use in the initial csv
addressessColumns = []
# Set the columns you want to carry over to your geocoded.csv and notFound.csv final documents
finalColumnsGeoCoded = []
finalColumnsNotFound = []

df = pd.read_csv('places.csv')
addresses = df[addressessColumns]

geocoded=pd.DataFrame(columns=finalColumnsGeoCoded, index=[0])
notFound=pd.DataFrame(columns=finalColumnsNotFound, index=[0])

for index, address in enumerate(df['address']):
    location = geolocater.geocode(address)
    if(location):
		# Enter your column names
        geocoded.loc[len(geocoded.index)] = [addresses['LPST ID'][index], addresses['Regulated Entity Number'][index], location.latitude, location.longitude]
    else:
        # Enter your column names
        notFound.loc[len(notFound.index)] = [addresses['LPST ID'][index], addresses['Regulated_Entity Number'][index], address]
        
geocoded.to_csv('geocoded_places.csv')
notFound.to_csv('notFound.csv')