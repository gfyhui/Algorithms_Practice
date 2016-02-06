# Load factor is the number of entries divided by the number of buckets in a hash table

def success(loadfactor):
	return .5*(1+(1/(1-loadfactor)))

def fail(loadfactor):
	return .5*(1+(1/(1-loadfactor))**2)


print success(.1)
print success(.25)
print success(.5)
print success(.75)
print success(.9)
print success(.99)


print fail(.1)
print fail(.25)
print fail(.5)
print fail(.75)
print fail(.9)
print fail(.99)