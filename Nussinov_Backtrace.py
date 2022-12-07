import os
import sys
 
DOWN = (1, 0)
LEFT = (0, -1)
DIAG = (1, -1)
ORIGIN = (0, 0)
 
def nussinov(v):
   M = [[0 for j in range(len(v)+1)] for i in range(len(v)+1)]
   P = [[ORIGIN for j in range(len(v)+1)] for i in range(len(v)+1)]
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
           M[i][j] = findScore(i,j, M, P, isPair(M[i][0],M[0][j]))
           j += 1
           i += 1
   print(backtrace(v, P, 1, len(v)))
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
 
 
def findScore(i, j, M, P, pair): #takes the coordinate and calculates isPair(i,j). Finds the max between left, bottom, and diagonal if not a pair and Diagonal+1 if it is a pair and returns that
   left = M[i][j-1]
   diag = M[i+1][j-1]
   diag_p = M[i+1][j-1] + 1
   down = M[i+1][j]
   bifurc = -1
   k = -1
   m = -1
   for x in range(i, j):
       if (M[i][x] + M[x + 1][j] >= bifurc):
           bifurc = M[i][x] + M[x + 1][j]
           k = x
   if (pair==1):
       m = max(diag_p, down, left, bifurc)
   else:
       m = max(diag, down, left, bifurc)
 
   if (m == down):
       P[i][j] = DOWN
   elif (m == left):
       P[i][j] = LEFT
   elif (m == diag_p or m == diag):
       P[i][j] = DIAG
   else:
       P[i][j] = ((i,k - 1),(k,j))
   return m
 
 
def backtrace(v, P, i, j):
   w = ["-" for x in range(len(v))]
   while True:
      di, dj = P[i][j]
      if (di,dj) == LEFT:
          w[j-1] = "-"
      elif (di,dj) == DOWN:
          w[i-1] = "-"
      elif (di,dj) == DIAG:
          if (isPair(v[i-1], v[j-1])):
             w[i-1] = "("
             w[j-1] = ")"
          else:
             w[i-1] = "-"
             w[j-1] = "-"
      else:
          w[di[0]-1:di[1]] = backtrace(v, P, di[0], di[1])[di[0]-1:di[1]]
          w[dj[0]-1:dj[1]] = backtrace(v, P, dj[0], dj[1])[dj[0]-1:dj[1]]
          if (isPair(v[di[1] - 1], v[dj[0] - 1]) and w[di[1] - 1] == "-" and w[dj[0] - 1] == "-"):
             w[di[1] - 1] = "("
             w[dj[0] - 1] = ")"
          break
      i, j = i + di, j + dj
      if (i >= j):
          break
   return w
 
 
if __name__ == '__main__':
   print("start")
   nussinov("AUGCGCGGGAUCGUCGAGAU")
   nussinov("GGGAAAUCC")
   nussinov("GCUCGGGUUCCCUAUUCAAGAGC")
