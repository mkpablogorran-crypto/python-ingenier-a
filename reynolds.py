rho = float (input("Enter the density of the fluid (kg/m^3): "))
V = float (input("Enter the velocity of the fluid (m/s): "))
D = float (input("Enter the diameter of the pipe (m): "))
mu = float (input("Enter the dynamic viscosity of the fluid (Pa*s): "))


Re = (rho * V * D) / mu

if Re < 2000:
    flow_type = "laminar"
elif Re >= 2000 and Re <= 4000:
    flow_type = "transitional"
else:
    flow_type = "turbulent"
    
print(f"The Reynolds number is: {Re:.2f}")
print(f"The flow type is: {flow_type}")
