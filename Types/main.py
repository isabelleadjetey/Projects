num : int = 2  
num_f : float =  2.8
num_str : str = "2.8"
boolean : bool = False
print(type(num))
print(type(num_f))
print(type(num_f))
print(type(boolean))

#Come viene compilato un programma python
import sys

a : int = 500
print(id(a))

b : int = a
print (sys.getrefcount(500))
#indagare perche porta  5
