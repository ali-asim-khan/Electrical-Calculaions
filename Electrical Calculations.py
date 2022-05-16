from cmath import sqrt

print("\n<<< Electrical Calculations >>>\n")

print("Enter 0 for unknown values")

A = int(input("Current(A): "))
V = int(input("Voltage(V): "))
W = int(input("Power(W): "))
C = int(input("Charge(C): "))
R = int(input("Resistance(Ω): "))
S = int(input("Time(S): "))
J = int(input("Energy Transfered(J): "))

# Current
if A == 0:
    if C != 0 and S != 0:
        print(C/S)
    elif V != 0 and R != 0:
        print(V/R)
    elif W != 0 and V != 0:
        print(W/V)
    elif W != 0 and R != 0:
        print(sqrt(W/R))
    else:
        print(J/(V*S))
else:
    print("Current: " + A)

# Voltage
if V == 0:
    if J != 0 and C != 0:
        print(J/C)
    elif A != 0 and R != 0:
        print(A*R)
    elif A != 0 and W != 0:
        print(W/A)
    else:
        print(J/(A*S))
else:
    print("Voltage: " + V)

# Power
if W == 0:
    if A != 0 and V != 0:
        print(A*V)
    elif A != 0 and R != 0:
        print((A*A)*R)
    else:
        print(J/S)
else:
    print("Power: " + W)

# Charge
if C == 0:
    if A != 0 and S != 0:
        print(A*S)
    else:
        print(J/V)
else:
    print("Charge: " + C)

# Resistance

if R == 0:
    if A != 0 and V != 0:
        print(V/A)
    else:
        print(W/(A*A))
else:
    print("Resistance: " + R)

# Time

if S == 0:
    if A != 0 and C != 0:
        print(A/C)
    elif J != 0 and W != 0:
        print(J/W)
    else:
        print(J/(A*V))
else:
    print("Time: " + S)

# Energy Transfered

if J == 0:
    if V != 0 and C != 0:
        print(V/C)
    elif W != 0 and S != 0:
        print(W*S)
    else:
        print(A*V*S)
else:
    print("Energy Transfered: " + J)