def code(a):
    total = []
    for i in range(1, a + 1):
        for j in range(i + 1, a + 1):
            sum_ = i + j
            if a % sum_ == 0:
                total.append(i)
                total.append(j)
    return total

a = int(input("Введите число от 3 до 20: "))
if 3 <= a <= 20:
    total = code(a)
    print("Нужный пароль:",*total)
else:
    print("Число должно быть в диапазоне от 3 до 20.")