import os
import sys


def nussinov(v):
    M = [[0 for j in range(len(v)+1)] for i in range(len(v)+1)]
    # N = [[0 for j in range(len(v)+1)] for i in range(len(v)+1)]
    for j in range(len(v)):
        M[0][j+1] = v[j]
        M[j+1][0] = v[j]
        # N[0][j+1] = v[j]
        # N[j+1][0] = v[j]
    n = len(v)
    for j in range(2,n+1):
        i = 1
        while(j < n+1):
            # N[i][j] = isPair(M[i][0],M[0][j])
            M[i][j] = findScore(i,j, M, isPair(M[i][0],M[0][j]))
            j += 1
            i += 1
    for r in M:
        print (r)
    # for r in N:
    #     print (r)




def isPair(i, j): #returns boolean for if its a pair or not 
	if (i == 'A' and j == 'U'):
		return 1
	elif (i == 'C' and j == 'G'):
		return 1
	elif (i == 'U' and j == 'A'):
		return 1
	elif (i == 'G' and j == 'C'):
		return 1
	return 0


def findScore(i, j, M, pair): #takes the coordinate and calculates isPair(i,j). Finds the max between left, bottom, and diagonal if not a pair and Diagonal+1 if it is a pair and returns that
    if (pair==1):
        return M[i+1][j-1] + 1
    else:
        # return max(left, diagonal, down)
        return max(M[i][j-1], M[i+1][j-1], M[i+1][j])



if __name__ == '__main__':
    print("start")
    nussinov("GGGAAAUCC")

