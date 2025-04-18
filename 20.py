# ARRAY COPYING BASED QUESTIONS.
# ensure that the destination array sizes are properly taken as per the rquirement.
# dont take extra cells in the destination array.
#
# 1. take an list1 of 10 numbers.
# take an empty list2.
# write for loop logic to copy list1 elements into list2.


list1 = [3,23.45,456,.345,5,2,5,76,34,35,46,64,436]
list2 = []

for i in list1:
    list2.append(i)
print(list2)