#%% Setup
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
countries = [
'ALB',
'AUT',
'AND',
'BEL',
'BGR',
'BIH',
'BLR',
'CHE',
'CYP',
'CZE',
'DNK',
'EGY',
'ESP',
'FRA',
'GIB',
'GRC',
'HRV',
'IRL',
'ISL',
'LIE',
'LTU',
'LUX',
'LVA',
'MAC',
'MCO',
'MDA',
'MKD',
'MLT',
'NOR',
'POL',
'PRK',
'PRT',
'ROU',
'SMR',
'SVK',
'SVN',
'SWE',
'VAT',
'XKO',
'EST',
'FIN',
'UKR',
'SRB',
'MNE',
'ITA',
'DEU',
'TUR',
'GBR',
'RUS',
'IRN',
'ARM',
'AZE',
'GEO',
'NLD',
'LBY',
'DZA',
'TUN',
'PSE',
'ISR',
'LBN',
'JOR',
'SYR',
'MAR',
'SAU',
'IRQ']

def list_country(mypath):

    from os.path import isfile, join
    from os import listdir

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    countries = {f.split('_')[1]for f in onlyfiles if f.find('gadm36_') != -1}
    return countries

def test_list_country():
    countries = list_country('/Users/samuel/Downloads/gadm36_CHN_shp')
    print(countries)


def draw_eu():

    plt.figure(figsize=(16,8))
    m = Basemap()
    #m = Basemap(llcrnrlon=-7, llcrnrlat = 32, urcrnrlon=50, urcrnrlat=57, projection= 'lcc' , lat_0 = 46, lon_0=15)
    m.arcgisimage()
    for i in range(len(countries)):
        m.readshapefile('/Users/tony/MyWork/python/gadm36_eur_shp/gadm36_' + countries[i] + '_shp/gadm36_' + countries[i] + '_0', 'states', drawbounds=True)

    #m.readshapefile('/Users/tony/MyWork/python/gadm36_IND_shp/gadm36_IND_0', 'states', drawbounds=True)
    #m.readshapefile('/Users/tony/MyWork/python/gadm36_levels_shp/gadm36_0', 'states', drawbounds=True)
    #m.drawrivers(color='blue',linewidth=0.3)
    '''parallels = np.linspace(30,75,5)
    m.drawparallels(parallels,labels=[True,False,False,False])
    meridians = np.linspace(-10,90,5)
    m.drawmeridians(meridians,labels=[False,False,False,True])
    #m.drawlsmask(land_color='coral',ocean_color='aqua',lakes='')
    #m.bluemarble()'''
    
    plt.title(r'$Europe$',fontsize=24)
    plt.show()

draw_eu()
