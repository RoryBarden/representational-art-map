import folium

# will probably have one map with both photos and paintings shown
# hopefully will add a bunch of filters (i.e. show only photos from 1921-1964, etc.)
main_map = folium.Map()
# keep name as index.html for github pages to work
main_map.save("index.html")