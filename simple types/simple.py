#Числа

def numbers():
    a = 2
    b = input ('введите число: ')
    print(a + float(b))

    v = float(input('Введите число от 1 до 10: '))
    print(v+10) 

#Строки

def strings():
    name = 'Александр'
    print(f'Привет, {name}') 

    name = input('Введите ваше имя: ')
    print(f'Привет, {name}! Как дела?') 

#Приведение типов
def types():
    print(float('1')) 
    print('2.5')  # ???
    print(bool(1))  # ???
    print(bool(''))  # ???
    print(bool(0))

numbers()
strings()
types()

