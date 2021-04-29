## @package python_problem
#
# This package performs misc operations.

from sys import argv
from copy import deepcopy

## Produces list of numbers present in the file 
#
# @param filename Name of the file which needs to be read
# @return List of numbers
#
# Read the file where each line is a number. Parse the integer,
# and insert the number into the list.
#
def make(filename):
	file = open (filename)
	l=[]
	for line in file:
		a=int(line)
		l.append(a)
	return l

## Sorts the numbers
#
# @param l List which contains the numbers for input
# @return Sorted list of numbers
#
# Sorts the numbers using bubble sort, which is a common sorting algorithm.
#
def fun1(l):	
	size=len(l)
	for i in range(0,size-1):
		for j in range(0,size-i-1):
			if l[j] > l[j+1]:
				temp=l[j]
				l[j]=l[j+1]
				l[j+1]=temp
			
	return l

## Binary Search
#
# @param l Sorted list of numbers
# @param x Number to be searched
# @return Number of probes it took to find the number
#
# A simple binary search implemenetation. Returns -1 if
# the number is not present in the list.
#
def fun2(l,x):
	n=int(x)
	probes=0
	s=0
	e=len(l)-1
	flag=0
	while(s<=e):
		probes=probes+1
		m=(s+e)//2
		print ("Probe "+str(probes)+":",m,l[m])
		if(l[m]==n):
			flag=1
			break
		elif(l[m]>n):
			e=m-1
		elif(l[m]<n):
			s=m+1
	if(flag==1):
		return probes
	else:	
		return -1

## Calculates determinant
#
# @param L Matrix whose determinant needs to be found
# @return Determinant of L i.e. |L|
# 
# Recursively finds the determinant of matrix.
#
def fun3(L):
	d=0
	n=len(L)
	if(n==1):
		return L[0][0]
	for i in range(0,n):
		A=deepcopy(L)
		for j in range(0,len(A)):
			A[j].pop(i)
		A.pop(0)
		d=d+L[0][i]*((-1)**i)*fun3(A)
	return d


L = make("data")
print (L)
L = fun1(L)
print ("\nAfter Fun1:")
print (L)
print ("\nFun2 Starts:")
ans = fun2(L, 48)
print ("Result of Fun2:", ans)

print ("\n")
# Change the elements and observe the result  
L = [[1, 2, 3], [100, 54, 23], [9, 27, 11]]
print(L)
ans = fun3(L)
print ("Result of Fun3:", ans)
