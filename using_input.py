from math import *
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan
# Section: 575
# Assignment: Lab 2.9  Using Variables
# Date: 5/09/2022
#
print("This program calculates the applied force given mass and acceleration")
#calculating force
mass = float(input("Please enter the mass (kg): "))
acl = float(input("Please enter the acceleration (m/s^2): "))
force = (mass * acl)
print(f"Force is {force:.1f} N")

print("")
#calculating wavelength
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = (2*distance) * (sin(radians(angle)))
print(f"Wavelength is {wavelength:.4f} nm")

print("")
#calculating left over radon
print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days): "))
halflife = 3.8
initial = float(input("Please enter the initial amount (g):"))
radon = initial * (2 ** (-days / halflife))
print(f"Radon-222 left is {radon:.2f} g")

print("")
#Calculating Pressure 
print("This program calculates the pressure given moles, volume, and temperature")
gasc = 8.314
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temp = float(input("Please enter the temperature (K): "))
pressure = ((moles * gasc * temp) / volume) / 1000
print(f"Pressure is {int(pressure)} kPa")

