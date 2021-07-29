import turtle as tt

'''set'''
bob = tt.Turtle()
bob.speed(0)
bob.pu()
bob.lt(180)
bob.fd(350)
bob.lt(90)
bob.fd(300)
bob.lt(90)
bob.pd()

'''program'''
a = 0
b = 1
c = a+b
succ_range = int(input("Range: "))
distance = int(input("Distance: "))
size = int(input("Size: "))
bob.pensize(size/2)

def Turning(lenght):
    bob.lt(90)
    bob.fd(lenght)
    bob.rt(180)
    bob.fd(lenght)
    bob.lt(90)
    bob.pu()
    bob.fd(distance)
    bob.pd()

for i in range(succ_range):
    if i == 0:
        Turning(c)
        
    else:
        Turning(c)
        c = a+b
        a = b
        b = c


    
