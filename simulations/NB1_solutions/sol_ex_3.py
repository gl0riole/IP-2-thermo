import numpy as np
import matplotlib.pyplot as plt

class ParticleClass():
    def __init__(self, v, r, R, m):
        self.m = m
        self.v = np.array(v, dtype=float)
        self.r = np.array(r, dtype=float)  
        self.R = np.array(R, dtype=float)

    def update_position(self, dt):
        self.r += self.v * dt


particle_array = []

for start_x in range(4):
    particle_array.append(ParticleClass(m=1, v=[2.0, 0], r=[start_x, 0.0], R=1.0))

for i in range(3):
    particle_array[0].update_position(0.2)
    particle_array[1].update_position(0.25)
    particle_array[2].update_position(0.5)
    particle_array[3].update_position(1.5)

print("huidige r van particle[0] : " + str(particle_array[0].r))

plt.figure()
for particle in particle_array:
    plt.plot(particle.r[0],'k.')
    plt.ylabel('r')
plt.show()

#!!!!посмотри можно ли использовать матрицу для записи всех растояний для каждого обьекта используя np.zero и append в матрицу!!!!!