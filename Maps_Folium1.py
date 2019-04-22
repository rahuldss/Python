import folium

map=folium.Map(location=[28.6382943,77.3764699],zoom_start=9,tiles='Mapbox Bright')
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[28.6382943,77.3764699],popup="My Location",icon=folium.Icon(color='green')))

for cords in [[28.6382943,77.3764699],[28.6482943,77.3864699]]:
    fg.add_child(folium.Marker(location=[cords[0],cords[1]],popup="My Location",icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map_Folium.html")
