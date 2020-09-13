from numpy import sqrt

#WIP!

def shear(Fx,Fy,SectionInput):

    
    A = SectionInput[0]

    tau_x = Fx/A
    tau_y = Fy/A

    print('Tau x ' + str( tau_x))
    print('Tau_y ' + str( tau_y))

    return tau_x,tau_y


def Stress(Mx,My,SectionInput):


    Ix  = SectionInput[3]
    Iy  = SectionInput[4]
    y_c = SectionInput[1]
    x_c = SectionInput[2]

    Sigma_x = -(Mx*y_c)/Ix
    Sigma_y = -(My*x_c)/Iy

    print('Sigma_x ' + str(Sigma_x))
    print('Sigma_y ' + str(Sigma_y))

    return Sigma_x,Sigma_y

def VonMisses(Sigma,Tau):
    
    VM = sqrt(Sigma**2 +( 3*Tau**2))

    print('VonMisses ' + str(VM))

    return VM
