from functools import partial
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="McCdama")
location = geolocator.geocode("Seestr. 18/1 72764")
print("===============Standard===============")
print((location.latitude, location.longitude))
print(location.raw)
print(location)
print("===============/Standard===============")


print("===============Reversed===============")
reversedLocation = geolocator.reverse("48.489232349999995, 9.219866345516573")
print(reversedLocation.address)
print((reversedLocation.latitude, reversedLocation.longitude))
print(reversedLocation.raw)
print("===============/Reversed===============")

print("===============Func tool parameter===============")
geocode = partial(geolocator.geocode, language="ar")
print(geocode("london"))


print("===============/Func tool parameter===============")

