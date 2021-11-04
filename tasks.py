import random
if __name__ == '__main__':
    cort2 = tuple([random.randint(-100, 100) for _ in range(100)])
    cort1 = tuple([random.randint(-100, 100) for _ in range(100)])
    proiz1 = 1
    proiz2 = 1
    for item in cort1:
       proiz1 *= item
    for item in cort2:
       proiz2 *= item
    print(f"{cort1}\n{cort2}\n{proiz1}\n{proiz2}")
    if proiz1 > proiz2:
        print("Произведение больше в 1-м кортеже")
    elif proiz1 < proiz2:
        print("Произведение больше в 2-м кортеже")
    else:
        print("Произведения равны")

    print(f"Макс индекс 1-го кортежа {cort1.index(max(cort1))} Макс индекс 2-го кортежа {cort2.index(max(cort2))}")

   # strings = input()
   # print({item: strings.count(item) for item in strings})

    print(set([random.randint(-100, 100) for _ in range(100)]) & set([random.randint(-100, 100) for _ in range(100)]))