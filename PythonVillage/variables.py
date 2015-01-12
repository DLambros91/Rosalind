#########################################################
# Author: Dlambros #
# Date: Sun, Dec 28, 2014 #
# #
# Given: Two positive integers a and b, each less than 1000. #
# #
# Return: The integer corresponding to the square of the  #
#         hypotenuse of the right triangle whose legs have #
#         lengths a and b.    #
# #
#########################################################

sides = []
with open('rosalind_ini2.txt', 'r') as f:
	for line in f:
		for word in line.split():
			sides.append(int(word))
hyp = sides[1]**2 + sides[0]**2
print hyp
print sides
