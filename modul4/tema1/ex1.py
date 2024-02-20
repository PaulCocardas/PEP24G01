def functie(x):
    y = 3 * x
    return 3 * x ** 2 - 4 * y + 4

while True:
    x = int(input(" x = "))
    if x < 10 or x > 20:
        while True:
            x = int(input("Numarul trebuie sa fie in intervalul [10;20]"))
            if x >= 10 and x <= 20:
                break
    print(f"Rezultatul functiei: {functie(x)}")
