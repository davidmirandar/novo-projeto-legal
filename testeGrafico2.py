from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def randrange(n, vmin, vmax):
	return (vmax - vmin) * np.random.rand(4) + vmin

fig=plt.figure()
ax =fig.add_subplot(111, projection='3d')

n = 100

#for c, m, zlow, zhigh in [('r','o', -50, -25),('b','^', -30, -5)]:
y = [1,2]
print(y)
xs = [-0.6508,-1.4492,2.0850,0.2569,0.0914]
xs2 = [0.2626,0.6418,1.1155,0.0121,-0.0429]
	#randrange(n,23,32)
ys =  [0.1097,0.8896,0.6876,0.6730,0.3399]
ys2 = [1.1476,1.0234,0.6043,0.5256,0.4660]
	#randrange(n,0,100)
zs = [4.0009,4.4005,12.0710,8.3265,7.0677]
zs2 = [7.7985,7.0427,7.4446,4.6316,5.4323]

	#randrange(n,zlow,zhigh)
#xs -1.4492 até 2.0850
#ys 0.1097 até 1.1476
#zs	4.0009 até 12.0710
#---------------------------------------
point = np.array([1,2,3])
normal = np.array([1,1,2])
point2 = np.array([1,3,4])

d = -point.dot(normal)

xx, yy = np.meshgrid(range(2),range(2))
print(xx)
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]
print(z)

#plt3d = plt.figure().gca(projection='3d')
ax.plot_surface(xx,yy,z,alpha=0.2)
#----------------------------------------
	#print(xs)
ax.scatter(xs,ys,zs,c='b',marker='o')
ax.scatter(xs2,ys2,zs2,c='r',marker='^')

ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')	
#axes3d.scatter(X,Y,Z,zdir='z',s=20,c='red',depthshade=True,*args,**kwargs)
plt.show()