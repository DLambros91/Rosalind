########################################################
# Author: Dlambros 				                             #
# Date: Sun, Dec 28, 2014			                         #
# 						                                         #
# Given: Two positive integers a and b (a < b < 10000) #
#						                                           #
# Return: The sum of all odd integers from a through b,#
#	        inclusively.	                               #
#						                                           #
########################################################

sum = 0
with open('rosalind_ini4.txt', 'r') as f:
	a,b = map(int,f.readline().split())
	f.close()
while (a < b):
	if a%2 == 1:
		sum = sum + a
	a += 1

print sum
