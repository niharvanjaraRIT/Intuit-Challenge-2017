
#### Author: Nihar Vanjara 
#### Contact: niv1676@g.rit.edu

import pandas as pd
import numpy as np
from sklearn.preprocessing import normalize

def display(relatedFeatures):
    '''
    the function prints all the categories which have related features.
    '''
    index = 1
    
    print("\nThe related features are grouped into categories as shown below\n")
    
    for all in relatedFeatures:
        print('Category',index)
        print('\n')
        for feature in all:
            print(feature)
        index += 1
        print('\n')
        
def main():
    
    print(" The program is running..")
    # frame list is a list containing information of all data files 
    # where each index location stores one dataframe object.
    frameList = [None] * 100
    
    # Read .csv files using pandas and store the objects in the list frameList.
    for i in range(100):
        
            #####################################################################
            # Change the path below in order to execute the code without errors #
            # The path should be able to locate files in the data folder.
            #####################################################################
        frameList[i] = pd.read_csv('D:\\PyProjects\\Intuit\\data\\user-' + str(i) + '.csv')
    

    uniqueVendors = []      # List of unique 'vendors'
    uniqueLocations = []    # List of unique 'locations'
    uniqueIDs = []          # List of unique 'IDs'
    uniqueDates = []        # List of unique 'dates'
    
    
    for i in range(len(frameList)):
        
        uniqueIDs += set(frameList[i].iloc[:,0].tolist())
        uniqueLocations += frameList[i].iloc[:,-1].tolist()
        uniqueVendors += frameList[i].iloc[:,-3].tolist()
        uniqueDates += frameList[i].iloc[:,-4].tolist()
        
        #### UNCOMMENT THE TWO LINES BELOW TO PRINT MISSING VALUES IN A FRAME  ####
        
        # print('Missing Values in Frame {0}: {1}'
        #      .format(i,frameList[i].isnull().sum().sum()))
    
    
    uniqueDates  = set(uniqueDates)
    # print(len(uniqueDates))            # UNCOMMENT THIS LINE to view number of unique dates
    
    uniqueVendors = set(uniqueVendors)
    # print(len(uniqueVendors))          # UNCOMMENT THIS LINE to view number of unique vendors
    
    uniqueLocations = set(uniqueLocations)
    # print(len(uniqueLocations))        # UNCOMMENT THIS LINE to view number of locations vendors
    
    uniqueIDsFrame = pd.DataFrame(uniqueIDs,columns=['auth_id'])  
    # print(uniqueIDsFrame)              # UNCOMMENT THIS LINE to view unique IDs
      
    uniqueVendorsFrame = pd.DataFrame(list(uniqueVendors),columns=['Unique Vendors']).sort_values(['Unique Vendors'])
    uniqueLocationsFrame = pd.DataFrame(list(uniqueLocations),columns=['Unique Location'])
      
    # print(uniqueVendorsFrame)    # UNCOMMENT to view unique Vendors
      
    uniqueVendorsFrame.to_csv('Unique-Vendors.csv',index=False)
       
    # Uncomment the lines below to view the 
    # print(uniqueVendors)
    # print(uniqueLocations)
     
    # features is a list of unique vendors  
    features = list(uniqueVendors)
    features.sort()
     
    # transformedFrame will be the new table
    transformedFrame = pd.DataFrame([],columns= features)
   
     
    # for loop below iterates through every dataframe in framelist 
    # and drops irrelevant columns. A groupby operation is performed 
    # on 'Vendor' and the sum of the amounts for each vendor is calculated
    # the new data is stored in transformed frame.
     
    for i in range(len(frameList)):
        frameList[i].drop(frameList[i].columns[[0,1,4]], axis=1, inplace=True)
         
        for feature in features:
            if feature not in frameList[i][' Vendor']:
                frameList[i] = frameList[i].append(pd.DataFrame([[feature, 0.0]],columns=[' Vendor', ' Amount']))
         
        p = frameList[i].groupby([' Vendor']).sum().T.iloc[0]
        transformedFrame = transformedFrame.append(p)
        
    transformedFrame = transformedFrame.reset_index(level=0)
    transformedFrame.columns = ['auth_id'] + features
    transformedFrame['auth_id'] = uniqueIDsFrame['auth_id'].values
    
    transformedFrame.to_csv('Transformed-Data.csv',index=False)
     
    # Calcualte the correlation of the features to check relevant features 
    correlation = transformedFrame.corr()
    
    correlation.to_csv('Correlation-Features.csv')   
    
    # print(correlation)
     
    # return indices in correlation for values greater than 0.7
    indices = np.where(correlation > 0.7)
     
    # store features in the form of a tuple such that 
    # feature x is not equal to feature y 
    indices = [(x,y) for x, y in zip(*indices) if x != y and x < y]
     
    # correlatedFeatures is a list consisting of a set of categories.  
    correlatedFeatures = []
    co = set()
    seen = set()
     
    # iterate through every correlated order pair and combine them into distinct sets/categories  
    for ind in indices:
           
        if correlation.index[ind[0]] in seen or correlation.columns[ind[1]] in seen:
            continue
        if len(co) == 0:
            co.add(correlation.index[ind[0]])
            co.add(correlation.columns[ind[1]])
        elif correlation.index[ind[0]] in co and correlation.columns[ind[1]] not in co:
            co.add(correlation.columns[ind[1]])
        elif correlation.index[ind[0]] not in co and correlation.columns[ind[1]] in co:
            co.add(correlation.index[ind[0]])
        else:
            correlatedFeatures.append(co)
            seen |= co
            co = set()
     
    # print the categories of correlatedFeatures calulated as above        
    display(correlatedFeatures)
       
    # create a dictionary with key as category name and value as the set of distinct features  
    newCategories = ({'Fitness/Sports':correlatedFeatures[0],  
                    'Geek':correlatedFeatures[1],
                    'ArtMusic':correlatedFeatures[2],  
                    'Late Payment':correlatedFeatures[3],
                    'Outdoors/Partying':correlatedFeatures[4],
                    'Indoors':correlatedFeatures[5], 
                    })
       

     
    # Perform the merge operation of columns and merge columns belonging to one category.
    # new column is created consisting of the merged columns. the old columns are then dropped
      
    for category,values in newCategories.items():
        transformedFrame[category] = 0.0
        for sub_category in values:
            transformedFrame[category] += transformedFrame[sub_category] 
            transformedFrame.drop(sub_category, axis=1, inplace=True)

     
 
    # create a new column restaurants and merge with other related columns
    transformedFrame['restaurants'] = (transformedFrame['Restaurant - Burgers'] +
                                       transformedFrame['Restaurant - Chinese'] +
                                       transformedFrame['Restaurant - Pizza'] +
                                       transformedFrame['Restaurant - Steakhouse'])
    


    # drop columns merged above   
    transformedFrame.drop(['Restaurant - Burgers','Restaurant - Pizza',
                           'Restaurant - Chinese','Restaurant - Steakhouse'],
                           axis=1, inplace=True)


    # create a new travel column and merge related columns  
    transformedFrame['travel'] = (transformedFrame['Best Western Hotel'] +
                                  transformedFrame['Cancun Beach Resort'] +
                                  transformedFrame['Comfort Inn'] +
                                  transformedFrame['Public Transportation - Bus Pass'] +
                                  transformedFrame['Public Transportation - Train Pass'] +
                                  transformedFrame['Taxi'] +
                                  transformedFrame['Southwest Flights - Cancun'] +
                                  transformedFrame['Uber'] +
                                  transformedFrame['Lyft'])
     
    # drop columns merged above   
    transformedFrame.drop(['Best Western Hotel','Cancun Beach Resort',
                           'Comfort Inn','Public Transportation - Bus Pass',
                           'Public Transportation - Train Pass','Taxi',
                           'Southwest Flights - Cancun','Uber','Lyft'],
                           axis=1, inplace=True)
     
    # create utilites column and merge related columns   
    transformedFrame['utilites'] = (transformedFrame['Gas & Electric'] +
                                    transformedFrame['Water & Sewer'] +
                                    transformedFrame['Time Warner Cable'])
       
    # drop columns merged above    
    transformedFrame.drop(['Gas & Electric','Water & Sewer',
                           'Time Warner Cable'],
                           axis=1, inplace=True)    
    # create child care column and merge related columns     
    transformedFrame['child care'] = (transformedFrame['Babies "R" Us'] +
                                  transformedFrame['BuyBuyBaby.com'] +
                                  transformedFrame['Hospital - Prenatal Care'] +
                                  transformedFrame['Amazon Order - Baby Crib'])
     
    # drop columns merged above      
    transformedFrame.drop(['Babies "R" Us','BuyBuyBaby.com',
                           'Hospital - Prenatal Care','Amazon Order - Baby Crib'],
                           axis=1, inplace=True)
     
    # create student loans column and merge related columns     
    transformedFrame['student loans'] = (transformedFrame['ACS - Student Loans'] +
                                    transformedFrame['Navient - Student Loans'])        
     
    # drop columns merged above     
    transformedFrame.drop(['ACS - Student Loans',
                           'Navient - Student Loans'],
                           axis=1, inplace=True)
     
    # create housing column and merge related columns     
    transformedFrame['housing'] = (transformedFrame['Hamilton Move & Storage'] +
                                  transformedFrame['Home Depot'] +
                                  transformedFrame['Housing Rent'] +
                                  transformedFrame['Refrigerator Depot'] +
                                  transformedFrame['Mark\'s Movers'] +
                                  transformedFrame['Jerome\'s Furniture'] +
                                  transformedFrame['FedEx Shipping'])
     
    # drop columns merged above 
    transformedFrame.drop(['Hamilton Move & Storage','Home Depot',
                           'Housing Rent','Refrigerator Depot','FedEx Shipping',
                           'Mark\'s Movers','Jerome\'s Furniture'],
                           axis=1, inplace=True)    
     
    # create groceries column and merge related columns     
    transformedFrame['groceries'] = (transformedFrame['Ralph\'s Grocery Store'] +
                                  transformedFrame['Sprouts Market'] +
                                  transformedFrame['Von\'s Groceries'] +
                                  transformedFrame['Whole Foods'] 
                                  )
    # drop columns merged above     
    transformedFrame.drop(['Ralph\'s Grocery Store','Sprouts Market',
                           'Von\'s Groceries','Whole Foods'],
                           axis=1, inplace=True) 
    # create miscellaneous column and merge related columns     
    transformedFrame['misc'] = (transformedFrame['Kay Jewelry'] +
                                  transformedFrame['Wedding Planner'] +
                                  transformedFrame['Netflix Subscription'] +
                                  transformedFrame['Starbucks Coffee'] 
                                  )
    

     
    # drop columns merged above   
    transformedFrame.drop(['Kay Jewelry','Wedding Planner',
                           'Netflix Subscription','Starbucks Coffee'],
                           axis=1, inplace=True)     
    
    
    # writes the merged data into a .csv file 
    transformedFrame.to_csv('Merged-Data.csv',index=False)    
    
    print("The variance of each feature is as follows\n")
                  
    for category in transformedFrame.keys():
        tmp = transformedFrame[category].as_matrix().reshape(1,-1).astype(float)
        print(category,np.var(normalize(tmp,norm='l2')))
       
    transformedFrame.drop(['restaurants','travel','housing'],
                           axis=1, inplace=True)    
       

    # writes the reduced dataframe into a .csv file        
    transformedFrame.to_csv('Reduced-Data.csv',index=False)
       
         


if __name__ == '__main__':
    main()