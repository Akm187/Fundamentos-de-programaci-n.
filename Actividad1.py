
print("=== CALIFICACIÓN ===")

name = input("Ingresa tu nombre: ")
grade = float(input("Ingresa tu calificación (1-100): "))

if grade < 0 or grade > 100:
    print("Calificación invalida, por favor usa del 1 al 100.")
elif grade >= 70:
    print("Felicidades,", name + "!")
    print("Pasaste.")
else:
    print("Lo siento,", name + ".")
    print("Reprobaste.")
