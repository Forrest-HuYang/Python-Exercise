import numpy
import matplotlib.pyplot as plt

#print(numpy.pi)

#x=numpy.arange(0, 2*numpy.pi, 0.01)
#y=numpy.sin(x)

x=numpy.arange(-20, 20, 0.01)
y=0.5*x**9-4*x**8+3*x**7-2*x**6+4*x**5
print(x)
print(y)
#plt.plot(x,y)
#plt.figure(figsize=(400,400),dpi=80) 
#plt.xlim(-20,20)
plt.ylim(-10**6,10**6)
plt.plot(x, y, 'r')
plt.show()

#t = numpy.arange(0., 5., 0.2)
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

#plt.show()  
