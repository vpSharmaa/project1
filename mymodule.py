import time  as t

x= t.ctime()
print(x)

new
def greeting(name):
	print("hello, how are you "+name )

x= "mohit kejriwal "

#mymodule.py file
new
import mymodule 

print(mymodule.x)

#usemodule.py file
new
import math 

x=math.sqrt(16)
print(int(x))

rahul
import time as t
def wish(name):
	hour=int(t.strftime("%H"))
	if hour <10:
		print("hey!",name,"good morning!")
	elif hour >10 and hour <= 15:
		print("hey!",name,"good afternoon!")
	elif hour  >15 and hour <= 20:
		print("hey!",name,"good evening!")
	elif hour >20 and hour <=24:
		print("hey!",name,"good night!")

#@a=wish("rahul")

rahul