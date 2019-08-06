
double =lambda x: x*2
print(double(1))

#tkinter
#linextraningacadamy


ml=[1,2,3,4,5,6]

nl=list(filter(lambda x:(x%2==0),ml))
print (nl)

def mul(x):
	return (x*x)

def add(x):
	return (x+x)

funl=[mul,add]

nl=list(map(lambda x: x(3),funl))
print (nl)




'''funcs = [multiply, add]
value = list(map(lambda x: x), funcs)
print(value)'''