
at(input("ingrese la velocidad del perihelio"))
r1=float(input("ingrese la posicion del perihelio"))
g=6.67e-11
m=5.97e24
pi=3.1416
v2=(((2*g*m)/(v1*r1))+(((2*g*m)/(v1*r1))**2+4*((v1**2-2*g*m)/r1))**1/2)/r1
r2=(r1*v1)/v2
print("la velocidad del afelio es: ",v2)
print("la posicion del felio es: ",r2)
emay=(r1+r2)/2
emen=(r1*r2)**1/2
print("el eje mayor es: ",emay)
print("el eje menor es: ",emen)
t=(2*pi*(emay*emen))/r1*v1
e=(r2-r1)/(r1+r2)
print("el periodo es: ",t)
print("e es: ",e)
