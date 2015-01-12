##############################################################
# Author: Dlambros                                           #
# Date: Sun, Dec 28, 2014                                    #
#                                                            #
# Given: A string s of length at most 200 letters and four   #
#        integers a, b, c and d.                             #
#                                                            #
# Return: The slice of this string from indices a through b  #
#         and c through d (with space in between),           # 
#         inclusively.                                       #
#                                                            #
##############################################################


abcd = []

with open('rosalind_ini3.txt', 'r') as f:
	s = f.readline()
	for word in f.readline().split():
        	abcd.append(int(word))
	f.close()

print s[abcd[0]:abcd[1]+1] + ' ' + s[abcd[2]:abcd[3]+1]
