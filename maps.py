#%% Setup

from pyecharts.globals import CurrentConfig, NotebookType

CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar

#%% Setup
myMap =  Map()
myMap.add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
myMap.set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        )

#%% Setup
#myMap.show_config()
#%%
myMap.render()
#%%
myMap.load_javascript()
myMap.render_notebook()


#%%

from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
bar.load_javascript()
bar.render()

#%% Setup
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20, 100)
plt.plot(x, np.sin(x))
plt.show()


#%% Setup
myMap =  Map()
myMap.add("商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china")
myMap.set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        )



#myMap.show_config()
myMap.render()