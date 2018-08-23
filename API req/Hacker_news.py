import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
names=[]
for submission_id in submission_ids[:15]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    tmp =response_dict['title'].split(' ')
    names.append(tmp[0])
    submission_dict = {
        'label': response_dict['title'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'value': response_dict['score']
        }
    submission_dicts.append(submission_dict)
    
#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            #reverse=True)

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
chart.title = 'News'
chart.x_labels=names

chart.add('',submission_dicts)
chart.render_to_file('Hi_news.svg')