from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Line
from pyecharts.globals import ChartType, SymbolType
import json
import requests

def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    mydata = json.loads(requests.get(url=url).json()['data'])
    return mydata

     

virus_data = get_data()
china_daily = virus_data['chinaDayList']
china_add = virus_data['chinaDayAddList']
dates = []
dates_add = []
dead_add = []
heal_add = []
num_confirmed = []
num_add = [0,0,0,4,17,136]
percentage_add = []

for day in china_daily:
    dates.append(day['date'])
    num_confirmed.append(int(day['confirm']))

for day in china_add:
    dates_add.append(day['date'])
    num_add.append(int(day['confirm']))
    dead_add.append(day['dead'])
    heal_add.append(day['heal'])

for i in range(1,len(num_add)):
    percentage = round(num_add[i]/num_confirmed[i],2)
    percentage_add.append(percentage)
    


def date_line() -> Line:
    c = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("累计确诊病例", num_confirmed)
        .add_yaxis("新增确诊病例", num_add)
        .set_global_opts(title_opts=opts.TitleOpts(title="全国确诊数"))
    )
    c.render()
    return

def dead_heal() -> Line:
    c = (
        Line()
        .add_xaxis(dates_add)
        .add_yaxis("新增死亡病例", dead_add)
        .add_yaxis("新增治愈病例", heal_add)
        .set_global_opts(title_opts=opts.TitleOpts(title="全国新增死亡/治愈数"))
    )
    c.render()
    return

def percentage_growth() -> Line:
    c = (
        Line()
        .add_xaxis(dates)
        .add_yaxis("日增长率", percentage_add)
        .set_global_opts(title_opts=opts.TitleOpts(title="全国病例增长率"))
    )
    c.render()
    return




date_line()
dead_heal()
percentage_growth()