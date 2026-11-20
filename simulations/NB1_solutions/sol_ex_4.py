import numpy as np
import matplotlib.pyplot as plt


class ParticleClass():
    def __init__(self, m, v, r, R):
        self.m = m
        self.v = np.array(v, dtype=float)
        self.r = np.array(r, dtype=float)
        self.R = np.array(R, dtype=float)

    def update_position(self, dt):
        self.r += self.v * dt


particles = []
for i in range(10):
    particles.append(ParticleClass(m=1, v=[np.random.randint(-5, 5), 0.0], r=[np.random.randint(0, 4), 0.0], R=1))

    if len(particles) == 10:
        print(f"the position begin: {particles[0].r}, and velocity begin: {particles[0].v}, and dt: {0.5}")
        for k in range(len(particles) - 1):
            particles[k].update_position(0.5)


print(f"the position end: {particles[0].r}")
'''
plt.figure()
for particle in particles:
    plt.plot(particles[0].r, 'k.')
plt.show()
'''


