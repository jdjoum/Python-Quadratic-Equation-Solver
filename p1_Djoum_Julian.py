import pylab
import math

while True :
    print("Quadratic Equation Solver")
    try:
        a = float(input("Please enter the value for the coefficient a: "))
    except:
        print("\nYou chose to EXIT the Quadratic Equation Solver.")
        break
    b = float(input("Please enter the value for the coefficient b: "))
    c = float(input("Please enter the value for the coefficient c: "))
    quadEq = (b**2)-4*a*c
    if(quadEq < 0):
        print("\nNo Real Solutions.")
        
        xs = []
        ys = []
        xLeft = -4
        xRight = 4
        n = 150
        dx = (xRight - xLeft) / n
        x = xLeft
        while(x <= xRight):
            xs.append(x)
            y = -b / (2*a)
            ys.append(y)
            x += dx
        pylab.title("Quadratic Equation Graph (No Solutions)")
        pylab.plot(xs, ys, "ro-")
        pylab.show()
        break
    elif(quadEq == 0):
        x1 = (-b + math.sqrt(quadEq)) / (2*a)
        print("\nOne Solution: ", x1)
        
        xs = []
        ys = []
        xLeft = x1 - 4
        xRight = x1 + 4
        n = 150
        dx = (xRight - xLeft) / n
        x = xLeft
        while(x <= xRight):
            xs.append(x)
            y = a*(x**2) + b*x + c
            ys.append(y)
            x += dx
        pylab.title("Quadratic Equation Graph (One Solution)")
        pylab.plot(xs, ys, "ro-")
        pylab.show()
        break
    elif(quadEq > 0):
        x1 = (-b + math.sqrt(quadEq)) / (2*a)
        x2 = (-b - math.sqrt(quadEq)) / (2*a)
        print("\nTwo Solutions: ", x1, x2)
        
        xs = []
        ys = []
        xLeft = x2 - 4
        xRight = x1 + 4
        n = 150
        dx = (xRight - xLeft) / n
        x = xLeft
        while(x <= xRight):
            xs.append(x)
            y = a*(x**2) + b*x + c
            ys.append(y)
            x += dx
        pylab.title("Quadratic Equation Graph (Two Solutions)")
        pylab.plot(xs, ys, "ro-")
        pylab.show()
        break
    
        
        
        