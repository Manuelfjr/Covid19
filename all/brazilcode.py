import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import argparse as argparse
import os as os

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Runs all the code''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--datebr', dest='datebr',
                        type=str,
                        default='11/6',
                        help='''datebr maps''')
    parser.add_argument('-t', '--today', dest='days',
                        type=int,
                        default=30,
                        help='''today ''')
    parser.add_argument('-w', '--weeks', dest='weeks',
                        type=int,
                        default=5,
                        help='''today ''')
    parser.add_argument('-nw', '--n_weeks', dest='n_weeks',
                        type=int,
                        default=14,
                        help='''number weeks ''')
    parser.add_argument('-n', '--ncountries', dest='n',
                        type=int,
                        default=10,
                        help='''number of countries''')
    return parser.parse_args()

def brazilcode(datebr='11/6', days=30, weeks=5, n_weeks=13, n=10):
    sns.set_style('darkgrid')
    images, folder = 'images','datasets'
    if not os.path.exists(images):
        os.makedirs(images)
    if not os.path.exists(folder):
        os.makedirs(folder)

    confirmbr = pd.read_csv('https://raw.githubusercontent.com/elhenrico/covid19-Brazil-timeseries/master/confirmed-cases.csv')

    deathsbr = pd.read_csv('https://raw.githubusercontent.com/elhenrico/covid19-Brazil-timeseries/master/deaths.csv')

    confirmbr['Cidade'] = confirmbr['Unnamed: 0']
    confirmbr['Estado'] = confirmbr['Unnamed: 1']

    deathsbr['Cidade'] = deathsbr['Unnamed: 0']
    deathsbr['Estado'] = deathsbr['Unnamed: 1']

    confirmbr.drop(['Unnamed: 0','Unnamed: 1'],axis=1,inplace=True)
    deathsbr.drop(['Unnamed: 0','Unnamed: 1'],axis=1,inplace=True)

    confirmbr = confirmbr.groupby(['Estado']).sum().T
#    jbr = confirmbr['BR']
    confirmbr.drop(['BR'],axis=1,inplace=True)

    deathsbr = deathsbr.groupby(['Estado']).sum().T
    jbr = deathsbr['BR']
    deathsbr.drop(['BR'],axis=1,inplace=True)

    statebrconfirm = confirmbr.iloc[:,5:]
    regionbrconfirm = confirmbr[['(CO)','(N)','(NE)','(S)','(SE)']]

    statebrdeaths = deathsbr.iloc[:,5:]
    regionbrdeaths = deathsbr[['(CO)','(N)','(NE)','(S)','(SE)']]

    regionbrconfirm.columns.name = 'Regiao'
    regionbrdeaths.columns.name = 'Regiao'
    
    regionbrconfirm.T.to_csv(os.path.join(folder,'regionbrconfirm.csv'), index=None)
    regionbrdeaths.T.to_csv(os.path.join(folder,'regionbrdeaths.csv'), index=None)
    statebrconfirm.T.to_csv(os.path.join(folder,'statebrconfirm.csv'), index=None)
    statebrdeaths.T.to_csv(os.path.join(folder,'statebrdeaths.csv'), index=None)
    
    
    #regionbrconfirm.T.to_csv(os.path.join(folder,'regionbrconfirm.csv'))
    #regionbrdeaths.T.to_csv(os.path.join(folder,'regionbrdeaths.csv'))

    #statebrconfirm.T.to_csv(os.path.join(folder,'statebrconfirm.csv'))
    #statebrdeaths.T.to_csv(os.path.join(folder,'statebrdeaths.csv'))

    maxconfirmregion = regionbrconfirm.T[datebr].sort_values(ascending=False)
    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxconfirmregion.index:
        ax.plot(range(regionbrconfirm.shape[0]), regionbrconfirm[i],label=i)
        ax.set_xlim(0,len(regionbrconfirm.index))
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Confirmados')
    plt.title('Acumulado de casos confirmados por COVID-19 (Por Região)- Brasil, {}'.format(datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'cumconfirmregion.png'))

    regionpercconfirm = pd.DataFrame(np.zeros((regionbrconfirm.shape[0],regionbrconfirm.shape[1])), index = regionbrconfirm.index, columns=regionbrconfirm.columns)
    for i in regionbrconfirm.columns:
        for j in range(regionbrconfirm.shape[0]-1):
            if regionbrconfirm[i][j] != 0:
                regionpercconfirm[i][j+1] = ((regionbrconfirm[i][j+1]- regionbrconfirm[i][j])/regionbrconfirm[i][j])
    a = pd.DataFrame(regionpercconfirm.T[datebr].sort_values(ascending = True))
    ixmaxconf = a.index

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in ixmaxconf:
        ax.plot(range(regionpercconfirm.shape[0]), regionpercconfirm[i],label=i)
        ax.set_xlim(regionbrconfirm.shape[0] - days,regionbrconfirm.shape[0])
        ax.set_ylim(0,0.150)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Incremento')
    plt.title('Incremento de confirmados por COVID-19 no Brasil por Região, para os ultimos {} dias - {}'.format(days,datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'confirmratedaysregion.png'))

    idmeanconfirmregion = pd.DataFrame(np.zeros((n_weeks,regionbrconfirm.shape[1])), index = range(n_weeks), columns=regionbrconfirm.columns)
    a = 0
    for i in regionbrconfirm.columns:
        for j in range(n_weeks):
            idmeanconfirmregion[i][j] = (regionpercconfirm[i][a:(a+7)].mean())
            a = a + 7
        a = 0

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxconfirmregion.index:
        ax.plot(range(1,idmeanconfirmregion.shape[0]+1), idmeanconfirmregion[i],label=i)
        ax.set_xlim(n_weeks - weeks,n_weeks)
        ax.set_ylim(0,0.150)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Incremento médio')
    plt.title('Incremento médio de confirmados para as {} últimas semanas, por COVID-19 no Brasil, por Região. Semana {} a semana {} de contagio - {}'.format(weeks,n_weeks - weeks,n_weeks,datebr + '/20'+ '.'))
    plt.legend()
    plt.savefig(os.path.join(images,'confirmrateweeksregion.png'))

    maxconfirmstate = statebrconfirm.T[datebr].sort_values(ascending=False)[:n]

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxconfirmstate.index:
        ax.plot(range(statebrconfirm.shape[0]), statebrconfirm[i],label=i)
        ax.set_xlim(0,len(statebrconfirm.index))
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Confirmados')
    plt.title('Acumulado de casos confirmados por COVID-19 (Por Estado)- Brasil, {}'.format(datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'cumconfirmstate.png'))

    statepercconfirm = pd.DataFrame(np.zeros((statebrconfirm.shape[0],statebrconfirm.shape[1])), index = statebrconfirm.index, columns=statebrconfirm.columns)
    for i in statebrconfirm.columns:
        for j in range(statebrconfirm.shape[0]-1):
            if statebrconfirm[i][j] != 0:
                statepercconfirm[i][j+1] = ((statebrconfirm[i][j+1]- statebrconfirm[i][j])/statebrconfirm[i][j])
    b = pd.DataFrame(statepercconfirm.T[datebr].sort_values(ascending = True))
    ixmaxconf =  b.T[maxconfirmstate.index].columns

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in ixmaxconf:
        ax.plot(range(statepercconfirm.shape[0]), statepercconfirm[i],label=i)
        ax.set_xlim(statebrconfirm.shape[0] - 30,statebrconfirm.shape[0])
        ax.set_ylim(0,0.35)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Incremento')
    plt.title('Incremento de casos confirmados por COVID-19 no Brasil por Estado, para os {} dias. {}'.format(days,datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'confirmratedaysstate.png'))

    idmeanconfirmstate = pd.DataFrame(np.zeros((n_weeks,statebrconfirm.shape[1])), index = range(n_weeks), columns=statebrconfirm.columns)
    a = 0
    for i in statebrconfirm.columns:
        for j in range(n_weeks):
            idmeanconfirmstate[i][j] = (statepercconfirm[i][a:(a+7)].mean())
            a = a + 7
        a = 0

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxconfirmstate.index:
        ax.plot(range(1,idmeanconfirmstate.shape[0]+1), idmeanconfirmstate[i],label=i)
        ax.set_xlim(n_weeks - weeks,n_weeks)
        ax.set_ylim(0.02,0.2)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Incremento médio')
    plt.title('Incremento médio de casos confirmados para as {} últimas semanas, por COVID-19 no Brasil, por Estado. Semana {} a semana {} de contagio - {}'.format(weeks,n_weeks - weeks,n_weeks,datebr + '/20'+ '.'))
    plt.legend()
    plt.savefig(os.path.join(images,'confirmrateweeksstate.png'))

    maxdeathsregion = regionbrdeaths.T[datebr].sort_values(ascending=False)

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxconfirmregion.index:
        ax.plot(range(regionbrdeaths.shape[0]), regionbrdeaths[i],label=i)
        ax.set_xlim(0,len(regionbrdeaths.index))
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Mortos')
    plt.title('Acumulado de mortos por COVID-19 (Por Região)- Brasil, {}'.format(datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'cumdeathsregion.png'))

    regionpercdeaths = pd.DataFrame(np.zeros((regionbrdeaths.shape[0],regionbrdeaths.shape[1])), index = regionbrdeaths.index, columns=regionbrdeaths.columns)
    for i in regionbrdeaths.columns:
        for j in range(regionbrdeaths.shape[0]-1):
            if regionbrdeaths[i][j] != 0:
                regionpercdeaths[i][j+1] = ((regionbrdeaths[i][j+1]- regionbrdeaths[i][j])/regionbrdeaths[i][j])
    a = pd.DataFrame(regionpercdeaths.T[datebr].sort_values(ascending = True))
    ixmaxdeaths = a.index

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in ixmaxdeaths:
        ax.plot(range(regionpercdeaths.shape[0]), regionpercdeaths[i],label=i)
        ax.set_xlim(regionbrdeaths.shape[0] - 30,regionbrdeaths.shape[0])
        ax.set_ylim(0,0.150)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Incremento')
    plt.title('Incremento de mortos, de um dia para o outro, por COVID-19 no Brasil por Região, para os ultimos {} dias. {}'.format(days,datebr +'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'deathsratedaysregion.png'))

    idmeandeathsregion = pd.DataFrame(np.zeros((n_weeks,regionbrdeaths.shape[1])), index = range(n_weeks), columns=regionbrdeaths.columns)
    a = 0
    for i in regionbrdeaths.columns:
        for j in range(n_weeks):
            idmeandeathsregion[i][j] = (regionpercdeaths[i][a:(a+7)].mean())
            a = a + 7
        a = 0

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxdeathsregion.index:
        ax.plot(range(1,idmeandeathsregion.shape[0]+1), idmeandeathsregion[i],label=i)
        ax.set_xlim(n_weeks - weeks,n_weeks)
        ax.set_ylim(0,0.150)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Incremento médio')
    plt.title('Incremento médio de mortos, de um dia para o outro, para as {} últimas semanas, por COVID-19 no Brasil, por Região. Semana {} a semana {} de contagio - {}'.format(weeks,n_weeks - weeks,n_weeks,datebr + '/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'deathsrateweeksregion.png'))

    maxdeathsstate = statebrdeaths.T[datebr].sort_values(ascending=False)[:n]

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxdeathsstate.index:
        ax.plot(range(statebrdeaths.shape[0]), statebrdeaths[i],label=i)
        ax.set_xlim(0,len(statebrdeaths.index))
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Número de Confirmados')
    plt.title('Acumulado de mortes por COVID-19 (Por Estado) - Brasil, {}'.format(datebr+'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'cumdeathsstate.png'))

    statepercdeaths = pd.DataFrame(np.zeros((statebrdeaths.shape[0],statebrdeaths.shape[1])), index = statebrdeaths.index, columns=statebrdeaths.columns)
    for i in statebrdeaths.columns:
        for j in range(statebrdeaths.shape[0]-1):
            if statebrdeaths[i][j] != 0:
                statepercdeaths[i][j+1] = ((statebrdeaths[i][j+1]- statebrdeaths[i][j])/statebrdeaths[i][j])
    b = pd.DataFrame(statepercdeaths.T[datebr].sort_values(ascending = True))
    ixmaxdeaths =  b.T[maxdeathsstate.index].columns

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in ixmaxdeaths:
        ax.plot(range(statepercdeaths.shape[0]), statepercdeaths[i],label=i)
        ax.set_xlim(statebrdeaths.shape[0] - 30,statebrdeaths.shape[0])
        ax.set_ylim(0,0.27)
    plt.xlabel('Dia do Contágio')
    plt.ylabel('Incremento')
    plt.title('Incremento de mortos, de um dia para o outro, por COVID-19 no Brasil por Estado, para os ultimos {} dias. {}'.format(days,datebr+'/20'+'.'))
    plt.legend()
    plt.savefig(os.path.join(images,'deathsratedaysstate.png'))

    idmeandeathsstate = pd.DataFrame(np.zeros((n_weeks,statebrdeaths.shape[1])), index = range(n_weeks), columns=statebrdeaths.columns)
    a = 0
    for i in statebrdeaths.columns:
        for j in range(n_weeks):
            idmeandeathsstate[i][j] = (statepercdeaths[i][a:(a+7)].mean())
            a = a + 7
        a = 0

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxdeathsstate.index:
        ax.plot(range(1,idmeandeathsstate.shape[0]+1), idmeandeathsstate[i],label=i)
        ax.set_xlim(n_weeks - weeks,n_weeks)
        ax.set_ylim(0.02,0.3)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Incremento médio')
    plt.title('Incremento médio de mortos, de um dia para o outro, para as {} últimas semanas, por COVID-19 no Brasil, por Estado. Semana {} a semana {} de contagio - {}'.format(weeks,n_weeks - weeks,n_weeks, datebr + '/20' + '.'))
    plt.legend()
    plt.savefig(os.path.join(images,'deathsrateweeksstate.png'))

    plt.figure(figsize=(18,10))
    sns.heatmap(idmeandeathsregion.T.corr().loc[range(3,n_weeks),range(3,n_weeks)],cmap='Reds',annot=True)
    plt.title('Mapa de calor do incremento médio de mortos, de um dia para o outro, nas ultimas {} semanas, por COVID-19 no Brasil, por Região - {}'.format(n_weeks,datebr + '/20' + '.,'))
    plt.savefig(os.path.join(images,'heatmapregionweeksdeathscorr.png'))

    plt.figure(figsize=(18,10))
    sns.heatmap(idmeandeathsregion.corr(),cmap='Reds',annot=True)
    plt.title('Mapa de calor das correlações de incremento médio de mortos, de um dia para o outro, por COVID-19 no Brasil, por Região - {}'.format(datebr +'/20'+'.'))
    plt.savefig(os.path.join(images,'heatmapregiondeathscorr.png'))

    tlregiondeaths = pd.DataFrame(np.zeros((regionbrdeaths.shape[0],regionbrdeaths.shape[1])), index = range(regionbrdeaths.shape[0]), columns=regionbrdeaths.columns)
    for i in regionbrdeaths.columns:
        for j in range(len(regionbrdeaths.index)):
            if regionbrconfirm[i][j] == 0:
                tlregiondeaths[i][j] = 0
            else:
                tlregiondeaths[i][j] = (regionbrdeaths[i][j])/(regionbrconfirm[i][j])

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxdeathsregion.index:
        ax.plot(range(1,tlregiondeaths.shape[0]+1), tlregiondeaths[i],label=i)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Taxa')
    plt.title('Taxa de letalidade do COVID-19, por região - {}'.format(datebr + '/20' + '.'))
    plt.legend()
    plt.savefig(os.path.join(images,'letalityratebrregion.png'))

    tlstatedeaths = pd.DataFrame(np.zeros((statebrdeaths.shape[0],statebrdeaths.shape[1])), index = range(statebrdeaths.shape[0]), columns=statebrdeaths.columns)
    for i in statebrdeaths.columns:
        for j in range(len(statebrdeaths.index)):
            if statebrconfirm[i][j] == 0:
                tlstatedeaths[i][j] = 0
            else:
                tlstatedeaths[i][j] = (statebrdeaths[i][j])/(statebrconfirm[i][j])

    fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(16,8))
    for i in maxdeathsstate.index:
        ax.plot(range(1,tlstatedeaths.shape[0]+1), tlstatedeaths[i],label=i)
    plt.xlabel('Semana do Contágio')
    plt.ylabel('Taxa')
    plt.title('Taxa de letalidade do COVID-19, por região - {}'.format(datebr + '/20' + '.'))
    plt.legend()
    plt.savefig(os.path.join(images,'letalityratebrstate.png'))

if __name__ == '__main__':
    args = parse_arguments()
    brazilcode(**vars(args))