import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import argparse
import os as os

cf.go_offline()

sns.set_style('darkgrid')

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-r', '--run', dest='run',
                        type=bool,
                        default=True,
                        help='''run maps''')
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='6/10/20',
                        help='''date maps''')
    parser.add_argument('-b', '--bool', dest='bool',
                        type=bool,
                        default=False,
                        help='''boolean value''')
    parser.add_argument('-f', '--folder', dest='folder',
                        type=str,
                        default='dataworldr',
                        help='''folder name''')
    parser.add_argument('-n', '--filename', dest='filename',
                        type=str,
                        default='recovered.csv',
                        help='''file name ''')
    parser.add_argument('-t', '--type', dest='type',
                        type=str,
                        default='rwm',
                        help='''type (confirmed,deaths,recovered) ''')
    return parser.parse_args()

def rwm(run=True, date='6/10/20',bool=True,folder='dataworldr',filename='recovered.csv',type='rwm'):
    if bool == False:
        db_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv', index_col=0)
        if not os.path.exists(folder):
            os.makedirs(folder)
        db_recovered.to_csv(os.path.join(folder, filename), index=None)
    else:
        db_recovered = pd.read_csv(os.path.join(folder, filename))

    db_recovered_country = db_recovered.groupby(['Country/Region']).sum()
    db_recovered_country.drop(['Lat','Long'],axis=1,inplace=True)

    if run == True:
        data = dict(type='choropleth',
                    colorscale = 'blues_r',
                    reversescale = True,
                    locations = db_recovered_country.index,
                    z = db_recovered_country[date],
                    locationmode = 'country names',
                    marker = dict(line = dict(color = 'rgb(0,0,0)',width =1)),
                    colorbar = {'title':"Recuperados confirmados"},
                    text = date
                    ) 
        layout = dict(title = 'Mapa do número de recuperados do COVID-19, por país - {}'.format(date.split('/')[1] + '/'  + date.split('/')[0] + '/' + date.split('/')[2] + '.'),
                    geo = dict(scope='world',
                                showframe = True,
                                projection = {'type':'natural earth'})
                    )

        choromap = go.Figure(data = [data],layout = layout)
        iplot(choromap,validate=False,image_width=15000, image_height=1000)
    else:
        print(pd.DataFrame(db_recovered_country))

if __name__ == '__main__':
    args = parse_arguments()
    rwm(**vars(args))