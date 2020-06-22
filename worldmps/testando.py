'''
import pandas as pd
locs = {
    'AC': [ -8.77, -70.55]
  , 'AL': [ -9.71, -35.73]
  , 'AM': [ -3.07, -61.66]
  , 'AP': [  1.41, -51.77]
  , 'BA': [-12.96, -38.51]
  , 'CE': [ -3.71, -38.54]
  , 'DF': [-15.83, -47.86]
  , 'ES': [-19.19, -40.34]
  , 'GO': [-16.64, -49.31]
  , 'MA': [ -2.55, -44.30]
  , 'MG': [-18.10, -44.38]
  , 'MS': [-20.51, -54.54]
  , 'MT': [-12.64, -55.42]
  , 'PA': [ -5.53, -52.29]
  , 'PB': [ -7.06, -35.55]
  , 'PE': [ -8.28, -35.07]
  , 'PI': [ -8.28, -43.68]
  , 'PR': [-24.89, -51.55]
  , 'RJ': [-22.84, -43.15]
  , 'RN': [ -5.22, -36.52]
  , 'RO': [-11.22, -62.80]
  , 'RR': [  1.89, -61.22]
  , 'RS': [-30.01, -51.22]
  , 'SC': [-27.33, -49.44]
  , 'SE': [-10.90, -37.07]
  , 'SP': [-23.55, -46.64]
  , 'TO': [-10.25, -48.25]
}
datalocs = pd.DataFrame(locs,index=['Lat','Long']).T
df = pd.read_csv('statebrconfirm.csv')
df['lat'] = datalocs['Lat'].values
df['long'] = datalocs['Long'].values

import plotly.graph_objects as go
import plotly.express as px
fig = px.density_mapbox(df, lat='lat', lon='long', z='21/6', radius=80,
                        center=dict(lat=-15, lon=-50), zoom=3,title='Mapa de calor do número de confirmados no Brasil')
fig.update_layout(mapbox_style="carto-darkmatter", mapbox_center_lon=-60)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},meta={'title': 'Mapa de calor'})

fig.show()
'''

'''
import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px
locs = {
    'AC': [ -8.77, -70.55]
  , 'AL': [ -9.71, -35.73]
  , 'AM': [ -3.07, -61.66]
  , 'AP': [  1.41, -51.77]
  , 'BA': [-12.96, -38.51]
  , 'CE': [ -3.71, -38.54]
  , 'DF': [-15.83, -47.86]
  , 'ES': [-19.19, -40.34]
  , 'GO': [-16.64, -49.31]
  , 'MA': [ -2.55, -44.30]
  , 'MG': [-18.10, -44.38]
  , 'MS': [-20.51, -54.54]
  , 'MT': [-12.64, -55.42]
  , 'PA': [ -5.53, -52.29]
  , 'PB': [ -7.06, -35.55]
  , 'PE': [ -8.28, -35.07]
  , 'PI': [ -8.28, -43.68]
  , 'PR': [-24.89, -51.55]
  , 'RJ': [-22.84, -43.15]
  , 'RN': [ -5.22, -36.52]
  , 'RO': [-11.22, -62.80]
  , 'RR': [  1.89, -61.22]
  , 'RS': [-30.01, -51.22]
  , 'SC': [-27.33, -49.44]
  , 'SE': [-10.90, -37.07]
  , 'SP': [-23.55, -46.64]
  , 'TO': [-10.25, -48.25]
}
datalocs = pd.DataFrame(locs,index=['Lat','Long']).T
df = pd.read_csv('statebrconfirm.csv')
df['lat'] = datalocs['Lat'].values
df['long'] = datalocs['Long'].values

import plotly.graph_objects as go
import plotly.express as px

fig = px.scatter_mapbox(df, lat="lat", lon="long", hover_data=["Estado", "21/6"],
                        zoom=3, height=600,size_max=60000)
fig.update_layout(mapbox_style="carto-darkmatter")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
'''
import pandas as pd
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/Manuelfjr/Covid19/master/worldmps/testando/idpolygon.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv('mundo.csv')

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df['city'], z=df['last_available_confirmed'],
                                    colorscale="Viridis", zmin=0, zmax=300000,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
