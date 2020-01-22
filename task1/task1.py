array = [5, 8, 0 ,0, 1, 5, 5, 5, 10, 6]

def sum(arr):
	acc = 0
	for i in arr:
		acc += i
	return acc

def med(arr):
	arr = sorted(arr)
	l = len(arr)

	if l % 2 != 0:
		return arr[l / 2 + 1]
	return (arr[l / 2] + arr[l / 2 + 1]) / 2.0


def maximum(arr):
	arr = sorted(arr)
	return arr[-1]


def minimum(arr):
	arr = sorted(arr)
	return arr[0]


def avg(arr):
	return sum(arr) / float(len(arr))


def percentile(p, arr):
	from math import modf
	l = len(arr)
	arr = sorted(arr)
	rem, quot = modf(float(p) / 100 * (l - 1) + 1)
	i = int(quot)
	try:
		return arr[i] + rem * (arr[i + 1] - arr[i]) 
	except IndexError:
		return arr[i] + rem 

def percentile90(arr):
	return percentile(90, arr)


def out(arg, *funcs):
	for f in funcs:
		print(f.__name__, f(arg))

out(array,
	percentile90,
	med,
	maximum,
	minimum,
	avg
	)


