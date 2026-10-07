## Alejandra Rivera Valenzuela NC 0200
## Ejercisios de python 

# ==========================================
# EJERCICIOS DE PYTHON - W3SCHOOLS
# (1 ejemplo por tema)
# ==========================================

# ------------------------------------------
# 1. Basic Conditions (Condiciones Básicas)
# Ref: https://www.w3schools.com/python/python_conditions.asp
# ------------------------------------------
print("--- 1. Condiciones Básicas ---")
a = 33
b = 200

if b > a:
    print("b es mayor que a")

print()


# ------------------------------------------
# 2. If...Elif (Estructura Condicional Elif)
# Ref: https://www.w3schools.com/python/python_if_elif.asp
# ------------------------------------------
print("--- 2. If...Elif ---")
x = 33
y = 33

if y > x:
    print("y es mayor que x")
elif x == y:
    print("x e y son iguales")

print()


# ------------------------------------------
# 3. If...Else (Estructura Condicional Else)
# Ref: https://www.w3schools.com/python/python_if_else.asp
# ------------------------------------------
print("--- 3. If...Else ---")
nota = 65

if nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

print()


# ------------------------------------------
# 4. For Loops (Bucle For)
# Ref: https://www.w3schools.com/python/python_for_loops.asp
# ------------------------------------------
print("--- 4. Bucle For ---")
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

print()


# ------------------------------------------
# 5. While Loops (Bucle While)
# Ref: https://www.w3schools.com/python/python_while_loops.asp
# ------------------------------------------
print("--- 5. Bucle While ---")
i = 1

while i < 6:
    print(i)
    i += 1