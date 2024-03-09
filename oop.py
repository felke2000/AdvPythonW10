
class Point2d:
	def __init__(self,name="A",x=0,y=0):
		self.name=name
		self.x=x
		self.y=y
	def coincides(self,otherPoint):
		return self.x==otherPoint.x and self.y==otherPoint.y
	def kiir(self):
		print("Coordinates of the point ",self.name," are ",self.x,self.y)
	def bisector(self):
		return self.x==self.y
		"""
		if self.x==self.y:
			return True
		else:
			return False
		"""

class Point3D(Point2d):
	def __init__(self,name='A',x=0,y=0,z=0):
		super().__init__(name,x,y)
		self.z=z
	def kiir(self):
		print(" ermflk ",self.name,self.x,self.y,self.z)

	def print_super(self):
		super().kiir()

	def projection(self):
		return Point2d(self.name,self.x,self.y)

	def proj_coincides(self,otherPoint):
		proj1=self.projection()
		proj2=otherPoint.projection()
		return proj1.coincides(proj2)







A=Point2d()
B=Point2d("B",1.5,-4)
print(A.coincides(B))
print(B.coincides(A))
#print(A.x)
#print(B.y)
A.kiir()
B.kiir()
print(A.bisector(),B.bisector())

Z=Point3D("Z",1,2,3)
Z.kiir()
Z.print_super()
print(Z.projection().bisector())
Z.projection().kiir()

A=Point3D("A",1,1,0)
B=Point3D("B",1,1,-1000)
print(A.proj_coincides(B))
