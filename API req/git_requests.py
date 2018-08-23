import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

print('Status:', r.status_code)

response_dict = r.json()

print("Total res",response_dict['total_count'])

repo_dicts = response_dict['items']
print("reps return",len(repo_dicts))

name,stars = [],[]
prlot_dcts=[]# configure data for pygal for more information by addint extended dic
for repo_dict in repo_dicts:
	name.append(repo_dict['name'])
	pr_dc = {
	'value':repo_dict['stargazers_count'],
	'label': str(repo_dict['description']),
	'xlink':repo_dict['html_url']
	}
	prlot_dcts.append(pr_dc)
	

my_cnf =pygal.Config()
my_cnf.x_label_rotation=45
my_cnf.show_legend = False
my_cnf.title_font_size =24
my_cnf.lable_font_size =14
my_cnf.major_label_font_size = 18
my_cnf.truncate_label =15
my_cnf.show_y_guides = False
#my_cnf.width = 1000


my_style =  LS('#333366',base_style=LCS)
chart = pygal.Bar(my_cnf,style=my_style)
chart.title = 'Most-Starred python github'
chart.x_labels=name

chart.add('',prlot_dcts)
chart.render_to_file('pythonrepos.svg')
	