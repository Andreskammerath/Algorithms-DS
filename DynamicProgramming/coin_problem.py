"""
Problem statement:
Given a list of N coins, their values (V1, V2, … , VN), and the total
sum S. Find the minimum number of coins the sum of which is S (we can
use as many coins of one type as we want), or report that it’s not 
possible to select coins in such a way that they sum up to S.
"""

S = int(input())

#string with values of coins
l = input().split() # "v1 v2 v3"
l = [int(i) for i in l]
l.sort()

# we create our memo matrix
m = [[0 for i in range(S+1)] for j in range(len(l)+1)]

# let's initialize first row with +inf(10000)
for i in range(1,S+1):
	m[0][i] = 10000

# we fill the memo matrix 
for j in range(1,len(l)+1):
	for i in range(1,S+1):
		if i >= l[j-1]:
			m[j][i] = min(m[j-1][i], i//l[j-1] + m[j][i%l[j-1]])
		else:
			m[j][i] = m[j-1][i]

# We print the solution
print(m[len(l)][S])

