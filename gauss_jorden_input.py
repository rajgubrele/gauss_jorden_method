
#Input file contains Matrix a and Matrix b which created from linear equations. 
#Input file import the code from module file and gives you 'gauss_jordan.out.txt'file as output, which contains the solution. 

from gauss_jordanmethod import*
import pandas as pd

a=[[9,3,-1,1,0,2,-2],[0,12,4,1,-1,0,3],[1,-1,10,1,3,-2,2],[1, 0,0,6,2,-1,0],[5,-1,0,1,8,0,-1],[-2,0,0,1,-1,4,0],[3,1,0,-2,6,0,15]]
b=[-9,5,0,7,1,-10,2]
gssjrdn(a,b)