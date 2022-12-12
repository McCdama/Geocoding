from functools import partial
from geopy.geocoders import Nominatim
import folium

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

print("===============Folium===============")
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
tooltip = "Click me!"
folium.Marker(
    [location.latitude, location.longitude],
    popup="<i>Home sweet Home!</i>",
    tooltip=tooltip,
    icon=folium.Icon(color="red", icon="info-sign"),
    radius=50,
).add_to(m)

m.save("index.html")


