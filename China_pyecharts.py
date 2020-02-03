from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo,Map
from pyecharts.globals import ChartType, SymbolType
import json
import requests
from pyecharts_javascripthon.dom import alert

def on_click():
    alert("点击事件触发")


def get_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    mydata = json.loads(requests.get(url=url).json()['data'])
    return mydata


def get_individual_cities():
    global max_num
    global cities_data
    global province_data
    for province in province_data:
        name = province['name']
        city_data = province['children']
        confirm = 0
        dead = 0
        heal = 0
        for city in city_data:
            data = city['total']
            confirm += data['confirm']
            dead += data['dead']
            heal += data['heal']
        if name == '浙江':
            max_num = confirm
        mydata.append([name,confirm])

     

virus_data = get_data()

province_data = virus_data['areaTree'][0]['children']

mydata = []
max_num = 0
get_individual_cities()



def map_virus() -> Map:
    global mydata
    global max_num
    c = (
        Map()
        .add("确诊病例", mydata, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-全国地图"),
            visualmap_opts=opts.VisualMapOpts(max_=max_num),
        )
    )
    c.on("click",on_click)
    c.render()

map_virus()
