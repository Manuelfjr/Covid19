import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
import argparse as argparse
cf.go_offline()
sns.set_style('darkgrid')

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='6/11/20',
                        help='''date maps''')
    parser.add_argument('-nc', '--nc', dest='nc',
                        type=int,
                        default=6,
                        help='''number country''')
    return parser.parse_args()

def covid19(date='6/11/20',nc=6):
    db_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    db_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    db_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    db_deaths_country = db_deaths.groupby(['Country/Region']).sum()
    db_confirmed_country = db_confirmed.groupby(['Country/Region']).sum()
    db_recovered_country = db_recovered.groupby(['Country/Region']).sum()

    db_deaths_country.drop(['Lat','Long'],axis=1,inplace=True)
    db_confirmed_country.drop(['Lat','Long'],axis=1,inplace=True)
    db_recovered_country.drop(['Lat','Long'],axis=1,inplace=True)

    maxdeaths = db_deaths_country[date].sort_values(ascending=False)[:nc]

    tldeaths = pd.DataFrame(np.zeros((db_deaths_country.T.shape[0],db_deaths_country.T.shape[1])), index = range(db_deaths_country.T.shape[0]), columns=db_deaths_country.T.columns)
    for i in maxdeaths.index:
        for j in range(len(tldeaths.index)):
            if db_deaths_country.T[i][j] == 0:
                tldeaths[i][j] = 0
            else:
                tldeaths[i][j] = (db_deaths_country.T[i][j])/(db_confirmed_country.T[i][j])
    
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in  maxdeaths.index:
        ax.plot(range(1,tldeaths.shape[0]+1), tldeaths[i],label=i)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Incremento médio')
    plt.title('Taxade letalidade para os {} paises com maior numero de mortos'.format(nc))
    plt.legend()
    plt.savefig('letalityrate.png')

if __name__ == '__main__':
    args = parse_arguments()
    covid19(**vars(args))