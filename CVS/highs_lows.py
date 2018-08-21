import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'death_valley_2014.csv'
with open(filename) as f:
	reder = csv.reader(f)
	header_row = next (reder)
	max_t=[]
	dates=[]
	min_t=[]
	for row in reder:
		try:
			strp_date = datetime.strptime(row[0],"%Y-%m-%d")
			Ma = int(row[1])
			Mi = int(row[3])
		except:
			print(strp_date," Missing Data")
		else:
			dates.append(strp_date)
			max_t.append(Ma)
			min_t.append(Mi)

	print(max_t)
fig = plt.figure(dpi=361, figsize=(10,6))
plt.plot(dates,max_t,c='red')
plt.plot(dates,min_t,c='blue')
plt.fill_between(dates,max_t,min_t,facecolor='blue',alpha=0.5)
plt.title(filename.split('.')[0], fontsize=24)
plt.xlabel('Days',fontsize=5)
plt.ylabel('temp', fontsize=16)
plt.tick_params(axis='both',which='both',labelsize=5,length=1)

plt.show()