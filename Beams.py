#Based on table 8.17 - Roarks
#1a



"""
Test inputs
W = 35000 #N
l = 250
a = 50


MaterialInput    = ReadData('StellDataBase.csv','S355')

SectionInput     = TeeSection(300,50,5,5)
"""

def Cantilever_LeftEndFree_RighEndFixed(W,l,a,MaterialInput,SectionInput):
    #MaterialInput    = ReadData(InputFileName,MaterialName)
    #SectionInput     = TeeSection(b,d,t,t_w)

    E = MaterialInput[0]
    I_x = SectionInput[3]
    I_y = SectionInput[4]

    def Formulas(I,Id):
        Shear_A         = W
        Bendingmoment_a = -W*(l-a)
        Deflection_A    = ((-W)/6*E*I) * (2*l**3 - 3*l**2*a + a**3 )
        Slope_A         = (W*(l-a)**2) / (2*E*I)

        name  = ['Shear_A         ','Bendingmoment_a','Bendingmoment_a','Deflection_A   ','Slope_A         ']
        units = ['N', 'Nmm', 'Nm','rad','mm']
        count = 0

        print('----- Results '+str(Id)+' ----' )
        for i in [Shear_A,Bendingmoment_a,(Bendingmoment_a/1000),Deflection_A,Slope_A]:
            print(name[count]+ ' ' + str(round(i,2)) + ' ' + str(units[count]) )

            if count == 4:
                print(name[count]+ ' ' + str(round(i,5)) + ' ' + str(units[count]) )


            count += 1
            
        print()

        return Shear_A,Bendingmoment_a,Deflection_A,Slope_A

    X_axis = Formulas(I_x,'I-x')

    y_axis = Formulas(I_y,'I-y')

    return X_axis,y_axis




#Cantilever_LeftEndFree_RighEndFixed(W,l,a,MaterialInput,SectionInput)