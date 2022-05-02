# Species TRY_ID
# Xinyuan Wei
# 2020/8/28

'''
The program creates a list of TRY species ID of all the species.
'''

import pandas as pd

# Read the data.
ID_file='Try_AccSpecies.csv'
ID_data=pd.read_csv(ID_file, encoding='ISO-8859-1')
#print(data)

Species_file='Try_Species_Selected.csv'
Species_data=pd.read_csv(Species_file)
#print(Species_data)

result=[]

for i in range (len(Species_data)):
    species=Species_data['Species'].at[i]
    #print(species)
    
    Index=ID_data.index[ID_data['AccSpeciesName']==species].tolist()[0]
    #print(Index)
    ID=ID_data['AccSpeciesID'].at[Index]
    #print(ID)
    result.append(ID)
    
print(result)

