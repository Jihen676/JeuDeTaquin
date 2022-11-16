import numpy as np
from numpy import zeros
from self import self


class taquin :
    def init(self):
        n = int(input("donner taille de la matrice carrée :\n"))
        M= zeros((n, n), int)
        for i in range(n):
            for j in range(n):
                if (i==n-1) and (j==n-1) :
                    break
                x= np.random.randint((n*n)+1)
                while x in M :
                    x = np.random.randint((n*n)+1)
                M[i][j]=x
        return M

    def initMB(self):
        M = zeros((n, n), int)
        k=0
        for i in range(n):
            for j in range(n):
                M[i][j]=k
                k+=1
        return M

    def admissible(mat, n, sens):
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    if sens == "B" and i == n - 1:
                        return False
                    elif sens == "H" and i == 0:
                        return False
                    elif sens == "D" and j == n - 1:
                        return False
                    elif sens == "G" and j == 0:
                        return False
                    else:
                        return True

    def action(mat,n,sens):
        for i in range (n) :
            for j in range (n):
                if mat[i][j] ==0:
                    if(sens=="B")and taquin.admissible(mat,n,sens):
                         mat[i][j] = mat[i+1][j]
                         mat[i+1][j]=0
                    elif(sens=="H")and taquin.admissible(mat,n,sens):
                        mat[i][j] = mat[i-1][j]
                        mat[i-1][j]=0
                    elif (sens == "D")and taquin.admissible(mat,n,sens):
                        mat[i][j] = mat[i][j+1]
                        mat[i][j+1] = 0
                    elif(sens=="G")and taquin.admissible(mat,n,sens):
                         mat[i][j] = mat[i][j-1]
                         mat[i][j-1]=0
                    break
        return mat

    def successeur(mat,n):
        l=[]
        if(taquin.admissible(mat,n,"B")):
            m=mat.copy()
            l.append(taquin.action(m,n,"B"))
        if(taquin.admissible(mat,n,"H")):
            m=mat.copy()
            l.append(taquin.action(m,n,"H"))
        if(taquin.admissible(mat,n,"D")):
            m = mat.copy()
            l.append(taquin.action(m,n,"D"))
        if(taquin.admissible(mat,n,"G")):
            m=mat.copy()
            l.append(taquin.action(m,n,"G"))
        return l

    

   

Mat=taquin.init(self)
print(Mat)
n=len(Mat)
print()
print("taquin.action(Mat,n,'H')\n",taquin.action(Mat,n,"H"))
print("taquin.action(Mat,n,'G')\n",taquin.action(Mat,n,"G"))
print("****successeur****")
for i in taquin.successeur(Mat,n):
    print(i,"\n")
MatBut=taquin.initMB(self)
print("Matrice But \n",MatBut)
taquin.heuristic(Mat,MatBut,n)