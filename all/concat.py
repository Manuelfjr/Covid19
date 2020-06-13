import pandas as pd

def concat():
    regionbrconfirm = pd.read_csv('regionbrconfirm.csv')
    regionbrdeaths = pd.read_csv('regionbrdeaths.csv')

    statebrconfirm = pd.read_csv('statebrconfirm.csv')
    statebrdeaths = pd.read_csv('statebrdeaths.csv')

    # Concatenando imagens/poptotalregion
    regionbrconfirm['image'],regionbrconfirm['poptotalregion'] = pd.read_csv('imageregion.csv',sep=',')['image'],pd.read_csv('imageregion.csv',sep=',')['poptotalregion'] 
    regionbrdeaths['image'], regionbrdeaths['poptotalregion'] = pd.read_csv('imageregion.csv',sep=',')['image'],pd.read_csv('imageregion.csv',sep=',')['poptotalregion'] 

    statebrconfirm['image'] = pd.read_csv('imagestate.csv',sep=',')
    statebrdeaths['image'] = pd.read_csv('imagestate.csv',sep=',')

    # Reescrevendo os csv
    regionbrconfirm.to_csv('regionbrconfirm.csv')
    regionbrdeaths.to_csv('regionbrdeaths.csv')

    statebrconfirm.to_csv('statebrconfirm.csv')
    statebrdeaths.to_csv('statebrdeaths.csv')

if __name__ == "__main__":
    concat()
