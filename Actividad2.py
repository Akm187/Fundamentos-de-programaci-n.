
print("=== LIQUIDO O SOLIDO ===")

temperature = float(input("Ingresa la temperatura en celsius: "))

if temperature < 0:
    print("El agua esta en estado solido (hielo).")
elif temperature < 100:
    print("El agua esta en estado liquido")
else:
    print("El agua esta en estado gaseoso (vapor).")
