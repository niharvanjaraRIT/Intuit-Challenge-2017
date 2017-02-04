
#### Author: Nihar Vanjara 
#### Contact: niv1676@g.rit.edu

import pandas as pd
import numpy as np

def main():
    
    #####################################################################
    # In order to execute the code without errors #
    # The path should be set to locate "Reduced-Data.csv"
    #####################################################################
    
    df = pd.read_csv('D:\\PyProjects\\Intuit\\Reduced-Data.csv')
    
    ### The features are derived as shown below and new columns are created.
    
    # Divorcee
    df['divorcee'] = np.where(df['Divorce Lawyer Fees']<0,'Yes', 'No')
    
    # Hobies (Fitness/Sports)
    df['Hobies (Fitness/Sports)'] = np.where(df['Fitness/Sports']<0,'Yes', 'No')
    
    # Hobbies (Reading/Muesums)
    df['Hobbies (Reading/Muesums)'] = np.where(df['Geek']<0,'Yes', 'No')
    
    # Hobbies (Art/Music)
    df['Hobbies (Reading/Muesums)'] = np.where(df['Geek']<0,'Yes', 'No')
    
    # Hobbies (Socialize/Partying)
    df['Hobbies (Socialize/Partying)'] = np.where(df['Outdoors/Partying']<0,'Yes', 'No')
    
    # likes indoor
    df['likes indoor'] = np.where(df['Indoors']<-2000,'Yes', 'No')
    
    # Parent
    df['Parent'] = np.where(df['child care']<0,'Yes', 'No')
    
    # Student
    df['Student'] = np.where(df['student loans']<0,'Yes', 'No')
    
    # has Credit Card
    df['Has Credit Card'] = np.where(df['Credit Card Payment']<0,'Yes', 'No')
    
    # unpunctual
    df['unpunctual'] = np.where(df['Late Payment']<0,'Yes', 'No')
    
    # income Strata (High/Medium/Low)
    
    high = np.percentile(df['Paycheck'], 70)
    low  = np.percentile(df['Paycheck'], 30)
    df['income Strata'] = np.where(df['Paycheck'] > high, 'High', 'Medium')
    df['income Strata'] = np.where(df['Paycheck'] < low, 'Low', df['income Strata'])

    # Free Utilites
    df['Free Utilites'] = np.where(df['utilites']<0,'Yes', 'No')
    
    print(df) 
    
    # Write Final Data into a file.
    df.to_csv('Final-Data.csv',index=False)
    

if __name__ == '__main__':
    main()