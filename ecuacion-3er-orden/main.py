import math

machine.freq(270000000)

def cubica_real(a, b, c, d):
    # Cálculo de coeficientes auxiliares
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

    # Cálculo del discriminante
    discriminante = (q**2/4)+(p**3/27)
    
    if discriminante < 0:
        angulo = math.acos(-q/2*math.sqrt(-27/p**3))/3
        X1 = (2*math.sqrt(-p/3)*math.cos(angulo))-b/(3*a)
        X2 = (2*math.sqrt(-p/3)*math.cos(angulo+2*math.pi/3))-b/(3*a)
        X3 = (2*math.sqrt(-p/3)*math.cos(angulo+4*math.pi/3))-b/(3*a)
        
        print(f"a={a}; b={b}; c={c}; d={d}\n")
        print(f"X1 = {X1}")
        print(f"X2 = {X2}")
        print(f"X3 = {X3}")

    else:
        print("Esta implementación no puede resolver esta ecuación.")

# Ejemplo de uso:
a = 1
b = -6
c = 11
d = -6

cubica_real(a, b, c, d)