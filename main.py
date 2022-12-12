from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="McCdama")
location = geolocator.geocode("Seestr. 18/1 72764")
print((location.latitude, location.longitude))
print(location.raw)
print(location)