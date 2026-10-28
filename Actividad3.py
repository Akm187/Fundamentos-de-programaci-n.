
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


print("=== Factorial Calculator ===")

number = int(input("Ingresa un número no negativo: "))

if number < 0:
    print("Error: Por favor, ingresa un número entero no negativo.")
else:
    answer = factorial(number)
    print("La factorial de", number, "es", answer)
