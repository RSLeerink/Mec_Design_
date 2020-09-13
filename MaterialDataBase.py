from pandas import DataFrame
import pandas as pd

import os.path
from os import path




MaterialName = 'S355'

"""

OutputFileName = 'StellDataBase.csv'
InputFileName  = OutputFileName

InputData = {   'MaterialName'              : [MaterialName], 
                'Youngs modulus [Mpa]  '    : 210000        ,
                'Yield strength [Mpa]  '    : 355           ,
                'Tensile strenght [Mpa]'    : 470}

"""

def AddMaterial(data,OutputFileName):
    #Adds material to the material data
    df = DataFrame(data=data)
    df = df.set_index('MaterialName')



    #If the output file exist add to it
    if path.exists(str(OutputFileName)) == True:
        print('Input file found')
        df_fromcsv = pd.read_csv(OutputFileName)
        df_fromcsv = df_fromcsv.set_index('MaterialName')

        if MaterialName in df_fromcsv.index:
            print('Value alrady in database, not adding it to database')
        else:
            print('Adding new material')
            print(df)
            df = df_fromcsv.append(df)
            df.to_csv(OutputFileName)

        #print(df_fromcsv)

    #if there is not outputfiel create it
    if path.exists(str(OutputFileName)) == False:
        print('File not found, making new file')
        df.to_csv(OutputFileName)
        #print(df_fromcsv)
            
    #print(df_fromcsv)
    print('')

    
    return df

def PrintDatabase(OutputFileName):
    df_fromcsv = pd.read_csv(OutputFileName)
    df_fromcsv = df_fromcsv.set_index('MaterialName')
    print(df_fromcsv)
    return

def ReadData(InputFileName,MaterialName):
    df_fromcsv = pd.read_csv(InputFileName)
    df_fromcsv = df_fromcsv.set_index('MaterialName')
    MaterialData = df_fromcsv.loc[MaterialName]
    
    print()
    print('Material data')
    print(MaterialData)
    print()

    YoungsModulus   = MaterialData[0]
    YieldStrength   = MaterialData[1]
    TensileStrenght = MaterialData[2]

    #Ouput
    # 0 - YoungsModulus
    # 1 - YieldStrength
    # 2 - TensileStrenght

    return YoungsModulus,YieldStrength,TensileStrenght



#ReadData(InputFileName,MaterialName)
#AddMaterial(InputData,OutputFileName)
#PrintDatabase(OutputFileName)