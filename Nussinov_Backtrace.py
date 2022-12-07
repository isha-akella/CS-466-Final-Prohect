import os
import sys
 
DOWN = (1, 0)
LEFT = (0, -1)
DIAG = (1, -1)
ORIGIN = (0, 0)
 
# Overall function, accepts an RNA sequence and outputs
# dynamic programming table showing max number of base pairs, 
# and base pairing corresponding to backtrace
def nussinov(v):
   # M: Dynamic programming table  
   M = [[0 for j in range(len(v)+1)] for i in range(len(v)+1)]
   # P: Table of backpointers for each space in M
   P = [[ORIGIN for j in range(len(v)+1)] for i in range(len(v)+1)]
   for j in range(len(v)):
       M[0][j+1] = v[j]
       M[j+1][0] = v[j]
   n = len(v)
   for j in range(2,n+1):
       i = 1
       while(j < n+1):
           M[i][j] = findScore(i,j, M, P, isPair(M[i][0],M[0][j]))
           j += 1
           i += 1
   print(backtrace(v, P, 1, len(v)))
   for r in M:
       print (r)
 

# Input = in two values in the dynamic programming table
# Output = 1 if the two nucleotides are a base pairing and 0 if not
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
 

# Takes the coordinate and calculates isPair(i,j). 
# Finds the max between left, bottom, and diagonal if not a pair and Diagonal+1 
# if it is a pair and returns that 
def findScore(i, j, M, P, pair): 
   # Cases of the recurrence to compare and find the maximum 
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
    
    
   # Update P accordingly based on the maximum recurrence case 
   if (m == down):
       P[i][j] = DOWN
   elif (m == left):
       P[i][j] = LEFT
   elif (m == diag_p or m == diag):
       P[i][j] = DIAG
   else:
       P[i][j] = ((i,k - 1),(k,j))
   return m
 
# Accepts v: the RNA string, P: the table of backpointers, i: the start index and j: the
# stop index. Returns w, a string of '()' and '-' characters that shows the base pair matching
# of v. 
def backtrace(v, P, i, j): 
   w = ["-" for x in range(len(v))]
   while True:
      # if i >= to j, the diagonal has been reached and the backtrace is concluded
      if (i >= j):
          break
      # values to increment i and j by
      di, dj = P[i][j]
      # update base pairing string w based on back pointer
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
          # for bifurcation case, use recursion to find base pairings for each 
          # bifurcated section of v.
          w[di[0]-1:di[1]] = backtrace(v, P, di[0], di[1])[di[0]-1:di[1]]
          w[dj[0]-1:dj[1]] = backtrace(v, P, dj[0], dj[1])[dj[0]-1:dj[1]]
          if (isPair(v[di[1] - 1], v[dj[0] - 1]) and w[di[1] - 1] == "-" and w[dj[0] - 1] == "-"):
             w[di[1] - 1] = "("
             w[dj[0] - 1] = ")"
          break
      # update values of i and j
      i, j = i + di, j + dj
   return w
 
 
if __name__ == '__main__':
   # nussinov("AUGCGCGGGAUCGUCGAGAU")
   nussinov('GGGCCCATAGCTCAGTGGTAGAGTGCCTCCTTTGCAAGGAGGATGCCCTGGGTTCGAATCCCAGTGGGTCCA')
   # nussinov("GGGAAAUCC")
   # nussinov("GCUCGGGUUCCCUAUUCAAGAGC")
