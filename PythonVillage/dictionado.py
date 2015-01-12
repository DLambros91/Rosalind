#########################################################
# Author: Dlambros					#
# Date: Sun, Dec 28, 2014				#
#							#
# Given: A string s of length at most 10000 letters.	#
#							#
# Return: How many times any word occurred in string.	#
#         Each letter case (upper or lower) in word 	#
#         matters. Lines in output can be in any order.	#
#							#
#########################################################
dic = dict()
with open('rosalind_ini6.txt', 'r') as f:
	s = f.readline().strip()
	f.close()
print s
for word in s.split(' '):
	if dic.has_key(word):
		dic[word] +=1
	else:
		if word != ' ':
			print word
			dic.update({word:1})
for key, value in dic.items():
	print key + ' ' + str(value)
