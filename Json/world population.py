import json
from conutry_codes import get_country_code as gcc
import pygal


filename = 'population_data.json'
cc_population = {}
with open(filename) as f:
	pop_data = json.load(f)

for  pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		contry_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = gcc(contry_name)
		if code:
			cc_population[code] = population

#group 
cc_group1,cc_group2,cc_group3 = {},{},{}
for co,po in cc_population.items():
	if po < 10000000:
		cc_group1[co]=po
	elif po < 1000000000:
		cc_group2[co]=po
	else:
		cc_group3[co]=po
#print(cc_population)
wm_style = pygal.style.RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = " Population 2010"
wm.add('0-10m',cc_group1)
wm.add('10m-1bn',cc_group2)
wm.add('>1bn',cc_group3)
#wm.render()
wm.render_to_file('world_population.svg')