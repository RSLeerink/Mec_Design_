from Beams import Cantilever_LeftEndFree_RighEndFixed
from MaterialDataBase import ReadData
from SectionSettings import TeeSection
from Shear_Stress import *

#Fx = 35000 #N
#Fy = 1000  #N
#l = 200
#a = 0


MaterialInput    = ReadData('StellDataBase.csv','S355')

SectionInput     = TeeSection(150,300,5,5)


BeamResult = Cantilever_LeftEndFree_RighEndFixed(Fx,Fy,l,a,MaterialInput,SectionInput)


"""
def shear(F,A):
    tau = F/A

def Stress(M,y,I):
    Sigma = -(M*y)/I
"""




Sigma = Stress(BeamResult[0][1],BeamResult[1][1],SectionInput)
Tau   = shear(BeamResult[0][0],BeamResult[1][0],SectionInput)




VonMisses(Sigma[0],Tau[0])
VonMisses(Sigma[1],Tau[1])


#shear(W,SectionInput)
