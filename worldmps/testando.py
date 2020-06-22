
from urllib.request import urlopen
import json
with urlopen('dados.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv('statebrconfirm.csv')

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df['Estado'], z=df['21/6'],
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
