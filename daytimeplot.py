import matplotlib.pyplot as plt
import numpy as np 

#phi = np.linspace(0,2*np.pi,100) #Angular position of Earth in orbit starting with winter solstice (around december 22)
#n = 54.607868 #Latitude geographical coordinate from -pi/2 (south pole) to pi/2 (north pole)

def calc_plot(phi,n):
    theta = 23.5*np.cos(phi)
    y = np.sin(np.deg2rad(n))
    r = np.sqrt(1-y**2)
    x = y*np.tan(np.deg2rad(theta))
    Py = np.sqrt(r**2-x**2)
    alpha = np.arctan2(Py,x)
    alpha = np.nan_to_num(alpha) #Change nans to numbers for next line to work
    beta = (x**2<r**2) * (2*np.pi - 2*alpha)/(2*np.pi) + (abs(x)==x) * (x**2>r**2) #Extra checks for full night and full day
    plt.plot(phi,beta,label="Latitude: "+str(n))

calc_plot(np.linspace(0,2*np.pi,100),0)
calc_plot(np.linspace(0,2*np.pi,100),40)
calc_plot(np.linspace(0,2*np.pi,100),-70)
calc_plot(np.linspace(0,2*np.pi,100),80)
plt.legend()
plt.xlabel("orbital position in radians")
plt.ylabel("fraction of day in sunlight")

plt.show()