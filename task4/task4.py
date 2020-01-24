class Timestamp:

	def __init__(self, time_str):

		splt = [int(i) for i in time_str.split(":")]

		if splt[0] < 0 or splt[0] > 23 or splt[1] < 0 or splt[1] > 59 or len(splt) != 2:
			raise TypeError("Illegal time format - HH:MM (24H) supported only")

		self.hour = splt[0]
		self.minute = splt[1]

	def to_min(self):
		return self.hour * 60 + self.minute

	def __le__(self, other):
		return self.to_min() <= other.to_min()

	def __lt__(self, other):
		return self.to_min() < other.to_min()

	def __ge__(self, other):
		return self.to_min() >= other.to_min()

	def __gt__(self, other):
		return self.to_min() > other.to_min()

	def __eq__(self, other):
		return self.to_min() == other.to_min()

	def __str__(self):
		str_min = str(self.minute)

		if len(str_min) == 1:
			str_min = "0" + str_min 

		return str(self.hour) + ":" + str_min

	# def plusMinute(self, mins=1):
	# 	minute = self.minute + mins

	# 	if minute > 59:
	# 		self = self.plusHour()
	# 		minute %= 60

	# 	return Timestamp(str(self.hour) + ":" + str(minute))

	# def plusHour(self, hours=1):
	# 	hour = self.hour + hours

	# 	if hour > 23:
	# 		hour %= 24

	# 	return Timestamp(str(hour) + ":" + str(self.minute))


	@staticmethod
	def listOf(*time_strs):
		return [Timestamp(ts) for ts in time_strs]


class Interval:

	def __init__(self, lower, upper):
		bounds = sorted([lower, upper])
		self.lower = bounds[0]
		self.upper = bounds[1]

		self.weight = 1


	# def union(self, other):
	# 	l_bounds = sorted([self.lower, other.lower])
	# 	u_bounds = sorted([self.upper, other.upper])

	# 	return Interval(l_bounds[0], u_bounds[1]).with_weight(self.weight + other.weight)

	def intersection(self, other):
		l_bounds = sorted([self.lower, other.lower])
		u_bounds = sorted([self.upper, other.upper])

		return Interval(l_bounds[1], u_bounds[0]).with_weight(self.weight + other.weight)


	def do_cross(self, other):
		l_bounds = sorted([self.lower, other.lower])
		u_bounds = sorted([self.upper, other.upper])

		return u_bounds[0] >= l_bounds[1]


	def with_weight(self, n):
		self.weight = n
		return self


	def __str__(self):
		return str(self.lower) + " - " + str(self.upper)


	def to_min(self):
		return self.upper.to_min() - self.lower.to_min()


	@staticmethod
	def fromString(string):
		lower, upper = string.split(" ")
		return Interval(Timestamp(lower), Timestamp(upper))


def main(file):

	rf = open(file, 'r').read().split("\n")
	print(rf)
	input_intervals = [Interval.fromString(i) for i in rf]

	overall = []

	max_val = 1

	acc_int = input_intervals[0]

	for interval in input_intervals[1:]:

		if acc_int.do_cross(interval):
			acc_int = acc_int.intersection(interval)

			if acc_int.weight == max_val:
				overall.append(acc_int)

			if acc_int.weight > max_val:
				max_val = acc_int.weight

				overall = [acc_int]

		else:
			acc_int = interval
			continue

	for i in overall:
		print(i.weight)


def main2(file):

	rf = open(file, 'r').read().split("\n")

	




if __name__ == "__main__":
	import sys
	main(sys.argv[1])











