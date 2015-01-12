###################################################
# Author: Dlambros				  #
# Date: Sun, Dec 28, 2014			  #
#						  #
# Given: A file containing at most 1000 lines.    #
#						  #
# Return: A file containing all the even-numbered #
#	  lines from the original file. Assume 	  #
#	  1-based numbering of lines.		  #
#						  #
###################################################

with open('rosalind_ini5.txt','r') as f:
	foo = open('result.txt','w')
	lines = f.readlines()
	for i in range(0, len(lines)):
		if i%2 == 1:
			foo.write(lines[i])
	foo.close()
	f.close()
