from Beams import Cantilever_LeftEndFree_RighEndFixed
from MaterialDataBase import ReadData
from SectionSettings import TeeSection

W = 35000 #N
l = 250
a = 50


MaterialInput    = ReadData('StellDataBase.csv','S355')

SectionInput     = TeeSection(300,50,5,5)


Cantilever_LeftEndFree_RighEndFixed(W,l,a,MaterialInput,SectionInput)


#Test

#Work!