try:
    a=float(input("Введите вещественное число A: "))
except ValueError:
    print("Вы допустили ошибку при вводе данных, попробуйте снова")
    a=float(input("Введите вещественное число A: "))
try:
    b=float(input("Введите вещественное число B: "))
except ValueError:
    print("Вы допустили ошибку при вводе данных, попробуйте снова")
    b=float(input("Введите вещественное число B: "))
try:
    c=float(input("Введите вещественное число C: "))
except ValueError:
    print("Вы допустили ошибку при вводе данных, попробуйте снова")
    c=float(input("Введите вещественное число C: "))
if (a<b) and (b<c):
    print("Да, A<B<C")
elif (a>b) and (b>c):
    print("Да, A>B>C")
else:
    print("Нет, ни одно из условий (A<B<C или A>B>C)не выполняется")

	
