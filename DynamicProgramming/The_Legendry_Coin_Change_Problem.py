"""
Problem statement:
link to problem: https://www.codechef.com/problems/CTY2
"""

S, a = input().split(" ")
S = int(S) 
#string with values of coins
l = input().split() # "v1 v2 v3"
l = [int(i) for i in l]
l.sort()

# we create our memo matrix
m = [[0 for i in range(S+1)] for j in range(len(l))]

# let's initialize first row with +inf(10000)
for i in range(1,S+1):
	if i %l[0] == 0:
		m[0][i] = 1

# we fill the memo matrix 
for j in range(1,len(l)):
	for i in range(1,S+1):
		if i > l[j]:
			m[j][i] = m[j-1][i] + m[j][i-l[j]]
		elif i == l[j]:
			m[j][i] = m[j-1][i] + 1
		else:
			m[j][i] = m[j-1][i]

# We print the solution
print(m[len(l)-1][S])

