import timeit
import random

def test1():
	for i in range(10000,1000001,20000):
		t = timeit.Timer("x[random.randrange(%d)]"%i,
						"from __main__ import random,x")
		x=list(range(i))
		lst_time = t.timeit(number=1000)
		print("%d,%1.6f" %(i,lst_time))

def test2():
	for i in range(1000,1000001,20000):
		t = timeit.Timer("x[random.randrange(%d)] = 1"%i,
						"from __main__ import random,x")
		x = {j:None for j in range(i)}
		d_time = t.timeit(number = 1000)
		print ("%d,%10.9f" % (i,d_time))

def test3():
	for i in range(10000,1000001,20000):
		t = timeit.Timer("del(x[random.randrange(%d)])"%i,
						"from __main__ import random,x")
		x = list(range(1000000))
		lst_time = t.timeit()
		x = {j:None for j in range(i)}
		d_time = t.timeit()
		print("%d, %2.9f, %2.9f" % (i,lst_time,d_time))