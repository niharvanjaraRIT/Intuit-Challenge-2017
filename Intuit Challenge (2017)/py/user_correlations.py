
#### Author: Nihar Vanjara 
#### Contact: niv1676@g.rit.edu

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    #####################################################################
    # In order to execute the code without errors #
    # The path should be set to locate "Reduced-Data.csv"
    #####################################################################
    df = pd.read_csv('D:\\PyProjects\\Intuit\\Reduced-Data.csv')
    
    ## Plot the correlation matrix between users.
    
    df=df.set_index('auth_id')
    df = df.T.corr()
    df[df < 0] = 0.0
    print(df)
    
    # mask half of the correlation matrix
    mask = np.zeros_like(df, dtype=np.bool)
    
    mask[np.triu_indices_from(mask)] = True
    
    f, ax = plt.subplots(figsize=(50, 50))
    
    cmap = sns.diverging_palette(220, 20, sep=20, as_cmap=True)
    
    # Generate heat map
    sns.heatmap(df, mask=mask, cmap=cmap,vmin=0,vmax=1.0,
            square=True, xticklabels=5, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
    
    # Set plot properties 
    ax.yaxis.label.set_size(30)
    ax.xaxis.label.set_size(30)
    ax.set_title('Correlation between users',fontsize= 30)
    plt.show()
    df.to_csv('User-Correlation.csv')

if __name__ == '__main__':
    main()