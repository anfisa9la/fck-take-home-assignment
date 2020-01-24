class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	@staticmethod
	def points(*args):
		return [Point(p[0], p[1]) for p in args]

class Line:

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def getValueEq(self, P):
		x1, x2, y1, y2 = self.p1.getX(), self.p2.getX(), self.p1.getY(), self.p2.getY()
		return (y1 - y2) * P.getX() +(x2 - x1) * P.getY() + x1*y2 - x2*y1 

	def spaceAboveIncludes(self, P):
		return self.getValueEq(P) > 0

	def spaceBelowIncludes(self, P):
		return self.getValueEq(P) < 0

	def onLineLies(self, P):
		return self.getValueEq(P) == 0  


class Rect:

	def __init__(self, *args):
		self.a, self.b, self.c, self.d = Point.points(*args)

	def calc(self, P):
		a, b, c, d = self.a, self.b, self.c, self.d
		AB, BC, CD, DA = Line(a, b), Line(b, c), Line(c, d), Line(d, a)

		if AB.spaceAboveIncludes(P):
			if BC.spaceBelowIncludes(P):
				return  


rect = Rect((0.0, 0.0), (0.0, 4.0), (6.0, 4.0), (6.0, 0.0))

a = Point(0.0,0.0)
b = Point(1.0,1.0)

print(rect.calc(Point(0.1, 3.9)))

	   
