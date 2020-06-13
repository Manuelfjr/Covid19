import pandas as pd

def concat():
    regionbrconfirm = pd.read_csv('regionbrconfirm.csv')
    regionbrdeaths = pd.read_csv('regionbrdeaths.csv')

    statebrconfirm = pd.read_csv('statebrconfirm.csv')
    statebrdeaths = pd.read_csv('statebrdeaths.csv')

    # Concatenando imagens
    regionbrconfirm['image'] = pd.read_csv('imageregion.csv',sep=',')
    regionbrdeaths['image'] = pd.read_csv('imageregion.csv',sep=',')

    statebrconfirm['image'] = pd.read_csv('imagestate.csv',sep=',')
    statebrdeaths['image'] = pd.read_csv('imagestate.csv',sep=',')

    # Reescrevendo os csv
    regionbrconfirm.to_csv('regionbrconfirm.csv')
    regionbrdeaths.to_csv('regionbrdeaths.csv')

    statebrconfirm.to_csv('statebrconfirm.csv')
    statebrdeaths.to_csv('statebrdeaths.csv')

if __name__ == "__main__":
    concat()
