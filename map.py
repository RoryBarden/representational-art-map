import folium
import pandas

# will probably have one map with both photos and paintings shown
# hopefully will add a bunch of filters (i.e. show only photos from 1921-1964, etc.)
main_map = folium.Map(location=(0, 0), zoom_start=3)

artworks = pandas.read_csv("artworks.csv")

for index, artwork in artworks.iterrows():
    # same html for every popup (will make look nicer!)
    # the format call can definitely be done better
    html = """
            <h1>{artwork}</h1>
            <a href="geo:{latitude},{longitude}">
                <p>{latitude}, {longitude}</p>
            </a>
            <h2>{artist}, {year}</h2>
            <h3>{type}, {movement}</h3>
            <a href={artwork_fullsize}>
                <img src={artwork_small} style="width:50em;">
            </a>
            <p>{description}</p>""".format(artwork = artwork['artwork'],
                                           latitude = artwork['latitude'],
                                           longitude = artwork['longitude'] ,
                                           artist = artwork['artist'], 
                                           year = artwork['year'], 
                                           type = artwork['type'], 
                                           movement = artwork['movement'], 
                                           artwork_small = artwork['artwork_small'],
                                           artwork_fullsize = artwork['artwork_fullsize'], 
                                           description = artwork['description'])
    # lazy loading bc far too many images (hopefully)
    folium.Marker(
        location=[artwork['latitude'], artwork['longitude']],
        popup=html,
        lazy=True
    ).add_to(main_map)

# map should be embedded into index.html
# but i can't be bothered atm
main_map.save("index.html")