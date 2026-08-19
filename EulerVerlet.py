import numpy as np
import matplotlib.pyplot as plt


G = 1.0          
                
M = 1000.0      
m = 1.0         

pos = np.array([10.0, 0.0])  
vel = np.array([0.0, 10.0])  


dt = 0.05
steps = 5000

trajectory = []

def compute_acc(pos):
    r_vec = -pos
    r = np.linalg.norm(r_vec)
    r_hat = r_vec / r
    a_mag = G * M / r**2
    acc =  a_mag * r_hat
    return acc, r




acc, r = compute_acc(pos)  

energies = []               
trajectory = []

for step in range(steps):
    vel = vel + acc * (dt/2)
    pos = pos + vel * dt
    acc, r = compute_acc(pos) 
    vel = vel + acc * (dt/2)

    KE = 0.5 * m * np.dot(vel, vel)
    PE = -G * M * m / r     
    energies.append(KE + PE)

    trajectory.append(pos.copy())



trajectory = np.array(trajectory)
plt.figure(figsize=(6,6))
plt.plot(trajectory[:,0], trajectory[:,1])
plt.plot(0, 0, 'yo', markersize=15)
plt.axis('equal')
plt.title("Orbit (Euler integration)")
plt.show()
plt.figure()
plt.plot(energies)
plt.xlabel("step")
plt.ylabel("Total energy")
plt.title("Energy vs time (Verlet)")
plt.show()
