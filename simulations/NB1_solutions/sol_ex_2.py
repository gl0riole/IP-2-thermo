import numpy as np
import matplotlib.pyplot as plt


# Uitvoeren van de simulatie
def distance_dt(delta_t):

    t_e = 10                   #s
    N = int(t_e/delta_t)+1
    t = np.arange(0, t_e + delta_t,delta_t) #s
    # fietser 1
    x_1 = np.zeros(N)          #m     maakt array van lengte N met alleen maar waarde 0.
    v_1 = 5                    #m/s

    # fietser 2
    x_2 = np.zeros(N)          #m     
    v_2 = np.zeros(N)          #m/s     
    a_2 = .5                   #m/s^2     


    for i in range(0,N-1):
        x_1[i+1] = x_1[i] + v_1*delta_t
        
        x_2[i+1] = x_2[i] + v_2[i]*delta_t
        v_2[i+1] = v_2[i] + a_2*delta_t

    return np.max(x_1), np.max(x_2)

dinstance_1 = distance_dt(0.25)
dinstance_2 = distance_dt(1)

print(dinstance_1)
print(dinstance_2)

#by changing the dt value from 0.25 to 1 seconds, the maximum distance of fietser 1 is unchanged, 50.0 meters, while the maximum distance of fietser 2 changed from 24.375 to 22.5 meters. From the point of physics, the maximum distance of fietser 2 should be 24.374 meters, which is the distance covered by a constant acceleration of 0.5 m/s^2 over 10 seconds. The difference in the results is caused by inventing a larger time step dt = 1 (s) in the discretisation, as it is limited by 10 (s), concluding into less steps and less distance travelled.