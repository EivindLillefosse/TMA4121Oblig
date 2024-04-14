import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter 


# Bølgeligning løyst numerisk i 3 dimensjonar

#Variablar
L = 1 #Lengde
T = 40   #Total tid

h = 0.02   #Steglengde
k = 0.04   #Tidssteg

#Test k/h² >= 1/2
if k/h**2 < 1/2:
    print('k/h² < 1/2')
    print('Kan gi ustabil løysing')
else:
    print('k/h² >= 1/2')
    print('Stabil løysing')


#Tal på gridpunkt i x, y og t
n_X = int(L/h)
n_Y = int(L/h)
n_T = int(T/k)

#Lager grid
x = np.linspace(0, L, n_X)
y = np.linspace(0, L, n_Y)
t = np.linspace(0, T, n_T)

X, Y = np.meshgrid(x, y)

#setter initialbetingelse ein puls i midten
u = np.zeros((n_X, n_Y, n_T))
u[int(n_X/2) , int(n_Y/2), 0] = 1
u[int(n_X/2) , int(n_Y/2) + 1, 0] = 0.5
u[int(n_X/2) , int(n_Y/2) - 1, 0] = 0.5
u[int(n_X/2) + 1 , int(n_Y/2), 0] = 0.5
u[int(n_X/2) -1 , int(n_Y/2), 0] = 0.5


#Løysar bølgeligninga
#Første tidssteg
for i in range(1, n_X-1):
    for j in range(1, n_Y-1):
        u[i, j, 1] = u[i, j, 0] + k**2/2*(u[i+1, j, 0] - 2*u[i, j, 0] + u[i-1, j, 0] + u[i, j+1, 0] - 2*u[i, j, 0] + u[i, j-1, 0])

#Resten av tidsstega, ved hjelp av Euler explisit metode
for n in range(1, n_T-1):
    for i in range(1, n_X-1):
        for j in range(1, n_Y-1):
            u[i, j, n+1] = 2*(1-k**2)*u[i, j, n] - u[i, j, n-1] + k**2*(u[i+1, j, n] - 2*u[i, j, n] + u[i-1, j, n] + u[i, j+1, n] - 2*u[i, j, n] + u[i, j-1, n])
            
#Lager animasjon
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def animate(i):
    ax.clear()
    ax.plot_surface(X, Y, u[:, :, i], cmap='viridis')
    ax.set_zlim(-1, 1)
    ax.set_title('t = ' + str(t[i]))
    
ani = animation.FuncAnimation(fig, animate, frames=n_T, interval=10, blit=False, repeat=False, save_count=n_T)

# Lagrar animasjonen som ein gif-file
ani.save('C:/Users/eivin/Documents/c++/bolgeligning.gif', writer='imagemagick', fps=30)

plt.show()

# plt.show()