import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy as cp


class ParticleClass():
    def __init__(self, m, v, r, R):
        self.m = m
        self.v = np.array(v, dtype=float)
        self.r = np.array(r, dtype=float)
        self.R = np.array(R, dtype=float)

    def update_position(self, dt):
        self.r += self.v * dt 

    @property
    def x(self):
        return self.r[0]
    
    @property
    def y(self):
        return self.r[1]

def info_particle(glist):
    for i, particle in enumerate(glist):
        print(f"particle {i}: r_begin = {particle.r}, v_begin = {particle.v}")

particles = [ParticleClass(m=1, v=[np.random.randint(-5, 5), 0.0], r=[np.random.randint(0, 4), 0.0], R=1) for _ in range(10)]
particles_c = cp(particles)
    
info_particle(particles)

for k in range(len(particles_c)):
    particles_c[k].update_position(0.5)


print("---------------------------------------")
info_particle(particles_c)


plt.figure()
plt.plot(particles[0].x, particles[0].y, 'b.')
plt.plot(particles[1].x, particles[1].y,'r.')
plt.plot(particles[2].x, particles[2].y,'g.')
plt.show()




