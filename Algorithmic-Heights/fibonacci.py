#########################################################
#							#
# Author: Dlambros					#
# Date: Mon, Dec 29, 2014				#
#							#
# Given: A positive integer n <= 25			#
#							#
# Return: The value of F(n)				#
#							#
#########################################################

with open('rosalind_fibo.txt','r') as f:
	num = int(f.readline().strip())
	f.close()
i = 0
fib = []
print num
while (i <= num):
	if i == 0:
		fib.append(0)
	elif i == 1:
		fib.append(1)
	else:
		fib.append(fib[i-1] + fib[i-2])
	i += 1  
print fib[num]	
