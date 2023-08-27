import math


class NDimensional:
    def __init__(self, *more ):
        self.more = more
class Vector2d(NDimensional):
    def __init__(self,x1=float, y1=float,*more):
        self.x1 = x1
        self.y1 = y1
        self.more = more

    def __add__(self,other):
        match other:
            case Vector2d():
                return Vector2d(self.x1+ other.x1 , self.y1+other.y1)
            case 1:
                raise ValueError()

    def __sub__(self,other):
        match other:
            case Vector2d():
                return Vector2d(self.x1 - other.x1, self.y1 - other.y1)

    def __mul__(self, other):
        match other:
            case Vector2d():
                return Vector2d(self.x1 * other.x1, self.y1 * other.y1)

    def __len__(self):
        return 2

    def __matmul__(self, other):
        match other:
            case Vector2d():
                return Vector2d((self.x1 * other.x1) + (self.y1 * other.y1))

    def __truediv__(self, other):
        match other:
            case Vector2d():
                return  ValueError()

    def __repr__(self):
        return f"Vector2d({self.x1}, {self.y1})"



v1=Vector2d(1, 1)
v2=Vector2d(2,1)

a=v1+v2
b=v1-v2
c=v1*v2
d=v1.x1 * v2.x1 +v1.y1 * v2.y1
e=len(v1)

print("add: ",a)
print("sub: ",b)
print("matmul: ",c)
print("truediv: ",d)
print("len: ",e)

vectors:list[Vector2d]=[a,b,c,]
print(vectors)

def myFunc(vector:Vector2d):
  length = math.sqrt(vector.x1**2+vector.y1**2)
  # print("length is:", length)
  if length < 2:
    return True
  else:
    # print("more than 2")
    return False


filtering = list(filter(myFunc, vectors))
print(filtering)

# for x in filtering:
#   print("less than 2:",x)




