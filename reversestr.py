# initializing string
test_string = "geekforgeeks"
# printing original string
print("The original string : " + str(test_string))
# using join() + sorted() + reverse
# Sorting a string
res = ''.join(sorted(test_string, reverse=True))
# print result
print("String after reverse sorting : " + str(res))
