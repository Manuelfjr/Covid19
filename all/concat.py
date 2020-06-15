import pandas as pd
import os as os
def concat():

    folder,root = 'datasets', '.others'
    regionbrconfirm = pd.read_csv(os.path.join(folder,'regionbrconfirm.csv'))
    regionbrdeaths = pd.read_csv(os.path.join(folder,'regionbrdeaths.csv'))

    statebrconfirm = pd.read_csv(os.path.join(folder,'statebrconfirm.csv'))
    statebrdeaths = pd.read_csv(os.path.join(folder,'statebrdeaths.csv'))
        
    # Concatenando imagens/poptotalregion
    regionbrconfirm['image'],regionbrconfirm['poptotalregion'] = pd.read_csv(os.path.join(root,'.imageregion.csv'),sep=',')['image'],pd.read_csv(os.path.join(root,'.imageregion.csv'),sep=',')['poptotalregion'] 
    regionbrdeaths['image'], regionbrdeaths['poptotalregion'] = pd.read_csv(os.path.join(root,'.imageregion.csv'),sep=',')['image'],pd.read_csv(os.path.join(root,'.imageregion.csv'),sep=',')['poptotalregion'] 

    statebrconfirm['image'] = pd.read_csv(os.path.join(root,'.imagestate.csv'),sep=',')
    statebrdeaths['image'] = pd.read_csv(os.path.join(root,'.imagestate.csv'),sep=',')
    
    # Reescrevendo os csv
    regionbrconfirm.to_csv(os.path.join(folder,'regionbrconfirm.csv'))
    regionbrdeaths.to_csv(os.path.join(folder,'regionbrdeaths.csv'))

    statebrconfirm.to_csv(os.path.join(folder,'statebrconfirm.csv'))
    statebrdeaths.to_csv(os.path.join(folder,'statebrdeaths.csv'))

if __name__ == "__main__":
    concat()
