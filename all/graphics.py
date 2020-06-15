import argparse
import os as os
import sys

modules = 'argparse os'.split(' ')

install, k = [], 0
for i in modules:
    if (i in sys.modules ) == False:
        install.append(i)
        print(install[k])
        k+=1

if len(install) >= 1:
    print('----------------------------------------------------------')
    for i in range(len(install)):
        print('Suggestion :' + '\n \n' + 'pip install {}'.format(install[i]))
        print()
    sys.exit()


def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--date', dest='date',
                        type=str,
                        default='6/11/20',
                        help='''date maps''')
    parser.add_argument('-nc', '--numcountries', dest='nc',
                        type=int,
                        default=6,
                        help='''number country''')
    return parser.parse_args()

def graphics(date='6/11/20',nc=6):
    images = 'images'
    import seaborn as sns
    import pandas as pd
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go
    
    sns.set_style('darkgrid')

    db_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    db_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    db_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    db_deaths_country = db_deaths.groupby(['Country/Region']).sum()
    db_confirmed_country = db_confirmed.groupby(['Country/Region']).sum()
    db_recovered_country = db_recovered.groupby(['Country/Region']).sum()
    db_deaths_country.drop(['Lat','Long'],axis=1,inplace=True)
    db_confirmed_country.drop(['Lat','Long'],axis=1,inplace=True)
    db_recovered_country.drop(['Lat','Long'],axis=1,inplace=True)

    #Confirmados
        
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in db_confirmed_country[date].sort_values(ascending = False)[:nc].index:
        ax.plot(range(db_confirmed_country.T.shape[0]), db_confirmed_country.T[i],label=i)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Confirmados')
    plt.title('Confirmados por COVID-19, para os {} Maiores Países - {}'.format(nc,date.split('/')[1]+'/'+date.split('/')[0]+'/'+date.split('/')[2]))
    plt.legend()
    plt.savefig(os.path.join(images,'confirmedcovid.png'))

    #Mortos
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in db_deaths_country[date].sort_values(ascending = False)[:nc].index:
        ax.plot(range(db_deaths_country.T.shape[0]), db_deaths_country.T[i],label=i)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Mortos')
    plt.title('Mortes por COVID-19, para os {} Maiores Países - {}'.format(nc,date.split('/')[1]+'/'+date.split('/')[0]+'/'+date.split('/')[2]))
    plt.legend()
    plt.savefig(os.path.join(images,'deathscovid.png'))

    #Recuperados
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in db_recovered_country[date].sort_values(ascending = False)[:nc].index:
        ax.plot(range(db_recovered_country.T.shape[0]), db_recovered_country.T[i],label=i)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Recuperados')
    plt.title('Recuperados por COVID-19, para os {} Maiores Países - {}'.format(nc,date.split('/')[1]+'/'+date.split('/')[0]+'/'+date.split('/')[2]))
    plt.legend()
    plt.savefig(os.path.join(images,'revoredcovid.png'))
    

if __name__ == '__main__':
    args = parse_arguments()
    graphics(**vars(args))