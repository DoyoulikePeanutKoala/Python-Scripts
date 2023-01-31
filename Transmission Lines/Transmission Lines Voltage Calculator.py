#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Title: T-Line Reflection Calculator
# Author: Gerald Atwood
# Date Published: 1/30/2023
# Description: For EEET-433: Transmission Lines Course @ RIT. Calculates
# Transmission Line time delay, reflection coefficients, and the number 
# of reflected waves until the transmission line reaches its steady-state voltage


# In[2]:


# Modules
import math


# In[3]:


# Known Variables
Vs = 10 # Source Voltage, DC Source, Volts
Rs = 25 # Source Impedance, Ohms
d = 1 # Transmission Line Length, Meters
Ro = 50 # Transmission Line Impedance, Ohms
Vp = 3*(10**8) # Velocity of Propagation of Transmission Line, meters/second
Rl = 100 # Load Impedance, Ohms


# In[4]:


# Calculating Time Delay, reflection coefficients and initial voltage at input of T-Line
td = d/Vp # Time Delay of Transmission Line
r_s = (Rs - Ro)/(Rs + Ro) # Source Reflection Coeff.
r_l = (Rl - Ro)/(Rl + Ro) # Load Reflection Coeff.
Vf = round(((Ro)/(Rs + Ro)) * Vs,3) # Initial Voltage at T-Line Input
Vr = round(Vf*r_l,3) # Reflected Wave, first reflection
Vl = Vf + Vr # Load Voltage, first reflection
V_ss = round(Vs*((Rl)/(Rl + Rs)),3) # steady-State Voltage


# In[5]:


# Loop reflection calculations until equilibrium
Vf_list = []
Vr_list = []
Vf_list.append(Vf)
Vr_list.append(Vr)
V_line_list = Vr_list + Vf_list
numBounces = 2 # Number of times the signal has traveled through the T-Line
# NOTE: Starts at 2 since the first two reflections have already been calculated
while math.isclose(0,Vr_list[-1],abs_tol = 0.1) == False:
    Vf = round(Vr*r_s,3)
    Vf_list.append(Vf)
    numBounces += 1
    Vr = round(Vf*r_l,3)
    Vr_list.append(Vr)
    numBounces += 1
    


# In[6]:


# Print out Results
td_txt = "Time Delay: {:.3E} <Seconds>".format(td)
print(td_txt)
print()
r_s_txt = "Source Reflection Coeff: {:.3E}".format(r_s)
print(r_s_txt)
print()
r_l_txt = "Load Reflection Coeff: {:.3E}".format(r_l)
print(r_l_txt)
print()
V_ss_txt = "Steady-State Voltage: {:.3E} <Volts>".format(V_ss)
print(V_ss_txt)
print()
print("Source Reflection Voltages: ")
for i in Vf_list:
    print ("{:.3E} <Volts>".format(i))
print()
print("Load Reflection Voltages: ")
for i in Vr_list:
    print ("{:.3E} <Volts>".format(i))
print()
print("Num. of Reflections: {}".format(numBounces))


# In[ ]:




