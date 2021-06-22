import leafleter.generator

with open("output.html", 'w') as outfile:
  outfile.write(leafleter.generator.get_html_page_prefix("website title", 50.06, 19.93))
  outfile.write(leafleter.generator.get_marker("text", 50.06, 19.93))
  outfile.write(leafleter.generator.get_marker("text2", 50.06, 19.94))
  outfile.write(leafleter.generator.get_marker("text3", 50.06, 19.95))
  outfile.write(leafleter.generator.get_circle_marker("circle", 50.07, 19.94, radius_in_px = 10))
  outfile.write(leafleter.generator.get_circle_marker("circle", 50.07, 19.96, radius_in_px = 10, options = {"color": '"red"'}))
  outfile.write(leafleter.generator.get_line(50.06, 19.92, 170, 0, color = 'blue'))
  shape = [[50.06, 19.93], [50.05, 19.80], [50.02, 19.83], [50.06, 19.93]]
  outfile.write(leafleter.generator.get_polygon(shape, color = "green", fill_color = "green"))


  geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "nananananana",
        "popupContent": "50/20"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [20, 50]
    }
  }
  outfile.write(leafleter.generator.get_geojson_placing(geojsonFeature))
  outfile.write(leafleter.generator.get_html_page_suffix())