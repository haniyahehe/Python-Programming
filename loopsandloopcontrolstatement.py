for i in range(1, 6):
    print("Number:", i)

    i = 1
while i <= 5:
    print("Number:", i)
    i += 1

    for row in range(1, 4):
       for col in range(1, 4):
        print(f"({row}, {col})", end=" ")
    print()

i = 1
while i <= 3:
    print(f"Outer Loop i={i}")
    for j in range(1, 4):
        print(f"    Inner Loop j={j}")
    i += 1

    for i in range(1, 6):
       if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("Number:", i)

    for i in range(1, 6):
       if i == 3:
        print("Skipping number:", i)
        continue
    print("Number:", i)

    for i in range(1, 6):
       if i == 3:
        pass
        print("Pass statement executed at i =", i)
    print("Number:", i)