from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#fig=plt.figure()
#ax =fig.add_subplot(111, projection='3d')

point = np.array([1,2,3])
normal = np.array([1,1,2])
point2 = np.array([1,3,4])

d = -point.dot(normal)

xx, yy = np.meshgrid(range(80),range(10))
print(xx)
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
print(z)

plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z,alpha=0.2)

plt3d.scatter(point2[0],point2[1],point2[2], color='green')
plt.show()

