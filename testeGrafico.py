#encoding: utf-8

import matplotlib.pyplot as plot

plot.style.use('Solarize_Light2')
x = [1,2,3,4,5,6,7,8,9,10]
y = [11,12,13,14,15,16,17,18,19,20]
plot.plot(x, y)
plot.title('Primeiro Gráfico')
plot.xlabel('Eixo X')
plot.ylabel('Eixo Y')

plot.show()