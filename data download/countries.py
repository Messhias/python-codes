import pygal

worldmap_chart = pygal.maps.world.World()

for country_code in sorted(world_map_chart.keys()):
    print(country_code,COUNTRIES[country_code])
