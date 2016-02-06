#Helper function to simplify fractions to simplest form
#Not foolproof: doesn't work for simplyfing primes past 19.
#See Euclid's Algorithm for a foolproof algorithm.
# def simplify(frac):
# 	if ((frac.num%2 == 0) and (frac.denom%2 == 0)):
# 		frac.num = frac.num/2
# 		frac.denom = frac.denom/2
# 		simplify(frac)
# 	elif ((frac.num%3 == 0) and (frac.denom%3 == 0)):
# 		frac.num = frac.num/3
# 		frac.denom = frac.denom/3
# 		simplify(frac)
# 	elif ((frac.num%5 == 0) and (frac.denom%5 == 0)):
# 		frac.num = frac.num/5
# 		frac.denom = frac.denom/5
# 		simplify(frac)
# 	elif ((frac.num%7 == 0) and (frac.denom%7 == 0)):
# 		frac.num = frac.num/7
# 		frac.denom = frac.denom/7
# 		simplify(frac)
# 	elif ((frac.num%11 == 0) and (frac.denom%11 == 0)):
# 		frac.num = frac.num/11
# 		frac.denom = frac.denom/11
# 		simplify(frac)
# 	elif ((frac.num%13 == 0) and (frac.denom%13 == 0)):
# 		frac.num = frac.num/13
# 		frac.denom = frac.denom/13
# 		simplify(frac)
# 	elif ((frac.num%17 == 0) and (frac.denom%17 == 0)):
# 		frac.num = frac.num/17
# 		frac.denom = frac.denom/17
# 		simplify(frac)
# 	elif ((frac.num%19 == 0) and (frac.denom%19 == 0)):
# 		frac.num = frac.num/19
# 		frac.denom = frac.denom/19
# 		simplify(frac)

def simplify(frac):
	divisor = gcd(frac.getNum(),frac.getDen())
	frac.changeNum(frac.getNum()/divisor)
	frac.changeDen(frac.getDen()/divisor)

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

# print(gcd(20,10))

class Fraction:
	#Initializing the fraction
	def __init__(self,top,bottom):
		if (bottom == 0):
			raise ValueError('Denominator cannot be 0.')
		if ((type(top) != int) or (type(bottom) != int)):
			raise ValueError('Numerator and denominator must be integers.')
		if bottom<0:
			self.num = top*-1
			self.denom = bottom*-1 
		else:
			self.num = top
			self.denom = bottom
		simplify(self)
	#Print (print)
	def __str__(self):
		return str(self.num) + '/' + str(self.denom)
	#Get the numerator
	def getNum(self):
		return self.num
	#Get the denominator
	def getDen(self):
		return self.denom
	def changeNum(self,n):
		self.num = n
	def changeDen(self,n):
		self.denom = n
	#Multiplication (*)
	def __mul__(self,f2):
		if type(f2) != int:
			newnum = self.num * f2.num
			newden = self.denom * f2.denom
			newfrac = Fraction(newnum,newden)
			simplify(newfrac)
			return newfrac
		else:
			newnum = self.num * f2
			newfrac = Fraction(newnum,self.denom)
			simplify(newfrac)
			return newfrac
	#Equality (==)
	def __eq__(self,f2):
		if ((self.num == f2.num) and (self.denom == f2.denom)):
			return True
		else:
			return False
	def __ne__(self,f2):
		if ((self.num != f2.num) or (self.denom != f2.denom)):
			return True
		else:
			return True
	#Addition (+)
	def __add__(self,f2):
		newnum = self.num * f2.denom
		newden = self.denom * f2.denom
		addnum = f2.num * self.denom
		addden = f2.denom * self.denom
		newnum = newnum + addnum
		newfrac = Fraction(newnum,newden)
		simplify(newfrac)
		return newfrac
	#Division (//)
	def __div__(self,f2):
		newnum = f2.denom
		newden = f2.num
		return self*Fraction(newnum,newden)
	#Subtraction (-)
	def __sub__(self,f2):
		newnum = self.num * f2.denom
		newden = self.denom * f2.denom
		subnum = f2.num * self.denom
		subden = f2.denom * self.denom
		newnum = newnum - subnum
		newfrac = Fraction(newnum,newden)
		simplify(newfrac)
		return newfrac
	#Less than or equal to (<=)
	def __le__(self,f2):
		diff = self - f2
		if (diff.num <= 0):
			return True
		else:
			return False
	#Less than (<)
	def __lt__(self,f2):
		diff = self - f2
		if (diff.num < 0):
			return True
		else:
			return False
	#Greater than (>)
	def __gt__(self,f2):
		diff = self - f2
		if (diff.num > 0):
			return True
		else:
			return False
	#Greater than or equal to (>=)
	def __ge__(self,f2):
		diff = self - f2
		if (diff.num >= 0):
			return True
		else:
			return False

# f = Fraction(11,18)
# print f
# print (f*2)
# g = Fraction(6,9)
# print g
# print f==g
# print f+g
# print f*g
# print f/g
# print f-g
# print f<=g
# print f<g
# print f>g
# print f>=g
# print type(f)
# print type(4)
# a = 4
# print type(a) == int 

f = Fraction(-3,4)
print f


# f = Fraction(1,3)
# print f
# g = Fraction(5,9)
# print g
# print (f*g)
# print (f+g)
# print (f-g)