# Species Total DBH
# Xinyuan Wei
# 2020/8/28

'''
The program calculates the total DBH of each species.
'''

import pandas as pd

# Read the data.
file='Luquillo_ForestGEO.csv'
data=pd.read_csv(file)
# print(data)

# Results matrix.
Results=pd.DataFrame()
header=['Species','Area(DBH)'] 
Results_arr=[]

Species_list=data.Latin.unique()
#print(Species_list)
N_Species=len(Species_list)
#print(N_Species)

for i in range (N_Species):
    temp=[]
    #print(Species_list[i])
    species_data=data.loc[data['Latin']==Species_list[i]]
    temp.append(Species_list[i])
    temp.append(species_data['DBH'].sum())
    #print(temp)
    Results_arr.append(temp)

Results=pd.DataFrame(data=Results_arr)
Results.to_csv('Species_DBH_Rank.csv', index=False, header=header)
