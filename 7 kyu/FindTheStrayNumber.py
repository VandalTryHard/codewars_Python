"""7 kyu
Find the stray number
You are given an odd-length array of integers, in which all of them are the same, except for one single number.
Complete the method which accepts such an array, and returns that single different number.
The input array will always be valid! (odd-length >= 3)
Examples
[1, 1, 2] ==> 2[17, 17, 3, 17, 17, 17, 17]
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""

# def stray(arr):
#     for i in set(arr):
#         if arr.count(i) == 1:
#             return(i)

#How this works
list_ = [17, 17, 3, 17, 17, 17, 17]
for i in set(list_):
	if list_.count(i) == 1:
		print(i)