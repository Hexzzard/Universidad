import numpy as np

def MD(m, new):
    sol = 100 #max value
    C = 0 #clase
    for i in m:
        Cx = np.sum(i[:, 0]) / (i.shape[0])
        Cy = np.sum(i[:, 1]) / (i.shape[0])

        Vx = 0
        Vy = 0
        Cxy= 0
        for j in i[:, 0]:
            Vx += ((j - Cx)**2)/(i.shape[0]-1)
        for j in i[:, 1]:
            Vy += ((j - Cy)**2)/(i.shape[0]-1)
        for j in i:
            Cxy += ( (j[0] - Cx) * (j[1] - Cy) )/(i.shape[0]-1)

        Mcov = np.array([[Vx,Cxy],[Cxy,Vy]])
        V = np.array([[new[0]-Cx],[new[1]-Cy]])

        MD = np.sqrt(np.dot(np.dot(np.transpose(V),np.linalg.inv(Mcov)),V))
        if (sol > MD):
            sol = MD
        C +=1
    return C,


m = np.array([[[33,42],[29,57],[39,38],[40,43],[45,30],[39,58]],[[67,61],[60,70],[62,55],[75,74],[55,56],[70,72]]])
new = np.array([49,49])

print(MD(m,new))
#return 2, 
#cluster 1: 2.99  , cluster 2: 2.24   se elige el menor