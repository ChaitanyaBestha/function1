def sum(a):
	total=0
	for element in a:
		if type(element)==type([]):
			total=total+sum(element)
		else:
			total=total+element

	return total
print( sum([1, 2, [3,4],[5,6]]))