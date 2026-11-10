a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
s = input("Введите действие (+, -, *, /): ")
if s == "+":
    result = a + b
elif s == "-":
    result = a - b
elif s == "*"
    result = a * b
elif s == "/":
    if b != 0:
        result = a / b
    else:
        result = "Ошибка (деление на ноль!)"
else:
    result = "Неверная операция"

print(f"Ответ: {result}")