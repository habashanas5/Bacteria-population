import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
population = 100
rate = 0.1
Timestep = 0.005
duration = 20
t = 0
h = []
v = []
iteration = int(duration/Timestep)
for i in range (iteration):
    t = i*Timestep
    h.append(t)
    population = population + (population*rate) * Timestep
    v.append(population)
    print('f(' , {t} , {population} , ')')
plt.plot(h,v)
plt.show()
