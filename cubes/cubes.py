from die import Die
import pygal

die1 = Die()
die2 = Die()
res=[]

for i in range(1000):
	tmp = die1.roll()+die2.roll()
	res.append(tmp)
fre=[]

for i in range(2,die2.num_sides+die1.num_sides+1):
	fre.append(res.count(i))
print(fre)

visu = pygal.Bar()

visu.title ="result of Die"
visu.x_labels = [str(i) for i in range(die1.num_sides-die2.num_sides+2,die1.num_sides+die2.num_sides+1)]
visu.x_title = "Nu of dIE"
visu.y_title ="Freq"

visu.add('D6',fre)
visu.render_to_file('report.svg')
