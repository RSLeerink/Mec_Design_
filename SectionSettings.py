
#ToDo
#Add units in the text output

def TeeSection(b,d,t,t_w):
    #Area
    A = t*b + t_w*d

    #distance to extreme fiber
    y_c = ( (b*t**2) + (t_w * d * (2*t + d)) ) / (2*A)
    x_c = b/2

    I_x = (b/3) * (d+t)**3 - ((d**3)/3)*(b-t_w)-A*(d+t-y_c)**2
    I_y = ( (t*b**3) / 12 ) + ( (d*t_w**3) / 12)
    
    name = ['A  ','y_c','x_c','I_x','I_y']
    count = 0

    print()
    print('-- Section data ------' )
    print('----- Tee Section ----' )
    for i in [A,y_c,x_c,I_x,I_y]:
        print(name[count]+ ' ' + str(round(i,2)) )
        count += 1
    
    print()
    
    #Output
    # 0 - A
    # 1 - y_c
    # 2 - x_c
    # 3 - I_x
    # 4 - I_y

    return A,y_c,x_c,I_x,I_y

TeeSection(100,100,5,5)